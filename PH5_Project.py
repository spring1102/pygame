username = input("please input username：")
if username == "admin":
    password = input("please input password:")
    if password == "admin":
        print("login successfully!")
    else:
        print("wrong password!")
else:
    print("wrong username")
