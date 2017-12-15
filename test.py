from subprocess import call
x=input("введите комментарий:")
call(["git", "status"])
call(["git", "add", "."])
call(["git", "commit", "-m", x])
call(["git", "push"])