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





- # 기본적인 명령어

### Git

- **Repository** : 특정 디렉토리를 버전 관리하는 저장소

  - **git init** 명령어로 로컬 저장소 생성
  - 버전관리가 되고 있으면 vs code에서 초록색으로 바뀜
  - 모든 버전에 대한 히스토리가 **.git** 디렉토리에 저장되고 있다는 의미(.~으로 된 폴더는 숨겨져 있음->숨긴 항목 보기)
    - 버전 관리에 대한 모든 것이 들어있음
  - .git 내의 하위 항목까지 모두 버전관리가 되고 있으니 안에 repository를 또 만들면 안됨

- **커밋(commit)한다** = 특정 버전으로 남긴다

  지금 상태를 특정 버전으로 남기고 싶을 때

  - repository 안에 커밋이 쌓이게 됨

  - 3가지 영역을 바탕으로 동작

    - **working directory** : 내가 작업하고 있는 실제 디렉토리 (Racing Ground)

      - untracked 파일 - git으로부터 추적되고있지 않는 파일

        **git add** 명령어로 staging area로 올림

    - **staging area** : 눈에 보이지 않지만(가상공간), 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 잠시 위치하는 공간

      - untracked 파일이 git에 의해 추적되기 시작 -> 버전 관리 시작

      - 이전 버전과 비교하여 변경된 것들이 저장

        **git commit** 명령어로 repository로 올림

    - **repository** : 커밋들이 저장되는 곳 (.git)

  - 코드를 수정하게 되면 working directory에 modified 파일이 되고, git add, git commit을 반복하여 여러 커밋 저장

- **git status** : 현재 git으로 관리되고 있는 파일들의 상태를 알 수 있음

- **git add .** : 추적되지 않은 모든 파일과 추적 하고 있는 파일 중 수정된 파일을 모두 staging area에 올림( **.** : 현재 위치)

- **git commit -m "commit_message"** : 커밋 메세지는 자세하게(어떤 것이 변경됐는지 쓰는 것이 좋음)

- **git config user.name "user_name"** : github 사용자 이름 등록

- **git config user.email "user_email"** : github 사용자 이메일 등록

- **git config --list** : github에 사용자 이름과 이메일이 잘 등록됐나 확인

- **git log** : commit이 사용자 이름과 이메일 앞으로 저장됐나 확인

- commit cc7703e087f74ef6db3a47ed4366244f083d1ddf : 커밋 고유 번호

  - 앞에 네자리만 봐도 서로 구분할 수 있음

- **git log** : git의 commit history 보기

- **git diff** commit_ID1 commit_ID2 : 두 commit 간 차이 보기 (ID1 기준으로 하여 달라진 점)



### Github

- public : 모두 공개, 누구나 가져갈 수 있음, 내 repository는 다른 사람이 수정할 수 없음
- private : 초대한 사람에게만 공개, 내 repository는 다른 사람이 수정할 수 없음
- **git clone {remote_repo}** : github에서 처음 상태만 가져오는 것
- **push** : git(local)에서 변경된 것을 github(remote)에 업데이트
- **pull** : github(remote)에서 변경된 것을 git(local)에 업데이트
  - github에서 수정할 일은 거의 없음
  - code 수정은 git에서 하고 push, pull로 업데이트
- **git remote add origin {remote_repo}**
  - origin : repo name(별명)
  - {remote_repo} : github에서 생성한 repo
- **git push -u origin master** : github에서 만든 새로운 repo를 git으로 
  - origin : repo name
  - master : local branch

- **git push origin master** : local repo의 최신 커밋을 remote repo로 push

