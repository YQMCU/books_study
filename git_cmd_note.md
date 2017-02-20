Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

D:\Documents and Settings\study_practise\book_study>git init
Initialized empty Git repository in D:/Documents and Settings/study_practise/boo
k_study/.git/

D:\Documents and Settings\study_practise\book_study>git clone https://github.com
/YQMCU/books_study.git
Cloning into 'books_study'...
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.

D:\Documents and Settings\study_practise\book_study>cd ..

D:\Documents and Settings\study_practise>git clone https://github.com/YQMCU/book
s_study.git
Cloning into 'books_study'...
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.

D:\Documents and Settings\study_practise>git status
fatal: Not a git repository (or any of the parent directories): .git

D:\Documents and Settings\study_practise>cd books_study

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        01-flask_web_development/

nothing added to commit but untracked files present (use "git add" to track)

D:\Documents and Settings\study_practise\books_study>git add .

D:\Documents and Settings\study_practise\books_study>git commit -m "flask web de
velopment by Python"
[master 6bdf781] flask web development by Python
 1 file changed, 14 insertions(+)
 create mode 100644 01-flask_web_development/note.md

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 646 bytes | 0 bytes/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To https://github.com/YQMCU/books_study.git
   e99f352..6bdf781  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean

D:\Documents and Settings\study_practise\books_study>dir
 驱动器 D 中的卷是 本地磁盘(D:)
 卷的序列号是 D2CF-7AD4

 D:\Documents and Settings\study_practise\books_study 的目录

2017-02-21  01:47    <DIR>          .
2017-02-21  01:47    <DIR>          ..
2017-02-21  01:47    <DIR>          01-flask_web_development
2017-02-21  01:46                13 README.md
               1 个文件             13 字节
               3 个目录 70,672,515,072 可用字节

D:\Documents and Settings\study_practise\books_study>tree .
卷 本地磁盘(D:) 的文件夹 PATH 列表
卷序列号为 D2CF-7AD4
D:\DOCUMENTS AND SETTINGS\STUDY_PRACTISE\BOOKS_STUDY
└─01-flask_web_development

D:\Documents and Settings\study_practise\books_study>tree . /s
无效的开关 - /s

D:\Documents and Settings\study_practise\books_study>tree /?
以图形显示驱动器或路径的文件夹结构。

TREE [drive:][path] [/F] [/A]

   /F   显示每个文件夹中文件的名称。
   /A   使用 ASCII 字符，而不使用扩展字符。


D:\Documents and Settings\study_practise\books_study>tree .  /f
卷 本地磁盘(D:) 的文件夹 PATH 列表
卷序列号为 D2CF-7AD4
D:\DOCUMENTS AND SETTINGS\STUDY_PRACTISE\BOOKS_STUDY
│  README.md
│
└─01-flask_web_development
        note.md


D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   01-flask_web_development/note.md

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add .

D:\Documents and Settings\study_practise\books_study>git commit -m "引入strapdow
njs for convert md_to_html without server side but client side"
[master fafc09a] 引入strapdownjs for convert md_to_html without server side but
client side
 1 file changed, 11 insertions(+), 2 deletions(-)

Warning: Your console font probably doesn't support Unicode. If you experience s
trange characters in the output, consider switching to a TrueType font such as C
onsolas!

D:\Documents and Settings\study_practise\books_study>git commit -m "modify:use s
trapdown.js for convert md_to_html without server side but client side"
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working tree clean

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 606 bytes | 0 bytes/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   6bdf781..fafc09a  master -> master

D:\Documents and Settings\study_practise\books_study>git add .

D:\Documents and Settings\study_practise\books_study>git commit -m "add : git_cm
d_note.md to note the git commands for reviewing"
[master 2f82da6] add : git_cmd_note.md to note the git commands for reviewing
 1 file changed, 144 insertions(+)
 create mode 100644 git_cmd_note.md

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.98 KiB | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/YQMCU/books_study.git
   fafc09a..2f82da6  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   git_cmd_note.md

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add .

D:\Documents and Settings\study_practise\books_study>git commit -m "Modify : mod
ify the 01-flask_web_development/note.md to be note.html"
[master 0dc90a0] Modify : modify the 01-flask_web_development/note.md to be note
.html
 2 files changed, 26 insertions(+), 1 deletion(-)
 rename 01-flask_web_development/{note.md => note.html} (100%)

D:\Documents and Settings\study_practise\books_study>git commit -m "Modify : ren
ame 01-flask_web_development/{note.md => note.html "
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working tree clean

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 647 bytes | 0 bytes/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   2f82da6..0dc90a0  master -> master

D:\Documents and Settings\study_practise\books_study>git add .

D:\Documents and Settings\study_practise\books_study>git commit -m "Modify:set 0
1-flask_web_development/{note.html} charset=utf8"
[master 9f8e540] Modify:set 01-flask_web_development/{note.html} charset=utf8
 2 files changed, 28 insertions(+), 2 deletions(-)

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 731 bytes | 0 bytes/s, done.
Total 5 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/YQMCU/books_study.git
   0dc90a0..9f8e540  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   git_cmd_note.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        scripts/

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add ./scripts
warning: LF will be replaced by CRLF in scripts/strapdown.js.
The file will have its original line endings in your working directory.

D:\Documents and Settings\study_practise\books_study>git add ./scripts/

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:add a sc
ript file into scripts/strapdown.js"
[master a544b72] Add:add a script file into scripts/strapdown.js
 1 file changed, 442 insertions(+)
 create mode 100644 scripts/strapdown.js

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 13.71 KiB | 0 bytes/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   9f8e540..a544b72  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   01-flask_web_development/note.html
        modified:   git_cmd_note.md

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add ./01-flask_web_deve
lopment/note.html

D:\Documents and Settings\study_practise\books_study>git  commit -m "Modify:modi
fy the script src"
[master 8c0b301] Modify:modify the script src
 1 file changed, 2 insertions(+), 1 deletion(-)

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   git_cmd_note.md

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add ./git_cmd_note.md

D:\Documents and Settings\study_practise\books_study>git commit -m "Modify:updat
e command"
[master fbb7274] Modify:update command
 1 file changed, 87 insertions(+)

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 7, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (7/7), 1.26 KiB | 0 bytes/s, done.
Total 7 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
To https://github.com/YQMCU/books_study.git
   a544b72..fbb7274  master -> master


D:\Documents and Settings\study_practise\books_study>git add ./update.bat

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:add upda
te.bat to excute bat to update git_cmd_note.md"
[master 0a73932] Add:add update.bat to excute bat to update git_cmd_note.md
 1 file changed, 4 insertions(+)
 create mode 100644 update.bat

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 370 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   fbb7274..0a73932  master -> master

