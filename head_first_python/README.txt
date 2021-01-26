모듈을 만들려면

1. 모듈 폴더 안에서 setup.py, README.txt 파일을 만들어야 한다.
1-1. setup.py 안에 여러 정보를 삽입한다.
1-2. README.txt 안에는 굳이 내용이 있을 필요는 없다.

2. 폴더 안에서 python setup.py sdist를 실행한다. 그러면 dist 폴더가 생기고 그 안에 압축파일이 생긴다.

3. dist 폴더 안에서 pip install [압축파일명]을 실행하면 모듈 설치 완료.
3-1. python -m venv env 를 실행하여 환경을 미리 만들어주고 모듈을 설치하면 더 좋다.

4. PyPI에 배포해서 사용하면 더 좋다. 이거는 알아서 해보자.