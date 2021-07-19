import os
import sys

excludes = [".git", "build", "project-gen.py"]
excludes = [os.path.join(os.getcwd(), path) for path in excludes]

default_project_name = "default_project_name"
default_author = "default_author"
default_nickname = "default_nickname"


def main():
    print("This is auto-generation script for c++ opensource project")
    print("You should input informations matched with your github repository")

    project_name = input("Please input project name: ")
    if project_name == "":
        project_name = default_project_name
    author = input("Please input author: ")
    if author == "":
        author = default_author
    nickname = input("Please input nickname: ")
    if nickname == "":
        nickname = default_nickname

    for dname, _, files in os.walk(os.getcwd()):
        for fname in files:
            fpath = os.path.join(dname, fname)
            skip = False
            for exclude in excludes:
                if exclude in fpath:
                    skip = True
            if not skip:
                print("Processing: ", fpath)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                    content = content.replace("${project_name}", project_name)
                    content = content.replace("${author}", author)
                    content = content.replace("${nickname}", nickname)
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content)

    while True:
        choice = input("Remove this script? [Y/N]").lower()
        if choice == 'y':
            os.remove(sys.argv[0])
            break
        elif choice == 'n':
            break
        else:
            print("Please input Y or N")


if __name__ == "__main__":
    main()
