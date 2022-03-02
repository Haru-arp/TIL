# Django The Web Framework

## Web Framework

### Web

- World Wide Web
- 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세게적인 정보 공간

### Static web page (정적 웹 페이지) 

- 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지

- 서버가 정적 웹 페이지에 대한 요청을 받은 경우

    서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄

- 모든 상황에서 모든 사용자에게 동일한 정보를 표시
- 일반적으로 HTML, CSS, JavaScript로 작성됨
- flat page라고도 함

### Dynamic web page(동적 웹 페이지)

- 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
- 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
- 서버 사이드 프로그래밍 언어 (Python, Java, C++등)가 사용되며, 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

### Framework

- 프로그래밍에서 특정 운영체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
- 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
- Application framework라고도 함

### Web framework

- 웹페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 데이터베이스 연동, 템플릿 형태의 표준, 세션관리, 코드 재사용 등의 기능을 포함.
- 동적인 웹 페이지나, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application framework의 일종

<hr>

## Django를 사용해야 하는 이유

- 검증된 Python 언어 기반 Web framework
- 대규모 서비스에도 안정적이며 오랫동안 세계적인 기업들에 의해 사용됨.
    - Ex) Spotify, Instagram, Dropbox, Delivery Hero

## Framework Architecture

- MVC Design Pattern (model - view - controller)
- 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
- 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나, 이면에서 실행되는 부분을 서로 영향없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음. 
- Django는 MTV Pattern 이라고 함.

## MTV Pattern

- Model
    - 응용 프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
- Template
    - 파일의 구조나 레이아웃을 정의
    - 실제 내용을 보여주는 데 사용(Presentation)
- View
    - HTTP 요청을 수신하고 HTTP 응답을 반환
    - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
    - Template에게 응답의 서식 설정을 맡김
- MTV
    - M : model
    - T : template
    - V : view

<hr>

# Django Intro

## Django 시작하기

- Django 설치 전 가상환경 생성 및 활성화

- Django 설치 

- 프로젝트 생성

    ```python
    django-admin startproject <프로젝트명>
    ```

- Django 서버 시작하기(활성화)

    ```python
    python manage.py runserver
    ```

- 메인 페이지 로켓 확인

<hr>

## 프로젝트 구조

- _ _ init _ _.py 

    - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시

- asgi.py

    - Asynchronous Server Gateway Interface 
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움

- settings.py

    - 애플리케이션의 모든 설정을 포함

- urls.py

    - 적절한 views의 연결을 지정

- wsgi.py

    - Web Server Gateway Interface
    - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움

- manage.py

    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티.

        ```django
        python manage.py <command> [options]
        ```

<hr>

## Application 생성

- 일반적으로 Application명은 복수형으로 하는 것을 권장

    ```django
    ex) python manage.py startapp articles
    ```

- admin.py 

    - 관리자용 페이지를 설정 하는 곳

- apps.py

    - 앱의 정보가 작성된 곳

- models.py

    - 앱에서 사용하는 Model을 정의하는 곳

- tests.py

    - 프로젝트의 테스트 코드를 작성하는 곳

- views.py

    - view 함수들이 정의 되는 곳

<hr>

## Project & Application

- ### Project

    - project(이하 프로젝트)는 Application(이하 앱)의 집합 (collection of apps)
    - 프로젝트에는 여러 앱이 포함될 수 있음
    - 앱은 여러 프로젝트에 있을 수 있음.

- ### Application

    - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
    - 하나의 프로젝트는 여러 앱을 가짐
    - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함.
        

<hr>

## 앱 등록

프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 추가해야 한다.

__INSTALLED_APPS__

- Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록.

## __앱 생성 시 주의 사항__ 

- 반드시 생성 후 등록!!
- INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않음.

<hr>

# 요청과 응답

## URLs

- HTTP 요청(request)을 알맞은 view로 전달

## View

- HTTP요청을 수신하고 HTTP응답을 반환하는 함수 작성
- Model을 통해 요청에 맞는 필요데이터에 접근
- Template에게 HTTP응답 서식을 맡김

## Templates

- 실제 내용을 보여주는데 사용되는 파일 
- 파일의 구조나 레이아웃을 정의 (ex HTML)
- template 파일 경로의 기본 값은 app 폴더 안의 templates 폴더로 지정되어있음. (샌드위치 구조)

## 추가 설정

- LANGUAGE_CODE

    - 모든 사용자에게 제공되는 번역을 결정

    - 이 설정이 적용되려면 USE_I18N이 활성화 되어 있어야 함.

        ```django
        #settings.py
        LANGUAGE_CODE = 'ko-kr'
        TIME_ZONE = 'Asia/Seoul'
        ```

- TIME_ZONE

    - 데이터베이스 연결의 시간대를 나타내는 문자열 지정

    - USE_TZ가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면, 

        UTC대신 새로 설정한 시간대의 인식 날짜 & 시간이 반환됨

    - USE)TZ이 False 인 상태로 이 값을 설정하는 것은 error가 발생하므로 주의

- USE_I18N
    - Django의 번역 시스템을 활성화해야 하는지 여부를 지정
- USE_L10N
    - 데이터의 지역화 된 형식(localized formatting)을 기본적으로 활성화할지 여부를 지정
    - True일 경우, Django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시
- USE_TZ
    - datatimes가 기본적으로 시간대를 인식하는지 여부를 지정
    - True일 경우 Django는 내부적으로 시간대 인식 날짜/ 시간을 사용