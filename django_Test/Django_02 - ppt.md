# Django_02 - ppt

## Model

- 단일한 데이터에 대한 정보를 가짐.
    - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함.
- 저장된 데이터베이스의 구조(lay out)
- Django는 model을 통해 데이터에 접속하고 관리
- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑됨.

## Database

- 데이터베이스(DB)
    - 체계화된 데이터의 모임
- 쿼리(Query)
    - 데이터를 조회하기 위한 명령어
    - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
    - "Query를 날린다."  --> DB를 조작한다.

## Database의 기본 구조

- 스키마(Schema)

    - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조 (structure)

- 테이블(Table)

    - 열(column) : 필드(Field) or 속성
    - 행(row): 레코드 (record) or 튜플 
    - PK(기본키) : 각 행의 고유값으로 Primary Key 로 불린다.

     반드시 설정해야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.

## Model 정리

- "웹 애플리케이션의 데이터를 구조화 하고 조작하기 위한 도구."

# ORM

## ORM

- Object - Relational - Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 (Django-SQL) 데이터를 변환하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS을 연동할 때 , 데이터베이스와 객체 지향 프로그래밍 언어간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법.
- Django는 내장 Django ORM을 사용함.

## ORM의 장점과 단점

- 장점
    - SQL을 잘 알지 못해도 DB조작이 가능
    - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
- 단점
    - ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음
- 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것. (생산성)

## ORM을 사용하는 이유!

- " 우리는 DB를 객체(object)로 조작하기 위해 ORM을 사용한다.!"

## models.py 작성

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
    - django.db.models. 모듈의 Model 클래스를 상속받음
- models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의.
    - title과 content은 모델의 필드를 나타낸다.
    - 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑된다. 

## 사용 모델 필드

- CharField(max_length=None)
    - 길이의 제한이 있는 문자열을 넣을 때 사용
    - CharField의 max_length는 필수인자.
    - 필드의 최대 길이(문자), 데이터베이스 레벨과 Django의 유효성 검사(값을 검증하는 것)에서 활용.
- TextField(**options)
    - 글자의 수가 많을 때 사용
    - max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에 반영은 되지만 모델과 데이터베이스 수준에는 적용되지 않음.
        -  max_length 사용은 CharField 에서 사용해야 함.

# Migrations

## Migrations

- Django가 model에 생긴 변화를 반영하는 방법
- Migration(이하 마이그레이션) 실행 및 DB 스키마를 다루기 위한 몇가지 명령어
    - makemigrations
    - migrate
    - sqlmigrate
    - showmigrations

## Migrations Comaands

1. makemigrations
    - model을 변경한 것에 기반한 새로운 마이그레이션(like 설계도)을 만들 때 사용
2. migrate
    - 마이그레이션을 DB에 반영하기 위해 사용
    - 설계도를 실제 DB에 반영하는 과정
    - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룬다.
3. sqlmigrate
    - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
    - 마이그레이션이 SQL문으로 어떻게 해석되어서 동작할지 미리 확인 할 수 있음.
4. showmigrations
    - 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
    - 마이그레이션 파일들이 migrate됐는지 안됐는지 여부를 확인 할 수 있음.

## DateField's options

- auto_now_add

    - 최초 생성 일자

    - Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신

        (테이블에 어떤 값을 최초로 넣을 때 )

- auto_now
    - 최종 수정 일자
    - Django ORM이 save를 할 때 마다 현재 날짜와 시간으로 갱신.



# Database API

## DB API

- DB를 조작하기 위한 도구
- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- Modle을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듦
- database-abstract API혹은 database-access API 라고도 함



## DB API 구문 - Making Queries 

- Article.objects.all() --------- Class Name, Manager, QuerySetAPI

## DB API

- Manager
    - Django 모델에 데이터베이스 Query 작업이 제공되는 인터페이스
    - 기본적으로 모든 Django 모델 클래스에 objects 라는 Manager를 추가
- QuerySet
    - 데이터베이스로부터 전달받은 객체 목록
    - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
    - 데이터베이스로부터 조회, 필터, 정렬 등을 수행 할 수 있음

## Django shell

- 일반 Python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음
- 그래서 장고 프로젝트 설정이 load 된 Python shell을 활용해 DB API 구문 테스트 진행



- 기본 Django shell 보다 더 많은 기능을 제공하는 shell_plus를 사용해서 진행
    - Django-sxtensions 라이브러리의 기능 중 하나.

# CRUD

## CRUD

- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 

    Create(생성), Read(읽기), Update(갱신), Delete(삭제)를 묶어서 일컫는 말



## READ

전체 article 객체 조회

```
Article.objects.all()
<QuerySet []>

# 이 때, 레코드가 하나만 있으면 인스턴스 객체로, 두 개 이상이면 쿼리셋으로 리턴
```



## CREATE

CREATE 첫 번째 방법

- 인스턴스 생성 후 인스턴스 변수 설정

```python
article = Article() #Article(class)로부터 article(instance)
article
<Article: Article object(None)>

article.title = 'first' #인스턴스 변수(title)에 값을 할당
article.content = 'django!' #인스턴스 변수(content)에 값을 할당

#save를 하지 않으면 아직 DB에 값이 저장되지 않음
article
<Article: Article object(None)>

Article.objects.all()
<QuerySet []>
#save를 하고 확인하면 저장된 것을 확인할 수 있다.
article.save()
article
<Article:  Article object(1)>
Article.objects.all()
<Query [Article: Article object (1)]>

```

- CREATE 두 번째 방법
    - 초기값과 함께 인스턴스 생성

```python
article = Article(title='second', content='django!!')
# 아직 저장이 안되어 있음
article
<Article : Article object (None)>
# save를 해주면 저장이 됨.
>>> article.save()
>>> article
<Article: Article object(2)>
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)> , <Article: Article object(2)>]>

# 값 확인
>>> article.pk
2
>>> article.title
'second'
>>> article.content
'django!'
```

- CREATE 세번째 방법
    - QuerySetAPI - create() 사용

```python
Article.objects.create(title='third', content='django!')
<Article: Article object(3)>
```

## CREATE 관련 메서드

- .save() method
    - saving objects
    - 객체를 데이터베이스에 저장함
    - 데이터 생성 시 save()를 호출하기 전에는 객체의 ID 값이 무엇인지 알 수 없음
        - ID값은 Django가 아니라 DB에서 계산되기 때문
    - 단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save()가 필요.

## str method

표준 파이썬 클래스의 메소드인 str()을 정의하여 각각의 object가 사람이 읽을 수 있는 문자열을 반환(return) 하도록 할 수 있음.

**작성 후 반드시 shell_plus를 재시작해야 반영됨.**

## READ

- QuerySet API method 를 사용해 다양한 조회를 하는 것이 중요
- QuerySet API method는 크게 2가지로 분료
    1. Methods that return new querysets
    2. Methods that do not return querysets

- **all()**
    - 현재 QuerySet의 복사본을 반환
    - Article. objects.all()

- **get()**

    - 주어진 lookup 매개변수와 일치하는 객체를 반환

    - 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고,

        둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생 시킴

    - 위와 같은 특징을 가지고 있기 때문에 primary key 와 같이 고유(unique)성을 보장하는 조회에서 사용해야 함.

- **filter()**
    - 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

## UPDATE

![image-20220415211205724](C:/Users/vr199/Desktop/django_Test/Django_02%20-%20ppt.assets/image-20220415211205724.png)

article 인스턴스 객체의 인스턴스 변수의 값을 변경 후 저장

## DELETE

- delete()

    - QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행하고,

        삭제된 객체 수와 객체 유형당 삭제 수가 표함된 딕셔너리를 반환

![image-20220415211336898](C:/Users/vr199/Desktop/django_Test/Django_02%20-%20ppt.assets/image-20220415211336898.png)

## Field lookups

- 조회 시 특정 검색 조건을 지정
- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인수로 지정됨.
- 사용 예시)
    - Article.objecs.filter(pk __ gt=2)
    - Article.objects.filter(content__contains='ja')

이 부분에 대해서는 더 알아보자. 

========================================제외===============================================

# Admin Site

## Automatic admin interface

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- Model class를 admin.py에 등록하고 관리
- django.contrib.auth 모듈에서 제공됨
- record 생성 여부 확인에 매우 유용하며, 직접 record를 삽입할 수도 있음.

## admin 생성

```python
python manage.py createsuperuser
```

## admin 등록

```python
# articles/admin.py
from django.contrib import admin
from .models import Article

#admin site에 register하겠다.
admin.site.register(Article)
```

- admin.py는 관리자 사이트에 Article 객체가 관리자인터페이스를 가지고 있다는 것을 알려주는 것.

- models.py에 정의한 /__/str/__/의 형태로 객체가 표현됨.

## ModelAdmin options



- ![image-20220415212432872](C:/Users/vr199/Desktop/django_Test/Django_02%20-%20ppt.assets/image-20220415212432872.png)**list_display**
    - models.py 에서 정의한 각각의 속성(칼럼)들의 값(레코드)을 admin 페이지에 출력하도록 설정.

- **list_filter, list_display_link 등 다양한 ModelAdmin options 참고**

    

# CRUD with views

## HTTP method

- GET
    - 특정 리소스를 가져오도록 요청 할 떄 사용
    - 반드시 데이터를 가져올 때만 사용해야 함
    - DB에 변화를 주지 않음
    - CRUD에서 R역할을 담당
- POST
    - 서버로 데이터를 전송할 때 사용
    - 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
    - 서버에 변경사항을 만듦
    - CRUD 에서 C/U/D역할을 담당

## 사이트 간 요청 위조( Cross - site - request forgery )

- 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법.
- Django는 CSRF에 대항하여 middleware와 template tag를 제공
- CSRF라고도 함.

## CSRF 공격 방어

- Security Token 사용 방식 (CSRF Token)
    - 사용자의 데이터에 임의의 난수 값을 부여해, 매 요청마다 해당 난수 값을 포함시켜 전송 시키도록 함
    - 이후 서버에서 요청을 받을 때마다 전달된 token값이 유효한지 검증
- 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용(GET 제외)
- Django는 CSRF token 템플릿 태그를 제공

## csrf_token template tag

```django
{% csrf_token %}
```

- CSRF 보호에 사용
- input type이 hidden으로 작성되며 value는 Django에서 생성한 hash값으로 설정됨
- 해당 태그 없이 요청을 보낸다면 Django 서버는 **403 forbidden**을 응답.

## CsrfViewMiddleware

- CSRF 공격 관련 보안 설정은 settings.py에서 Middleware에 작성되어있음
- 실제로 요청 과정에서 urls.py 이전에 Middleware의 설정 사항들은 순차적으로 거치며 응답은 반대로 하단에서 상단으로 미들웨어를 적용시킴.

## Middleware

- 공통 서비스 및 기능을 애플리케이션에 제공하는 소프트웨어
- 데이터 관리, 애플리케이션 서비스, 메시징, 인증 및 API 관리를 주로 미들웨어를 통해 처리
- 개발자들이 애플리케이션을 보다 효율적으로 구축할 수 있도록 지원하며, 애플리케이션, 데이터 및 사용자 사이를 연결하는 요소처럼 작동

## Django shortcut function - 'redirect()'

- 새 url로 요청을 다시 보냄
- 인자에 따라 HttpResponseRedirect를 반환
- 브라우저는 현재 경로에 따라 전체 UrL 자체를 재구성 (reconstruct)
- 사용 가능한 인자
    - model
    - view name
    - absolute or relative URL