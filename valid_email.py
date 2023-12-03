email = input("Enter Your Email: ")# TAKE USER INPUT
k,j,d=0,0,0
if len(email)>=6:# EMAIL LETTER SHOULD BE ATLEAST 6
    if email[0].isalpha():# FIRST LETTER OF EMAIL SHOULD BE ALPHABIT 
        if "@" in email and email.count('@')==1:
            for i in email :
                if i==i.isspace():
                    k=1
                elif i.isalpha():
                    if i==i.isupper():
                        j=1
                elif i.isdigit():
                    continue
                elif i=="_" or i=="." or i=="@":
                    continue
                else:
                    d=1
            if k==1 or d==1 or d==1:
                print('PLEASE ENTER A VAILID EMAIL ID ') 
            else:
                print('right email')       
        else:
            print('PLEASE ENTER A VALID EMAIL ID ')
    else:
        print("PLEASE ENTER A VALID EMAIL ID ")
else:
    print ("PLEASE ENTER A VALID EMAIL ID ")
