# Haru's TIL (Today I Learned)



# Git 시작하기

- 검색 - cmd

- 명령어를 이용하여 컴퓨터에게 일을 시키는 것을 CLI 라고 한다. <-> GUI (Graphic User Interface)

  ##  PowerShell

  일부 Unix/ Linux 명령어 사용 가능

 ### 간단한 Unix/ Linux 명령어

1. 현재 위치의 폴더, 파일 목록보기 = **ls**
2. 현재 위치를 이동하는 명령어 = **cd\<path>** 
   - **cd..** = 상위폴더로 이동.
3. 폴더 생성하기 **mkdir \<name>**
4. **~(물결표)** = home
5. 파일 만들기 = **touch \<name>** 
6. 파일 지우기 = **rm \<name> ** 
7. 폴더 지우기 = **rm -r \<name>** 

# Git  기본기

Repository = 특정 디렉토리를 버전 관리하는 저장소



git init 명령어로 로컬 저장소를 생성합니다..

.git 디렉토리에 버전 관리에 필요한 모든 것이 들어있다.

--> 특정 버전으로 남긴다! ="커밋(Commit)"한다. 3가지 영역을 바탕으로 동작.

## 커밋

1. Working Directory

   - 내가 작업하고 있는 실제 디렉토리

2. Staging Area

   - 커밋(Commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳

3. Repository

   - 커밋(Commit)들이 저장되는 곳

   ### git status 

   : 현재 git으로 .....

   ### git add .

   추적되지 않은 모든 파일과 추적 하고 있는 파일 중 수정 된 파일을 모두 Staging Area에 올려요

​		git add .의 .은 현재 위치라고 알려진다.

# 드디어 Commit을!

git commit -m "Commit_message" : 커밋 입력하는 코드 



## git log, git diff	



