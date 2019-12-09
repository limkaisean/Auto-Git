@echo off

cd "C:\"
cd "C:\Users\User\Desktop\Github Projects"
py autogit.py %*
set repoName=%*
cd "C:\Users\User\Desktop\Github Projects\%repoName%"
set repoName=%repoName: =-%
git init
git remote add origin git@github.com:limkaisean/repoName.git
type nul > README.md
git add .
git commit -m "Initial commit"
git push -u origin master
