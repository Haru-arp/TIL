# WEB



## HTML(Hyper Text Markup Language)

- HTML 문서의 기본 구조 ( ! + tab ) 
    - html: 문서의 최상위(root)요소
    - head: 문서 메타데이터 요소
        - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
        - 일반적으로 브라우저에 나타나지 않는 내용
    - body: 문서 본문 요소
        - 실제 화면 구성과 관련된 내용

## head 예시

- /<title>/:브라우저 상단 타이틀
- /<meta>/: 문서 레벨 메타데이터 요소
- /<link>/: 외부 리소스 연결요소
- /<script>/ : 스크립트 요소 (javascript 파일/ 코드)
- /<style> /: CSS직접 작성

## DOM트리

- 텍스트 파일인 HTML문서를 브라우저에서 렌더링 하기 위한 구조
    - HTML 문서에 대한 모델을 구성함
    - HTML 문서 내의 각 요소에 접근/ 수정에 필요한 프로퍼티와 메서드를 제공함

## 주요 태그와 속성

- 내용이 없는 태그들
    - br, hr, img, input, link, meta
- 요소는 중첩될 수 있음.

- 속성:
    - 속성을 통해 태그의 부가적인 정보를 설정할 수 있음.
    - 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공.
    - 요소의 시작 태그에 작성하며 보통 이름과 같이 하나의 쌍으로 존재
    - 태그와 상관없이 사용 가능한 속성들도 있음.

## HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇몇 요소에는 아무 효과가 없을 수 있음.)
    - id: 문서 전체에서 유일한 고유 식별자 지정
    - class : 공백으로 구분된 해당 요소의 클래스의 목록(CSS,JS에서 요소를 선택하거나 접근)
    - data-*: 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
    - style: inline 스타일
    - title: 요소에 대한 추가 정보 지정
    - tabindex: 요소의 탭 순서



## 시멘틱 태그

- HTML5에서 의미론적 요소를 담은 태그의 등장
    - 기존 영역을 의미하는 div태그를 대체하여 사용
- 대표적인 태그 목록
    - header: 문서 전체나 섹션의 헤더(머리말 부분)
    - nav: 네비게이션
    - aside: 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    - section: 문서의 일반적인 구분. 컨텐츠의 그룹을 표현
    - article: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - footer: 문서 전체나 섹션의 푸터(마지막 부분)
- Non semantic 요소는 div, span 등이 있으며, h1, table 태그들도 시멘틱 태그로 볼 수 있음
- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미있는 정보의 그룹을 태그로 표현.
- 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함.
- 검색엔진 최적화(SEO)를 위해서 메타태그, 시멘틱 태그 등을 통한 마크업을 효과적으로 활용 해야 함

## 태그

### 텍스트 요소

- <a></a> : href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
- <b></b><strong></strong>: 굵은 글씨 요소 중요한 강조하고자 하는 요소(보통 굵은 글씨로 표현)
- <i></i><em></em>:기울임 글씨 요소, 중요한 강조하고자 하는 요소(보통 기울임 글씨로 표현)
- /<br>/:텍스트 내의 줄 바꿈 생성
- <img>: src 속성을 활용하여 이미지 표현
- <span></span>: 의미없는 인라인 컨테이너

### 그룹 컨텐츠

- /<p></p>/:하나의 문단 (paragraph)
- /<hr>/ : 문단 레벨 요소에서의 주제의 분리를 의미하며, 수평선으로 표현됨.(A horizontal Rule)
- /<ol></ol><ul></ul><li></li>/: 순서가 있는 리스트 (ordered), 순서가 없는 리스트(unordered)
- /<pre></pre>/: HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백 문자를 유지
- /<blockquote></blockquote>/: 텍스트가 긴 인용문 주로 들여쓰기를 한 것으로 표현됨.
- /<div></div>/: 의미 없는 블록 레벨 컨테이너 

# CSS(Cascading Style Sheets)

- 스타일을 지정하기 위한 언어! 선택하고, 스타일을 지정한다.
- css구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택.
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속서에 부여할 값을 의미.
    - 속성(Property): 어떤 스타일 기능을 변경할지 결정
    - 값(value): 어떻게 스타일 기능을 변경할지 결정

## CSS 정의 방법

- 인라인(inline)
- 내부 참조(embedding)-<style>
- 외부 참조(link file) - 분리된 CSS파일

## Q5.  CSS 우선순위

```
1. !important
2. Inline Style
3. id 선택자.
4. class 선택자
5. 요소 선택자
6. 소스 순서
```



## 선택자(Selector) 유형

- 기본 선택자 
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자.\
    
- 결합자(Combinators)
    - 자손 결합자, 자식 결합자(:첫 번째 요소의 바로 아래 자식인 노드를 선택 >)
    - 일반 형제 결합자(A~B ~결합자는 형제, 즉 첫 번째 요소를 뒤따르면서, 같은 부모를 공유하는 두 번째 요소를 선택합니다.), 
        인접 형제 결합자(+, +결합자는 인접 형제, 즉 첫 번째 요소의 바로 뒤에 위치하면서 같은 부모를 공유하는 두 번째 요소를 선택합니다.)
    
- 의사 클래스/요소(Pseudo Class) ( 의사 : 는 문서트리가 포함하지 않는 상태 정보에 기반해 요소를 선택할 수 있습니다.), (의사 :: 는 html이 포함하지 않는 개체를 선택합니다. ) https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Selectors
    - 링크, 동적 의사 클래스 : (:link, :visited, :hover, :active, :focus)
    
        - link: 링크의 기본 상태이며, 사용자가 아직 한 번도 이 링크를 통해 연결된 페이지를 방문하지 않은 상태
        - visited: 사용자가 한 번이라도 이 링크를 통해 연결된 페이지를 방문한 상태입니다.
        - hover: 사용자의 마우스 커서가 링크 위에 올라가 있는 상태입니다.
        - active: 사용자가 마우스로 링크를 클릭하고 있는 상태입니다.
        - focus: 키보드나 마우스의 이벤트(event) 또는 다른 형태로 해당 요소가 포커스(focus)를 가지고 있는 상태입니다.
        - :hover는 반드시 :link와 :visited가 먼저 정의된 후에 정의되어야 정상적으로 동작합니다.
        - :active는 반드시 :hover가 먼저 정의된 후에 정의되어야 정상적으로 동작합니다.
    
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자 ( http://www.tcpschool.com/css/css_selector_pseudoClass )
    
        - 구조적 의사 클래스
    
            - : first-child : :first-child는 모든 자식(child) 요소 중에서 맨 앞에 위치하는 자식(child) 요소를 모두 선택합니다.
            - : last-child : :last-child는 모든 자식(child) 요소 중에서 맨 마지막에 위치하는 자식(child) 요소를 모두 선택합니다.
            - : nth-child : nth-child는 모든 자식(child) 요소 중에서 앞에서부터 n번째에 위치하는 자식(child) 요소를 모두 선택합니다.
            - : nth-last-child : nth-last-child는 모든 자식(child) 요소 중에서 뒤에서부터 n번째에 위치하는 자식(child) 요소를 모두 선택합니다.
            - : first-of-type : :first-of-type는 모든 자식(child) 요소 중에서 맨 처음으로 등장하는 특정 타입의 요소를 모두 선택합니다.
            - : last-of-type : :last-of-type는 모든 자식(child) 요소 중에서 맨 마지막으로 등장하는 특정 타입의 요소를 모두 선택합니다.
            - : nth-of-type : :nth-of-type는 모든 자식(child) 요소 중에서 n번째로 등장하는 특정 타입의 요소를 모두 선택합니다.
            - : nth-last-of-type : :nth-last-of-type는 모든 자식(child) 요소 중에서 뒤에서부터 n번째로 등장하는 특정 타입의 요소를 모두 선택합니다.
            - :only-child :   :only-child는 자식(child) 요소를 단 하나만 가지는 요소의 자식(child) 요소를 모두 선택합니다.
            - :only-of-type :  :only-of-type는 자식(child) 요소로 특정 타입의 요소 단 하나만을 가지는 요소의 자식(child) 요소를 모두 선택합니다.
            - :empty: :empty는 자식(child) 요소를 전혀 가지고 있지 않은 요소를 모두 선택합니다.
            - :root : :root는 해당 문서의 root 요소를 선택합니다.
    
        - 기타 의사 클래스 (http://www.tcpschool.com/css/css_selector_etc)
    
            - :not :  :not 선택자는 모든 선택자와 함께 사용할 수 있으며, 해당 선택자를 반대로 적용하여 선택합니다.
    
            - :lang : 
    
            - :lang 선택자는 특정 HTML 요소를 사용자 컴퓨터의 언어 설정에 따라 다르게 표현할 때 사용합니다.
    
                예를 들면, 영어에서는 인용의 표현으로 따옴표("")를 사용하나, 프랑스어에서는 부등호(<>)를 사용합니다.
    
                이렇게 언어에 따라 달라지는 태그의 모양을 사용자 컴퓨터의 언어 설정에 따라 다르게 표현할 수 있게 해줍니다.
    
        - 의사 엘리먼트: (http://www.tcpschool.com/css/css_selector_pseudoElement)
    
            - 의사 요소(pseudo-element)는 해당 HTML 요소의 특정 부분만을 선택할 때 사용합니다.
    
            - 선택자::의사요소이름 {속성: 속성값;}
    
            - ::first-letter:   
    
                ```
                이 의사 요소(pseudo-element)는 텍스트의 첫 글자만을 선택합니다.
                단, 블록(block) 타입의 요소에만 사용할 수 있습니다.
                이 의사 요소를 통해 사용할 수 있는 속성은 다음과 같습니다.
                \- font 속성
                \- color 속성 
                \- background 속성
                \- margin 속성
                \- padding 속성
                \- border 속성
                \- text-decoration 속성
                \- text-transform 속성
                \- line-height 속성
                \- float 속성
                \- clear 속성
                \- vertical-align 속성 (단, float 속성값이 none일 경우에만)
                ```
    
            - ::first-line
    
            - ```
                이 의사 요소는 텍스트의 첫 라인만을 선택합니다.
                단, 블록(block) 타입의 요소에만 사용할 수 있습니다.
                
                이 의사 요소를 통해 사용할 수 있는 속성은 다음과 같습니다.
                
                - font 속성
                - color 속성 
                - background 속성
                
                - word-spacing 속성
                - letter-spacing 속성
                - text-decoration 속성
                - text-transform 속성
                - line-height 속성
                - clear 속성
                - vertical-align 속성
                ```
    
            - ::before
    
            - ``` 
                이 의사 요소는 특정 요소의 내용(content) 부분 바로 앞에 다른 요소를 삽입할 때 사용합니다.
                ```
    
            - ::after 
    
            - ```
                이 의사 요소는 특정 요소의 내용(content) 부분 바로 뒤에 다른 요소를 삽입할 때 사용합니다.
                ```
    
            - ::selection
    
            - ```
                이 의사 요소는 해당 요소에서 사용자가 선택한 부분만을 선택할 때 사용합니다.
                ```
    
            - 의사 엘리먼트의 동시 적용: 하나의 HTML 요소에 여러 개의 의사 요소를 동시에 적용할 수 있습니다. 
    
        - 속성 선택자 : (http://www.tcpschool.com/css/css_selector_attribute)
    
            - 속성 선택자를 사용하면 특정 속성이나 특정 속성값을 가지고 있는 HTML 요소를 선택할 수 있습니다.
    
            - \- [속성이름] 선택자 :  [속성이름] 선택자는 특정 속성을 가지고 있는 요소를 모두 선택합니다.
    
                \- [속성이름="속성값"] 선택자 : [속성이름="속성값"] 선택자는 특정 속성을 가지고 있으며, 해당 속성의 속성값까지 일치하는 요소를 모두 선택합니다.
    
            - 문자열 속성 선택자 :
    
                - \- [속성이름~="속성값"] 선택자 : [속성이름~="속성값"] 선택자는 특정 속성의 속성값에 특정 문자열로 이루어진 하나의 단어를 포함하는 요소를 모두 선택합니다.
    
                    
    
                - \- [속성이름|="속성값"] 선택자 :  [속성이름|="속성값"] 선택자는 특정 속성의 속성값이 특정 문자열로 이루어진 하나의 단어로 시작하는 요소를 모두 선택합니다.
    
                    
    
                - \- [속성이름^="속성값"] 선택자:  [속성이름^="속성값"] 선택자는 특정 속성의 속성값이 특정 문자열로 시작하는 요소를 모두 선택합니다.
    
                    
    
                - \- [속성이름$="속성값"] 선택자:  [속성이름$="속성값"] 선택자는 특정 속성의 속성값이 특정 문자열로 끝나는 요소를 모두 선택합니다.
    
                    
    
                - \- [속성이름*="속성값"] 선택자 : [속성이름*="속성값"] 선택자는 특정 속성의 속성값에 특정 문자열를 포함하는 요소를 모두 선택합니다.
    
                     

## CSS 선택자 정리

- 요소 선택자
    - HTML 태그를 직접 선택
- 클래스(class) 선택자
    - 마침표(.) 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자 
    - #문자로 시작하며, 해당 아이디가 적용된 항목을 선택
    - 일반적으로 하나의 문서에 1번만 사용. 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장.

## CSS 적용 우선순위(cascading order)

- CSS 우선 순위를 아래와 같이 그룹을 지어볼 수 있다.

- Q5.  CSS 우선순위
  
    ```
    1. !important
    2. Inline Style
    3. id 선택자.
    4. class 선택자
    5. 요소 선택자
    6. 소스 순서
    ```
    
    - 1. 중요도(Importance) - 사용시 주의
            - !important
        2.  우선순위 (Specificity)
            - 인라인> id >class, 속성, pseude-class > 요소, pseudo - element
        3. CSS 파일 로딩 순서

## CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다. 
    - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
    - 상속 되는 것 예시
        - ex) Text 관련 요소 (font, color, text-align), opacity, visibility 등
    - 상속 되지 않는 것 예시
        - ex) Box model 관련 요소 (width, height, margin, padding, border, box-sizing, display), position관련 요소(position, top/right/bottom/left z-index)등

## 크기 단위

- px(픽셀)
    - 모니터 해상도의 한 화소인 "픽셀" 기준
    - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
- em
    - (바로 위, 부모요소에 대한)상속의 영향을 받음
    - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가장
- rem
    - (바로 위, 부모 요소에 대한)상속의 영향을 받지 않음
    - 최상위 요소(.html)의 사이즈를 기준으로 배수 단위를 가짐
- viewpoint
    - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
    - 디바이스의 viewpoint를 기준으로 상대적인 사이즈가 결정됨
    - vw, vh, vmin, vmax

## 색상 단위

- 색상 키워드
    - 대소문자를 구분하지 않음
    - red, blue, black 과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상
    - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식 
        - '#' + 16진수 표기법
        - rgb()함수형 표기법
- HSL 색상
    - 색상. 채도. 명도를 통해 특정 색을 표현하는 방식.
- a 는 alpha(투명도)

## 결합자 (Combinators)

- 자손 결합자
    - selectorA하위의 모든 selectorB요소
- 자식 결합자
    - selectorA바로 아래의 selectorB요소
- 일반 형제 결합자 (~)
    - selectorA의 형제 요소 중 뒤에 위치하는 selectorB요소를 모두 선택
- 인접 형제 결합자 (>)
    - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB요소를 선택

## Box model 

- 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치)

- 모든 HTML 요소는 box 형태로 되어있음

- 하나의 박스는 네 부분(영역)으로 이루어짐

    - content : 글이나 이미지 등 요소의 실제 내용

    - padding : 테두리 안쪽의 내부 여백, 요소에 적용된 배경색, 이미지는 padding까지 적용

    - border : 테두리 영역

    - margin : 테두리 바깥의 외부 여백, 배경색을 지정할 수 없다. 

        margin 숏핸드: margin __ : 상하좌우 margin __ __ : 상하, 좌우 , margin __ __ __ : 상 좌우 하

        margin __ __ __ __ : 상우하좌

## 인라인, 블록 요소 각각의 특징들

- display: block 
    - 줄 바꿈이 일어나는 요소 
    - 화면 크기 전체의 가로 폭을 차지한다.
    - 블록 요소 안에 인라인 레벨 요소가 들어갈 수 있음. 
- display: inline
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - content 너비만큼 가로 폭을 차지한다.
    - width, height, margin-top, margin-bottom을 지정할 수 없다.
    - 상하 여백은 line-height로 지정한다. 

## 블록 레벨 요소와 인라인 레벨 요소

- 블록 레벨 요소와 인라인 레벨 요소 구분(HTML 4.1까지)
- 대표적인 블록 레벨 요소
    - div / ul , ol, li /p / hr/ form 등 
- 대표적인 인라인 레벨 요소
    - span /a / img / input, label / b, em ,i ,strong 등 
- 속성에 따른 수평 정렬:
    - margin-right:auto; 좌측정렬
    - text-align:left: 좌측정렬
    - margin-left:auto; 우측 정렬
    - text-align: right: 우측 정렬
    - margin-right: auto, margin-left:auto; 가운데 정렬
    - text-align: center 가운데 정렬


## display

- display: inline-block	
    - block과 inline레벨 요소의 특징을 모두 가짐
    - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin속성을 모두 지정할 수 있음.
- display: none
    - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
    - 이와 비슷한 visibility:hidden은 해당 요소가 공간은 차지하나, 화면에 표시만 하지 않는다.

## CSS position

- 문서 상에서 요소를 위치를 지정
- static : 모든 태그의 기본 값 (기준 위치)
    - 일반적인 요소의 배치 순서에 따름(좌측 상단)
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티 (top, bottom, left, right)를 사용하여 이동 가능
    - relative : 상대 위치
        - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
        - 레이아웃에서 요소가 차지하는 공간은 static 일 때와 같음 (normal position 대비 offset)
    - absolute : 절대 위치
        - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
        - static이 아닌 가장 가까이 있는 부모/ 조상 요소를 기준으로 이동 (없는 경우 body) 
    - fixed : 고정 위치
        - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
        - 부모 요소와 관계없이 viewport를 기준으로 이동
            - 스크롤 시에도 항상 같은 곳에 위치함

CSS 원칙

- CSS 원칙 1,2: Normal flow
    - 모든 요소는 네모 (박스모델), 좌측상단에 배치
    - display에 따라 크기와 배치가 달라짐
- CSS원칙 3
    - position으로 위치의 기준을 변경
        - relative: 본인의 원래 위치
        - absolute: 특정 부모의 위치
        - fixed: 화면의 위치

## CSS Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
    - main axis(메인 축)
    - cross axis(교차 축)
- 구성 요소
    - Flex Container(부모 요소)
        - Flexbox 레이아웃을 형성하는 가장 기본적인 모델
        - Flex Item 들이 놓여있는 영역
        - display 속성을 flex, 혹은 inline-flex로 지정
    - Flex Item(자식 요소)
        - 컨테이너에 속해있는 컨텐츠(박스)

- 왜 Flex box를 사용해야 하는가
    - 1. 수직정렬이 용이하다
        2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치한다

## Flex 속성

- 배치 설정

    - Flex- direction : Main axis 기준 방향 설정
        - 역방향의 경우 HTML태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)
        - row, row-reverse, column, column-reverse
    - flex-wrap: 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정, 즉 기본적으로 컨테이너 영역을 벗어나지 않도록 함
        - nowrap(기본값): 한줄에 배치
        - wrap: 넘치면 그 다음 줄로 배치
    - flex-flow: flex-direction과 flex-wrap의 shorthand!
    - 차례로 작성

- 공간 나누기

    - justify-content(main-axis)
        - flex-start
        - flex-end
        - center
        - space-between
        - space-around
        - space-evenly
    - align-content(cross axis)
        - flex-start
        - flex-end
        - center
        - space-between
        - space-around
        - space-evenly

- 정렬

    - align-items(모든 아이템을 cross axis기준으로)

        

    - align-self(개별 아이템)

        - ###### 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용

- 기타 속성

    - flex- grow: 남은 영역을 아이템에 분배 (https://blogpack.tistory.com/863)
    - order :배치 순서
    
    https://heropy.blog/2018/11/24/css-flexible-box/ 확인

```css
Flex Item을 위한 속성들

- order - Item의 순서를 설정
- flex - flex-grow , flex-shrink , flex-basis 에 대한 단축 속성!
- flex-grow - Item의 너비 증가(grow) 비율 설정
- flex-shrink - Item의 너비 감소(shrink) 비율 설정
- flex-basis - Item의 기본 너비 설정
```

```css
Flex Container 속성들

- display - Flex Container를 정의
- flex-flow - flex-direction 과 flex-wrap 을 줄여서 쓸 수 있음
- flex-direction - item들의 주 축(main-axis) 설정
- flex-wrap - item들의 줄 바꿈 설정
- justify-content - 주 축(main-axis)의 정렬  방법 설정
- align-content - 교차 축(cross-axis)의 정렬 방법 설정 (2줄 이상)
- align-items - 교차 축(cross-axis)의 정렬 방법 설정 (1줄)
```



<hr>



# BootStrap


```css
mt-1 = .mt-1{
    margin-top: 0.25rem !important;
}
<!---mt-1--->: margin-top , 1rem = 16px 고로 0.25 * 16 = 4px ( 0.25 rem = 4px )
html의 root 글꼴 크기는 16px

m-1 0.25rem 4px
m-2 0.5rem 8px
m-3 1rem 16px
m-4 1.5rem 24px
m-5 3rem 48px

.mx-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
}

.mx-auto { 수평 중앙 정렬
    margin-right: auto !important;
    margin-left: auto !important;
}

.py-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}
spacing 종합
m : margin                        0  0rem   0px               
p : padding                        1  0.25rem   4px
t : top                            2  0.5rem   8px
b : bottom                        3  1rem   16px
s : left                        4  1.5rem   24px
e : right                        5  3rem   48px
x : left, right
y : top, bottom
```

```css
color                                    #000000 : 검정색
primary : 파란색                  #ffffff : 흰색             
secondary: 회색                  rgba(255, 0 , 0) : 빨간색
success: 초록색                  rgba(0, 255 , 0) : 초록색
info : 청색                     rgba(0, 0 , 255) : 파란색
warning: 노란색
danger: 빨간색
light: 하얀색
dark: 검정색
```



# Grid System( web design )

- 요소들의 디자인과 배치에 도움을 주는 시스템

- 기본 요소
    - Column: 실제 컨텐츠를 포함하는 부분
    - Gutter : 칼럼과 칼럼 사이의 공간 ( 사이 간격 )
    - Container : Column들을 담고 있는 공간



- Bootstrap Grid system은 flexbox로 제작됨
- container, rows, column으로 컨텐츠를 배치하고 정렬
- 반드시 기억해야 할 2가지!
    - 1. 12개의 column
        2. 6개의 grid breakpoint (xs, sm, md, lg, xl ,xxl)
