from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'single_pages/landing.html', {'title': '대문'})

def about_me(request):
    return render(request, 'single_pages/about_me.html', {'title': '저는요'})