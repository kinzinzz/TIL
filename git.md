# Git Status

## a.txt 파일을 만든 직후

> 빨간 글씨 => 1통

```bash
$ git status
On branch master

# 트래킹이 되고 있지 않은 파일?
# => 1통 (working girectory)
# => 한번도 git으로 관리되고 있지 않은 파일! 
Untracked files:
# git add 사용해봐
# 포함시키기 위해서 /커밋이 될 것 =>2통에 넣으려면
  (use "git add <file>..." to include in what will be committed)
        a.txt
# 커밋할 것은 없어 ==> 2통이 비어있어
# 하지만(but) 트래킹되지 않은 파일은 존재한다.
#(git add 사용해서 트래킹해)
nothing added to commit but untracked files present (use "git add" to track)
```

## b.txt 파일을 만들고 add 한 이후

```bash
$ git status
On branch master
# (커밋될) 변경사항들 => 2통
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        # 새로운 파일 : b.txt
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt
```

- ## (master) 있는 곳에는 git init을 하지 않는다.

- ## git 명령어를 입력할 때에는 <u>항상</u> 경로를 잘 보자

- ## 명령어의 결과 영어를 잘 읽자.

