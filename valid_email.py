email = input("Enter Your Email: ")# TAKE USER INPUT

if len(email)>=6:# EMAIL LETTER SHOULD BE ATLEAST 6
    if email[0].isalpha():# FIRST LETTER OF EMAIL SHOULD BE ALPHABIT 
        if "@" in email and email.count('@')==1:
            pass
        else:
            print('PLEASE ENTER A VALID EMAIL ID ')
    else:
        print("PLEASE ENTER A VALID EMAIL ID ")
else:
    print ("PLEASE ENTER A VALID EMAIL ID ")
