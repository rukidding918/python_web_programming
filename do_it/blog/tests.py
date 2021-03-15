from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.test import TestCase, Client

from blog.models import Post, Category

# Create your tests here.
class TestView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Post.objects.count(), 0)
        main_area = BeautifulSoup(response.content, 'html.parser').find('div', {'id': 'main-area'})
        self.assertIn('아직 게시물이 없습니다', main_area.text)

        self.user_trump = User.objects.create_user(username='trump', password='trumppassword')
        self.user_obama = User.objects.create_user(username='obama', password='obamapassword')
        self.category_programming = Category.objects.create(name='프로그래밍', slug='프로그래밍')
        self.category_music = Category.objects.create(name='음악', slug='음악')

        post_001 = Post.objects.create(
            title='첫번째',
            content='첫번째포스트',
            author=self.user_trump,
            category=self.category_programming
        )
        post_002 = Post.objects.create(
            title='두번째',
            content='두번째포스트',
            author=self.user_obama,
            category=self.category_music
        )
        self.assertEqual(Post.objects.count(), 2)
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertIn(post_001.title, soup.text)
        self.assertIn(post_002.title, soup.text)

    def post_detail_test(self):
        post_001 = Post.objects.create(title='첫번째', content='첫번째포스트')
        self.assertEqual(post_001.get_absolute_url(), '/blog/1/')

    def test_create_post(self):
        # self.test_post_list()
        response = self.client.get('/blog/create_post/')
        self.assertEqual(response.status_code, 302)
        self.user_trump = User.objects.create_user(username='trump', password='trumppassword')
        self.client.login(username='trump', password='trumppassword')
        response = self.client.get('/blog/create_post/')
        self.assertEqual(response.status_code, 200)
        self.client.post(
            '/blog/create_post/',
            {
                'title': 'new_trump',
                'content': 'new_trump_content',
            }
        )
        last_post = Post.objects.last()
        self.assertEqual(last_post.title, 'new_trump')
        self.assertEqual(last_post.author.username, 'trump')

    def test_update_post(self):
        update_post_url = f'/blog/update_post/{self.post_001.pk}'


        #로그인 하지 않은 경우
        response = self.client.get(update_post_url)
        self.assertNotEqual(response.status_code, 200)

        #로그인 했지만 작성자가 아닌 경우
        self.assertNotEqual(self.post_001.author, self.user_trump)

