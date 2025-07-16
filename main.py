iduser = ' '
password1 = ' '
#creating login user id
def userid():
    global iduser
    iduser = input("Create Your User I'd : ")
    if ( len(iduser) >= 8 and len(iduser) <= 16 ):
        print ("\n\n\t\t"" Your User I'd is : " , iduser)
    else:
        while ( len(iduser) not in range(8,16) ):
            print("Invalid selection.. :( ""\n\n""Try again...""\n")
            iduser = input("Create Your User I'd : ")
            if ( len(iduser) >= 8 and len(iduser) <= 16 ):
                print ("\n\n\t\t"" Your User I'd is : " , iduser)
                break
            else:
                continue


#password strength check
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔸 Use at least 8 characters.")

    # Upper and lower case
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("🔸 Mix uppercase and lowercase letters.")

    # Digits
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("🔸 Add some numbers.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("🔸 Include special characters.")

    # Overall rating
    if strength == 4:
        return "✅ Strong password!"
    elif strength >= 2:
        return "⚠️ Medium strength password.\n" + "\n".join(feedback)
    else:
        return "❌ Weak password.\n" + "\n".join(feedback)

#generate password
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password



#password creation
def password():
    global password1
    trying = 0
    choice = input("\n\n""Do you want to generate a password (press 1 to create own & any other to generate ) :")
    if choice=='1':
        print ("\n\n""Password should have minimum 8 characters including atleast a number and a symbol ")
        while trying == 0:
            password1 = input ("\n\n""Create a strong password : ")
            print(check_password_strength(password1))
            choice2 = input("\n\n""Do you want to continue with this password (press 1 to continue & any other to try again) : ")
            if choice2 == '1':
                break
            else:
                continue
    else:
        password1 = generate_password()
        print ("\n\n\t\t""Your default password is : ", password1)


#main process
print ("\n\n\t\t\t\t""Login Page""\n\n\n\n")
count = 1
while count == 1:
    userid()
    password()
    choose = input("\n\n""Do you want to change your credentials (if yes press 1 and to continue press any other) : ")
    if choose == '1':
        count = 1
    else:
        break
count = 1
while count == 1:
    print ("\n\n\t\t\t\t""Login Page""\n\n\n\n")
    iduser2 = input("User I'd : ")
    password2 = input("Password : ")
    if iduser2 == iduser and password1 == password2:
        print("\n\n\n\t\t"" Welcome :) ")
        break
    else:
        print("Invalid credentials :( ")
        continue
