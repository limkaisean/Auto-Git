import sys
import os
import autogitconfig as cfg
from github import Github

path = os.getcwd()

def create():
    argsLen = len(sys.argv) 
    repoName = ' '.join(sys.argv[1:])
    os.makedirs(path + "/" + repoName)
    user = Github(cfg.username, cfg.password).get_user()
    repo = user.create_repo(repoName)
    print("Repository" + repoName + "was successfully created.")
    print(repoName)


if __name__ == "__main__":
    create()