def cred():

    splchar= "!@#$%^&*()_+={}\[]|/;'"",.<>?"
    locase='abcdefghijklmnopqrstuvwxyz'
    upcase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num="0123456789"
    k=l=0
    if id[0] in splchar or id[0] in num:
            exit("id should not start with special character or a number")
    id1=id.split('@')

    if id1[1]!='gmail.com' and id1[1]!='yahoo.in':
        exit("not in email format")
    print(" register to login")
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    phone_num = input("Enter mobile number: ")

            #password format
    print("Minimum and Maximum length of password is 5 ,16\n "
          "Password must have 1 upper case,1 lowercas,1 digit ,1 splecial character ")
    pword=input("Enter the password : ")
    if len(pword)< 5 : print("Too small")
    elif len(pword)>16:print("Too long")
    def forconditions(a,b,c):
            k=0
            for i in a:
                if i in b:
                    k+=1
            if k == 0:
                    exit(f" no {c} found")
    forconditions(pword,splchar,'special_character')
    forconditions(pword,num,'number')
    forconditions(pword,locase,'lower_case letter')
    forconditions(pword,upcase,'uppercase letter')
    user=fname+" "+lname+" "+phone_num+" "+id+" "+pword+"\n"
    file1=open("logins_database3.txt","a+")
    file1.write(user)
    file1.close()
    print("Run again for access")

print("email format: user_name@gmail.com or user_name@yahoo.in ")
id=input("Enter the email id/user name: ")
file2=open("logins_database3.txt","r+")
readfile=file2.read()
if id in readfile:
    print("Enter the password  or Enter 2 to access forget password")
    psword=input()
    with open("logins_database3.txt","r+") as f:
        for line in f:
            userArray=(line.split())
            if id in userArray:
                l=[]
                text=str(userArray)
                if psword== userArray[4]:
                    print("Access granted")
                    ch=input("To change password enter 5 otherwise enter 0 :")
                    if ch=='5':
                        mob=input("Enter your mobile number")
                        if userArray[2]==mob:
                            od=input("Enter old password")
                            np=input("Enter new password")
                            repl = line.replace(userArray[4], np)
                            with open("logins_database3.txt", "r+") as k:
                                lines = k.readlines()
                                ptr = id
                                with open("logins_database3.txt", "w") as fw:
                                    for line in lines:
                                        if ptr not in line:
                                            fw.write(line)
                                with open("logins_database3.txt", "a+") as fa:
                                        fa.seek(0)
                                        fa.write(repl)


                        else:
                            print("Incorrect mobile number")
                    elif ch==0:
                        print("Login successful")
                elif psword == '2':
                    print("password :",userArray[4])
                else:
                    print("Incorrect password")
                    print("Enter 2 to access forget password")
                    forget=int(input())
                    if forget==2:
                        print("password: ",userArray[4])
            file2.close()
else:
    cred()