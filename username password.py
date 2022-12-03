import admin_

tries = 0
while tries < 5:
    uname = input("Username: ")
    pword = input("Password: ")

    dict_admin = {"admin123":"dylan321","james321":"james321"}
    dict_user = {"user123":"james420"}

    if uname in dict_admin.keys() and pword == dict_admin[uname]:
        admin()
    elif uname in dict_user.keys() and pword == dict_user[uname]:
        print("You are user.")
        break
    else:
        print("You have entered wrong username and password, would you like to sign-up.")
    tries += 1