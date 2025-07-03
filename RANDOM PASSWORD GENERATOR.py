import random  #RANDOM PASSWORD GENERATOR
import string
ghontu = string.ascii_letters + string.digits + string.punctuation
no = int(input("Enter the length of password you want:"))
print("Your random password of the required length is:")
for i in range (no):
    ti = random.choice(ghontu)
    print(ti , end= "")