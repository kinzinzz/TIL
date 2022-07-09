# Git 수업

> 지속적으로 업데이트 중입니다.



## 1. Git 기초 명령어

- ` $ git init ` : 로컬 저장소 생성 
- ` $ git add 파일명` : 2통 
- ` $ git commit -m '커밋 메세지' ` : 커밋
- `$ git status `: 상태확인 
- `$ git log` : 버전확인  
- ` $ git push` : 원격 저장소에 보내기  
- ` $ git pull `: 원격 저장소로부터 받기 
- ` $git remote add origin http://github.com/유저네임/저장소이름.git ` : 로컬 저장소에는 한번만 설정 해주면 되고 원격 저장소 정보를 로컬 저장소에 추가.
- ` $git add origin master `>> 인증(처음한번만)
- ` $git remote -v `  : 원격 저장소의 정보를 확인
- ` $ git push origin master ` : 커밋한 내용을 원격저장소로 보낸다.
- ` $git pull origin master ` : 다른 컴퓨터에서 작업할 때 로컬 저장소로 파일을 가져온다.
- ` $git config user.name kinzinzz` : 사용자 이름 
- ` $git config user.email kinzinzz@naver.com` :  사용자 메일



## 2. 로컬 저장소

- 로컬 저장소(Local Repository): 내 PC에 파일이 저장되는 개인 전용 저장소.

  

  

## 3. 원격 저장소

- Git, GitHub 은 버전을 관리하고 <u><b>commit</b></u>한 내용만 기록된다.

- 이용하는 방법

  > init >> add >> commit >> ` $git push <원격저장소이름> <브랜치이름> ` 

- 이용시 참고 사항
  - Git은 파일 관리가 아니라 <u><b>버전관리</b></u>(commit이 없으면 push도 안된다.)
  - Everything up-to-date(모두 업데이트 되어있다) : 새로운 commit 없다.
  - u를 적어주면 앞으로 현재 브랜치를 자동으로 origin이라는 저장소에 master 브랜치로 연결해서 간단해게 git push만 입력해도 자동으로 연결된다.
  - push 실패 : 로컬과 원격 저장소의 커밋 이력이 다른 경우 발생한다.(pull 이용한다.)
  - 버전관리가 필요없는 파일 : `  .gitignore `  /**<u>커밋하기전에 미리</u>** .gitignore을 해야한다.



## 4. merge conflict(non fast-forward 병합)

- merge conflict 발생이유
  - 'conflict' 이라 나오는 것을 보니 자동 병합에 실패한 것.
  - 각각의 브랜치에서 같은 행에 포함되어 있기 때문이다.
- 해결방법
  - 충돌이 있는 부분에 Git 이 자동으로 정보를 포함하여 파일 내용을 변경한다.
  - 어떤 브랜치에서 어떤 부분이 충돌되었는지 확인할 수 있다.
  - 충돌이 일어난 부분은 일일 확인해서 수정한다.