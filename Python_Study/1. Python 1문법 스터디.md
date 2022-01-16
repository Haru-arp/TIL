#  숫자형 

## 	숫자형이란?

- __숫자형(Number)__이란 숫자 형태로 이루어진 자료형.

- __정수, 실수, 8진수, 16진수__ 같은 것들이 있다. 

  |  항목  |      파이썬 사용 예      |
  | :----: | :----------------------: |
  |  정수  |       123, -456, 0       |
  |  실수  | 123.45 , -1234.5, 3.4e10 |
  | 8진수  |        0o34, 0o25        |
  | 16진수 |        0x2A, 0xFF        |

   ## 숫자형 만들기

- __정수형__ : 정수형 (Integer)이란 정수를 뜻하는 자료형이다. 

  ```python
  a = 123
  a = -178
  a = 0
  ```

- __실수형__ :  실수형(Floating-point)은 소수점이 포함된 숫자.

  ```python
  a = 1.2
  a = -3.45
  a = 4.24E10
  a = 4.24e-10
  ```

- __8진수와 16진수__ : 8진수(Octal)를 만들기 위해서 숫자가 0o또는 0O로 시작, 16진수를 만들기 위해서는 0x로 시작.

  ```python	
  a = 0o177
  a = 0x8ff
  b = 0xABC
  ```

## 	숫자형을 활용하기 위한 연산자.

- __사칙연산__ 

  덧셈, 뺄셈, 곱셈, 나눗셈인 사칙연산을 수행

  ```python
  a = 3
  b = 4
  a + b 
  7
  ```

  ``` python
  a * b
  12
  a / b
  0.75
  ```

- x의 y제곱을 나타내는 ** 연산자.
  제곱값을 돌려주는 연산자 **

  ```python
  a = 3
  b = 4
  a ** b 
  81(3^4)
  ```

- 나눗셈 후 나머지를 반환하는 %연산자

  나머지를 돌려주는 연산자 %

  ```python
  7 % 3 
  1
  
  3 % 7
  3
  ```

- 나눗셈 후 몫을 반환하는 //연산자

  ```python
  7 / 4
  1.75
  
  7 // 4
  1
  ```

  정수값만 돌려준다.

- __연습문제__

  ```python
  숫자 14를 3으로 나누었을 때 몫과 나머지를 확인해보자
  14 //3 
  4
  
  14 % 3
  2
  ```

  

# 문자열 자료형

		## 		문자열이란? 

- 문자열이란 문자, 단어 등으로 구성된 문자들의 집합.

  ```python
  "Life is too short, You need Python"
  "a"
  "123"
  ```

  따옴표로 둘러싸여 있으면 모두 문자열이라고 보면 된다.

## 		문자열은 어떻게 만드나?

1. 큰따옴표(" ")

   ```python
   "Hello World"
   ```

2. 작은따옴표(' ')

   ```python
   'Python is fun'
   ```

3. 큰따옴표 3개를 연속(" " ")

   ```python
   """Life is too short, You need python"""
   ```

4. 작은따옴표 3개를 연속(' ' ')

   ```python
   '''Life is too short, You need python'''
   ```

   왜 4가지냐?

## 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때 

​	1.문자열에 작은따옴표(') 포함시키기

```python
food = "Python's favorite food is perl"
```

​		문자열 안에 작은따옴표가 있을 때 문자열을 큰따옴표로 둘러싸야지 기호로 인식되지 않는다.



2. 문자열에 큰따옴표(") 포함시키기

   ```python
   say = '"Python is very easy." he says'
   ```

   위와 같이 큰따옴표가 포함된 문자열이라면 문자열을 작은따옴표로 둘러싸면 된다.

   

3. 백슬래시(\\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기

   ```python
   food = 'python\'s favorite food is perl'
   say = "\"python is very easy.\" he says."
   ```

   백슬래시를 작은따옴표나 큰따옴표 앞에 삽입하면 백슬래시 뒤의 작은 따옴표나 큰따옴표는 문자열을 둘러싸는 기호의 의미가 아니라 문자 그 자체를 뜻하게 된다.

## 여러줄인 문자열을 변수에 대입하고 싶을 때 

​	1.줄을 바꾸는 이스케이프 코드 '\ n' 삽입하기.

```python
multiline = "Life is too short\nYou need python"
```

\n을 삽입하는 방법은 읽기에 불편하고 줄이 길어지는 단점이 있다.

 2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기

    -  위 1번의 단점을 극복하기 위해서 큰따옴표 3개와 작은따옴표 3개를 사용한다. 

      ```python
      multilime='''
      Life is too short
      You need Python
      '''(작은따옴표 3개를 사용한 경우)
      ```

      ```python
      multiline="""
      Life is too short
      You need Python
      """(큰따옴표 3개를 사용한 경우)
      ```

      

# 문자열 연산하기

 	파이썬에서는 문자열을 더하거나 곱할 수 있다. 방법에 대하여 알아보자

1. 문자열 더해서 연결하기 (Concatenation)

   ```python
   head = "Python"
   tail = "is fun!"
   head + tail
   'Python is fun!'
   ```

 2. 문자열 곱하기

    ```python
    a = "Python"
    a * 2
    'PythonPython'
    ```

3. 문자열 곱하기 응용

   ```python
   #multistring.py
   print("=" * 50)
   print("My Program")
   print("=" * 50)
   
   ===============================================
   My Program
   ===============================================
   ```

4. 문자열 길이 구하기

   ```python
   a = "Life is too short"
   len(a)
   17
   ```

   문자열의 길이는 다음과 같이 len함수를 사용하면 구할 수 있다. len함수는 print함수처럼 파이썬의 기본 내장함수로 별다른 설정 없이 바로 사용할 수 있다.

## 문자열 인덱싱과 슬라이싱

- 인덱싱(Indexing)이란. 

  ​	무엇인가를 '가르킨다' 는 의미.

- 슬라이싱(Slicing)이란.

  ​    무엇인가를 '잘라낸다' 는 의미.

### 문자열 인덱싱이란?

```python
a = "Life is too short, You need Python"
a[3]
'e'
```

a[3]이 뜻하는 것은 a라는 문자열의 네 번째 문자 e를 말한다.  

__"파이썬은 0부터 숫자를 센다."__

### 문자열 인덱싱 활용하기

ex)

``` python
a = "Life is too short, You need Python"
a[0]
'L'
a[12]
's'
a[-1]
n
```

a[-1]의 의미는? 

- a[-1]은 뒤에서부터 세어 첫 번째가 되는 문자를 말함. 그러므로 뒤에서부터 첫번째는 n입니다.

a[-0] = ??

```python
a[-0]
'L'
```

### 문자열 슬라이싱이란?

단어를 뽑아내는 방법

```python
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b
'Life'
```

효율적인 방법 

```python
a = "Life is too short, You need Python"
a[0:4]
'Life'
```

왜 0부터 4일까?

슬라이싱 기법으로 a[시작번호:끝번호]를 지정할 때 끝 번호에 해당하는 것은 포함하지 않는다. a[0:3]을 수식으로 나타내면 다음과 같다.

0 <= a < 3



### 문자열을 슬라이싱 하는 방법

```python
a[0:5]
'Life '

a[0:2]
'Li'

a[5:7]
'is'

a[12:17]
'short'
```

a[시작번호 : 끝번호]에서 끝 번호 부분을 생략하면 시작번호부터 그 문자열의 끝까지 뽑아낸다

a[시작번호 : 끝번호]에서 시작번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.

```python
a[:17]
'Life is too short'
```

시작번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지를 뽑아낸다.

```python
a[:]
'Life is too short, You need Python'
```

# 문자열 포매팅

## 문자열 포매팅 따라하기

1. 숫자 바로 대입 : 숫자를 대입할 때는 %d를 넣어야 한다.

   ```python
   "I eat %d apples." % 3
   'I eat 3 apples'
   ```

2. 문자열 바로 대입 : 문자열을 대입할때는 %s를 넣어야 한다.

   ```python
   "I eat %s apples." %"five"
   'I eat five apples.'
   ```

   

3. 숫자 값을 나타내는 변수로 대입

   ```python
   number = 3 
   "I eat %d apples." % number
   'I eat 3 apples'
   ```

4. 2개 이상의 값 넣기

   ```python
   number = 10
   day = "three"
   "I ate %d apples. so I was sick for %s days." %(number, day)
   'I ate 10 apples. so I was sick for three days.'
   ```

##  문자열 포맷 코드

| 코드 |           설명            |
| :--: | :-----------------------: |
|  %s  |      문자열(String)       |
|  %c  |    문자 1개(Character)    |
|  %d  |       정수(Integer)       |
|  %f  | 부동 소수(Floating-point) |
|  %o  |           8진수           |
|  %x  |          16진수           |
|  %%  | Literal %(문자 '%' 자체)  |

%s 포맷코드인데 이 코드는 어떤 형태의 값이든 변환해 넣을 수 있다. 

```python
"I have %s apples" % 3
'I have 3 apples'
"rate is %s" % 3.234
'rate is 3.234'
```

%s는 자동으로 %뒤에 있는 값을 문자열로 바꾸기 때문이다.

## 포맷 코드와 숫자 함께 사용하기

1. 정렬과 공백

   ```python
   "%10s" % "hi"
   '        hi'<------오른쪽 정렬
   
   
   "%-10sjane" %'hi'
   'hi        jane'
   ```

2. 소수점 표현하기

```python
"%0.4f" % 3.42134234
'3.4213'
```

소수점 4번째 자리까지만 나타내고 싶은 경우에는 위와같이 사용.

```python
"%10.4f" %3.42134234
'     3.4213'
```

소수점 4번째 자리까지만 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬하는 예.



## format 함수를 사용한 포매팅

### 숫자 바로 대입하기

```python
"I eat {0} apples" .format(3)
'I eat 3 apples'
```

### 문자열 바로 대입하기

```python
"I eat {0} apples" .format("five")
'I eat five apples'
```

### 숫자 값을 가진 변수로 대입하기

```python
number = 3
"I eat {0} apples" . format(number)
'I eat 3 apples '
```

### 2개 이상의 값 넣기

```python
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days." .format(number, day)
'I ate 10 apples. so I was sick for three days.'
```

### 이름으로 넣기

```python
"I ate {number} apples. so I was sick for {day} days." .format(number=10, day=3)
'I ate 10 apples. so I was sick for 3 days'
```

### 인덱스와 이름을 혼용해서 넣기

```python
"I ate {0} apples. so I was sick for {day} days." .format(10, day=3)
'I ate 10 apples. so I was sick for 3 days.'
```

위와 같이 인덱스 항목과 name =value 형태를 혼용하는 것도 가능하다.



### 왼쪽 정렬

```python
"{0:<10}" .format("hi")
'hi       '
```

:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.

### 오른쪽 정렬

```python
"{0:>10}" .format("hi")
'       hi'
```

### 가운데 정렬

```python
"{0:^10}" .format("hi")
'      hi     '
```

:^ 기호를 사용하면 가운데 정렬도 가능하다.

### 공백 채우기

```python
"{0:=^10}" .format("hi")
'====hi===='
"{0:!<10}" .format("hi")
'hi!!!!!!!!'
```

### 소수점 표현하기

```python
y = 3.42134234
"{0:0.4f}" .format(y)
'3.4213'
```

### {또는} 문자 표현하기

```python
"{{ and }}" .format()
'{ and }'
```

format 함수를 사용해 문자열 포매팅을 할 경우 {}와 같은 중괄호 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우에는 위 예의 {{}}처럼 2개를 연속해서 사용하면 된다.



### f 문자열 포매팅

문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다.

```python
name = '홍길동'
age = 30
f '나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'

f'나는 내년이면 {age +1}살이 된다.'
'나는 내년이면 31살이 된다.'
```

딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용할 수 있다.

```python
d = {'name' : '홍길동', 'age':30 }
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
```

### 정렬

```python
f'{"hi":<10}'
'hi           ' <--왼쪽 정렬
f'{"hi":>10}'
'           hi' <== 오른쪽 정렬
f'{"hi":^10}'
'     hi     ' <== 가운데 정렬
```

### 공백 채우기

```python
f'{"hi":=^10}'
'====hi===='
f'{"hi":!<10}'
'hi!!!!!!!!'
```

### 소수점

```python
y = 3.42134234
f'{y:0.4f}'
'3.4213'
f'{y:10.4f}'
'    3.4213'
```

f문자열에서 {}문자를 표시하려면 다음과 같이 두 개를 동시에 사용해야 한다.

```python
f'{{ and }}'
'{ and }'
```

## 문자열 관련 함수

문자열 자료형은 자체적으로 함수를 가지고있다. 이들 함수를 다른 말로 문자열 내장 함수라 한다. 이 내장 함수를 사용하려면 문자열 변수 이름 뒤에 '.'를 붙인 다음에 함수 이름을 써주면 된다. 이제 문자열의 내장 함수에 대해서 알아보자.



### 문자 개수 세기 (count) 

```python
a = "hobby"
a. count('b')
2
```

문자열 중 문자 b의 개수를 돌려준다.

### 위치 알려주기 1(find)

```python
a = "Python is the best choice"
a.find('b')
14 < -- 문자열에서 b가 처음 나온 위치
a.find('k')
-1 
```

문자열 중 문자 b가 처음으로 나온 위치를 반환한다. 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.

### 위치 알려주기 2(index)

```python
a = "Life is too short"
a.index('t')
8
a.index('k')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: substring not found  <--- k가 없기 때문에 오류 발생
```

 문자열 중 문자 t가 맨 처음으로 나온 위치를 반환한다. 만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킨다. 앞의 find 함수와 다른 점은 문자열 안에 존재하지 않는 문자를 찾으면 __오류가 발생__한다는 점이다. 

### 문자열 삽입(Join)

```python
"," .join('abcd')
'a,b,c,d'
```

abcd문자열의 각각의 문자 사이에 ','를 삽입한다.

join함수는 문자열 뿐만 아니라 앞으로 배울 리스트나 튜플도 입력으로 사용할 수 있다. join함수의 입력으로 리스트를 사용하는 예는 다음과 같다.

```python
"," .join(['a','b','c','d'])
'a,b,c,d'
```

### 소문자를 대문자로 바꾸기 (upper)

```python	
a = "hi"
a.upper()
'HI'
```

upper함수는 __소문자를 대문자__로 바꾸어준다. 만약 문자열이 이미 대문자라면 아무 변화도 일어나지 않는다.

### 대문자를 소문자로 바꾸기(lower)

```python
a = "HI"
a.lower()
'hi'
```

lower함수는 대문자를 소문자로 바꾸어 준다.

### 왼쪽 공백 지우기(lstrip)

```python
a = " hi"
a.lstrip()
'hi '
```

문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다. lstrip에서 l은 left를 의미한다.

### 오른쪽 공백 지우기(rstrip)

```python
a = " hi "
a.rstrip()
' hi'
```

문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다. rstrip에서 r는 right를 의미한다.

### 양쪽 공백 지우기(strip)

```python
a = " hi "
a.strip()
'hi'
```

문자열 양쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다.

### 문자열 바꾸기(replace)

```python
a = "Life is too short"
a. replace("Life", "Your leg")
'Your leg is too short'
```

replace(바뀌게 될 문자열, 바꿀 문자열)처럼 사용해서 문자열 안의 특정한 값을 다른 값으로 치환해 준다.

### 문자열 나누기(split)

```python
a = "Life is too short"
a.split()
['Life','is','too','short']
b = "a:b:c:d"
b.split(':')
['a','b','c','d']
```

split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다. 만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다. 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다. ['Life','is','too','short'] 나 ['a','b','c','d']가 리스트이다. 