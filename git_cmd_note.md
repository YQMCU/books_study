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

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        scripts/strapdown.css
        scripts/themes/

nothing added to commit but untracked files present (use "git add" to track)

D:\Documents and Settings\study_practise\books_study>git add ./scripts/strapdown
.css ./scripts/themes/
warning: LF will be replaced by CRLF in scripts/strapdown.css.
The file will have its original line endings in your working directory.
warning: LF will be replaced by CRLF in scripts/themes/bootstrap-responsive.min.
css.
The file will have its original line endings in your working directory.
warning: LF will be replaced by CRLF in scripts/themes/united.min.css.
The file will have its original line endings in your working directory.

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:add scri
pts/ strapdown.js's stylesheets"
[master 72fe804] Add:add scripts/ strapdown.js's stylesheets
 3 files changed, 953 insertions(+)
 create mode 100644 scripts/strapdown.css
 create mode 100644 scripts/themes/bootstrap-responsive.min.css
 create mode 100644 scripts/themes/united.min.css

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 7, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 21.09 KiB | 0 bytes/s, done.
Total 7 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   8fbc8f5..72fe804  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   01-flask_web_development/note.html

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add ./01-flask_web_deve
lopment/note.html

D:\Documents and Settings\study_practise\books_study>git commit -m "Modify:edit
chapter01 preface"
[master 8fb9905] Modify:edit chapter01 preface
 1 file changed, 22 insertions(+)

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 1.34 KiB | 0 bytes/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   b6801db..8fb9905  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/
        note_template.html
        scripts/markdown_parse.js
        scripts/themes/fonts/
        scripts/themes/google_font_ubuntu.css

nothing added to commit but untracked files present (use "git add" to track)

D:\Documents and Settings\study_practise\books_study>git add scripts/themes/goog
le_font_ubuntu.css
warning: LF will be replaced by CRLF in scripts/themes/google_font_ubuntu.css.
The file will have its original line endings in your working directory.

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:add impo
rt static stylesheet file google_font_ubuntu.css"
[master 626b34a] Add:add import static stylesheet file google_font_ubuntu.css
 1 file changed, 48 insertions(+)
 create mode 100644 scripts/themes/google_font_ubuntu.css

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 967 bytes | 0 bytes/s, done.
Total 5 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/YQMCU/books_study.git
   ae23448..626b34a  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/
        note_template.html
        scripts/markdown_parse.js
        scripts/themes/fonts/

nothing added to commit but untracked files present (use "git add" to track)

D:\Documents and Settings\study_practise\books_study>dir 02-web_scraping_with_Py
thon
 驱动器 D 中的卷是 本地磁盘(D:)
 卷的序列号是 D2CF-7AD4

 D:\Documents and Settings\study_practise\books_study\02-web_scraping_with_Pytho
n 的目录

2017-02-23  12:43    <DIR>          .
2017-02-23  12:43    <DIR>          ..
2017-02-23  01:25    <DIR>          codes
2017-02-23  12:33            11,025 note.html
2017-02-23  12:42            11,226 test.html
               2 个文件         22,251 字节
               3 个目录 62,169,280,512 可用字节

D:\Documents and Settings\study_practise\books_study>git add scripts/themes/font
s/

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:add stat
ic woff  ubuntu fonts"
[master f556673] Add:add static woff  ubuntu fonts
 6 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 scripts/themes/fonts/ODszJI8YqNw8V2xPulzjO_esZW2xOQ-xsNqO47m
55DA.woff2
 create mode 100644 scripts/themes/fonts/WkvQmvwsfw_KKeau9SlQ2_esZW2xOQ-xsNqO47m
55DA.woff2
 create mode 100644 scripts/themes/fonts/Wu5Iuha-XnKDBvqRwQzAG_esZW2xOQ-xsNqO47m
55DA.woff2
 create mode 100644 scripts/themes/fonts/gYAtqXUikkQjyJA1SnpDLvesZW2xOQ-xsNqO47m
55DA.woff2
 create mode 100644 scripts/themes/fonts/iQ9VJx1UMASKNiGywyyCXvesZW2xOQ-xsNqO47m
55DA.woff2
 create mode 100644 scripts/themes/fonts/sDGTilo5QRsfWu6Yc11AXg.woff2

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 11, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (11/11), done.
Writing objects: 100% (11/11), 152.19 KiB | 0 bytes/s, done.
Total 11 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/YQMCU/books_study.git
   626b34a..f556673  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/
        note_template.html
        scripts/markdown_parse.js

nothing added to commit but untracked files present (use "git add" to track)

D:\Documents and Settings\study_practise\books_study>git add 02-web_scraping_wit
h_Python/
warning: LF will be replaced by CRLF in 02-web_scraping_with_Python/note.html.
The file will have its original line endings in your working directory.

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:Web Scra
ping with Python note use markdown_parse.js to convert the html"
[master a405e9d] Add:Web Scraping with Python note use markdown_parse.js to conv
ert the html
 10 files changed, 765 insertions(+)
 create mode 100644 02-web_scraping_with_Python/codes/link_scrape.py
 create mode 100644 02-web_scraping_with_Python/codes/sitemap.xml
 create mode 100644 02-web_scraping_with_Python/codes/sitemap_parse.py
 create mode 100644 02-web_scraping_with_Python/codes/url_download.py
 create mode 100644 02-web_scraping_with_Python/codes/url_download.pyc
 create mode 100644 02-web_scraping_with_Python/codes/url_download_retry.py
 create mode 100644 02-web_scraping_with_Python/codes/url_download_retry.pyc
 create mode 100644 02-web_scraping_with_Python/codes/url_download_set_agent.py
 create mode 100644 02-web_scraping_with_Python/note.html
 create mode 100644 02-web_scraping_with_Python/test.html

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 14, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (14/14), done.
Writing objects: 100% (14/14), 8.00 KiB | 0 bytes/s, done.
Total 14 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   f556673..a405e9d  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        note_template.html
        scripts/markdown_parse.js

nothing added to commit but untracked files present (use "git add" to track)

D:\Documents and Settings\study_practise\books_study>git add scripts/markdown_pa
rse.js

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:the scri
pt for markdown format content convert to the common text"
[master e9d3a20] Add:the script for markdown format content convert to the commo
n text
 1 file changed, 22 insertions(+)
 create mode 100644 scripts/markdown_parse.js

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 792 bytes | 0 bytes/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   a405e9d..e9d3a20  master -> master


D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   git_cmd_note.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        note_template.html

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add note_template.html

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:note tem
plate"
[master e9542cc] Add:note template
 1 file changed, 26 insertions(+)
 create mode 100644 note_template.html

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 734 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   dda85e2..e9542cc  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    02-web_scraping_with_Python/codes/link_scrape.py
        deleted:    02-web_scraping_with_Python/codes/sitemap.xml
        deleted:    02-web_scraping_with_Python/codes/sitemap_parse.py
        deleted:    02-web_scraping_with_Python/codes/url_download.py
        deleted:    02-web_scraping_with_Python/codes/url_download.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.py
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_set_agent.py
        modified:   02-web_scraping_with_Python/test.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/codes/ch01/

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add 02-web_scraping_wit
h_Python/codes/ch01/

D:\Documents and Settings\study_practise\books_study>git commit -m "Modify:move
current python codes to ch01/"
[master 9411178] Modify:move current python codes to ch01/
 8 files changed, 99 insertions(+)
 create mode 100644 02-web_scraping_with_Python/codes/ch01/link_scrape.py
 create mode 100644 02-web_scraping_with_Python/codes/ch01/sitemap.xml
 create mode 100644 02-web_scraping_with_Python/codes/ch01/sitemap_parse.py
 create mode 100644 02-web_scraping_with_Python/codes/ch01/url_download.py
 create mode 100644 02-web_scraping_with_Python/codes/ch01/url_download.pyc
 create mode 100644 02-web_scraping_with_Python/codes/ch01/url_download_retry.py

 create mode 100644 02-web_scraping_with_Python/codes/ch01/url_download_retry.py
c
 create mode 100644 02-web_scraping_with_Python/codes/ch01/url_download_set_agen
t.py

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 447 bytes | 0 bytes/s, done.
Total 4 (delta 2), reused 0 (delta 0)
fatal: The remote end hung up unexpectedly
fatal: The remote end hung up unexpectedly
error: RPC failed; curl 6 SSL read: error:00000000:lib(0):func(0):reason(0), err
no 10054
Everything up-to-date

D:\Documents and Settings\study_practise\books_study>git push
fatal: AggregateException encountered.
   发生一个或多个错误。
Username for 'https://github.com': yqmcu
Password for 'https://yqmcu@github.com':
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/YQMCU/books_study.git/'

D:\Documents and Settings\study_practise\books_study>git push
Everything up-to-date

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    02-web_scraping_with_Python/codes/link_scrape.py
        deleted:    02-web_scraping_with_Python/codes/sitemap.xml
        deleted:    02-web_scraping_with_Python/codes/sitemap_parse.py
        deleted:    02-web_scraping_with_Python/codes/url_download.py
        deleted:    02-web_scraping_with_Python/codes/url_download.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.py
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_set_agent.py
        modified:   02-web_scraping_with_Python/test.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/codes/ch02/

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add 02-web_scraping_wit
h_Python/codes/ch02/

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:chapter0
2 codes"
[master 8121dd5] Add:chapter02 codes
 1 file changed, 10 insertions(+)
 create mode 100644 02-web_scraping_with_Python/codes/ch02/regex_demo.py

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 6, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 651 bytes | 0 bytes/s, done.
Total 6 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/YQMCU/books_study.git
   9411178..8121dd5  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    02-web_scraping_with_Python/codes/link_scrape.py
        deleted:    02-web_scraping_with_Python/codes/sitemap.xml
        deleted:    02-web_scraping_with_Python/codes/sitemap_parse.py
        deleted:    02-web_scraping_with_Python/codes/url_download.py
        deleted:    02-web_scraping_with_Python/codes/url_download.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.py
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_set_agent.py
        modified:   02-web_scraping_with_Python/test.html

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git rm 02-web_scraping_with
_Python/codes
fatal: not removing '02-web_scraping_with_Python/codes' recursively without -r

D:\Documents and Settings\study_practise\books_study>git rm -h
usage: git rm [<options>] [--] <file>...

    -n, --dry-run         dry run
    -q, --quiet           do not list removed files
    --cached              only remove from the index
    -f, --force           override the up-to-date check
    -r                    allow recursive removal
    --ignore-unmatch      exit with a zero status even if nothing matched


D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    02-web_scraping_with_Python/codes/link_scrape.py
        deleted:    02-web_scraping_with_Python/codes/sitemap.xml
        deleted:    02-web_scraping_with_Python/codes/sitemap_parse.py
        deleted:    02-web_scraping_with_Python/codes/url_download.py
        deleted:    02-web_scraping_with_Python/codes/url_download.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.py
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_set_agent.py
        modified:   02-web_scraping_with_Python/test.html
        modified:   git_cmd_note.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/codes/ch02/bs4_find_demo.py
        02-web_scraping_with_Python/codes/ch02/soup_parse_demo.py

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    02-web_scraping_with_Python/codes/link_scrape.py
        deleted:    02-web_scraping_with_Python/codes/sitemap.xml
        deleted:    02-web_scraping_with_Python/codes/sitemap_parse.py
        deleted:    02-web_scraping_with_Python/codes/url_download.py
        deleted:    02-web_scraping_with_Python/codes/url_download.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.py
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_set_agent.py
        modified:   02-web_scraping_with_Python/test.html
        modified:   git_cmd_note.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/codes/ch02/bs4_find_demo.py
        02-web_scraping_with_Python/codes/ch02/bs4_scraping.py
        02-web_scraping_with_Python/codes/ch02/lxml_css_demo.py
        02-web_scraping_with_Python/codes/ch02/lxml_parse_demo.py
        02-web_scraping_with_Python/codes/ch02/soup_parse_demo.py
        02-web_scraping_with_Python/codes/ch02/url_download.py
        02-web_scraping_with_Python/codes/ch02/url_download.pyc
        02-web_scraping_with_Python/n.c
        CNAME
        example.webscraping.html

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git add CNAME

D:\Documents and Settings\study_practise\books_study>git commit -m "Add:change n
ame for visiting"
[master a457475] Add:change name for visiting
 1 file changed, 1 insertion(+)
 create mode 100644 CNAME

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 288 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   8121dd5..a457475  master -> master

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    02-web_scraping_with_Python/codes/link_scrape.py
        deleted:    02-web_scraping_with_Python/codes/sitemap.xml
        deleted:    02-web_scraping_with_Python/codes/sitemap_parse.py
        deleted:    02-web_scraping_with_Python/codes/url_download.py
        deleted:    02-web_scraping_with_Python/codes/url_download.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.py
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_set_agent.py
        modified:   02-web_scraping_with_Python/test.html
        deleted:    CNAME
        modified:   git_cmd_note.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/codes/ch02/bs4_find_demo.py
        02-web_scraping_with_Python/codes/ch02/bs4_scraping.py
        02-web_scraping_with_Python/codes/ch02/lxml_css_demo.py
        02-web_scraping_with_Python/codes/ch02/lxml_parse_demo.py
        02-web_scraping_with_Python/codes/ch02/soup_parse_demo.py
        02-web_scraping_with_Python/codes/ch02/url_download.py
        02-web_scraping_with_Python/codes/ch02/url_download.pyc
        02-web_scraping_with_Python/n.c
        example.webscraping.html

no changes added to commit (use "git add" and/or "git commit -a")

D:\Documents and Settings\study_practise\books_study>git rm CNAME
rm 'CNAME'

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        deleted:    CNAME

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    02-web_scraping_with_Python/codes/link_scrape.py
        deleted:    02-web_scraping_with_Python/codes/sitemap.xml
        deleted:    02-web_scraping_with_Python/codes/sitemap_parse.py
        deleted:    02-web_scraping_with_Python/codes/url_download.py
        deleted:    02-web_scraping_with_Python/codes/url_download.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.py
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_set_agent.py
        modified:   02-web_scraping_with_Python/test.html
        modified:   git_cmd_note.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/codes/ch02/bs4_find_demo.py
        02-web_scraping_with_Python/codes/ch02/bs4_scraping.py
        02-web_scraping_with_Python/codes/ch02/lxml_css_demo.py
        02-web_scraping_with_Python/codes/ch02/lxml_parse_demo.py
        02-web_scraping_with_Python/codes/ch02/soup_parse_demo.py
        02-web_scraping_with_Python/codes/ch02/url_download.py
        02-web_scraping_with_Python/codes/ch02/url_download.pyc
        02-web_scraping_with_Python/n.c
        example.webscraping.html


D:\Documents and Settings\study_practise\books_study>

D:\Documents and Settings\study_practise\books_study>git push
Everything up-to-date

D:\Documents and Settings\study_practise\books_study>git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        deleted:    CNAME

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    02-web_scraping_with_Python/codes/link_scrape.py
        deleted:    02-web_scraping_with_Python/codes/sitemap.xml
        deleted:    02-web_scraping_with_Python/codes/sitemap_parse.py
        deleted:    02-web_scraping_with_Python/codes/url_download.py
        deleted:    02-web_scraping_with_Python/codes/url_download.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.py
        deleted:    02-web_scraping_with_Python/codes/url_download_retry.pyc
        deleted:    02-web_scraping_with_Python/codes/url_download_set_agent.py
        modified:   02-web_scraping_with_Python/test.html
        modified:   git_cmd_note.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        02-web_scraping_with_Python/codes/ch02/bs4_find_demo.py
        02-web_scraping_with_Python/codes/ch02/bs4_scraping.py
        02-web_scraping_with_Python/codes/ch02/lxml_css_demo.py
        02-web_scraping_with_Python/codes/ch02/lxml_parse_demo.py
        02-web_scraping_with_Python/codes/ch02/soup_parse_demo.py
        02-web_scraping_with_Python/codes/ch02/url_download.py
        02-web_scraping_with_Python/codes/ch02/url_download.pyc
        02-web_scraping_with_Python/n.c
        example.webscraping.html


D:\Documents and Settings\study_practise\books_study>git commit -m "RM:remove CN
AME"
[master 7a7f633] RM:remove CNAME
 1 file changed, 1 deletion(-)
 delete mode 100644 CNAME

D:\Documents and Settings\study_practise\books_study>git push
fatal: unable to access 'https://github.com/YQMCU/books_study.git/': Couldn't re
solve host 'github.com'

D:\Documents and Settings\study_practise\books_study>git push
Counting objects: 2, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 226 bytes | 0 bytes/s, done.
Total 2 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/YQMCU/books_study.git
   a457475..7a7f633  master -> master

   











