import os
import json
import random2 as rd


def reg():
    name = input("Enter your name:")
    user = f"{name}.json"
    
    if os.path.exists(user):
        print("User already register")
        login1()
    else:
        print("User added successfully!")
        id = rd.randint(0,1000)
        print("Your id is",id)
        saved = {'Username':name,'Id':id}
        with open(user,'w') as fp:
            json.dump(saved,fp)
    

def login1():
    name = input("Enter your name:")
    user = f'{name}.json'
    id = int(input("Enter id:"))
    if not os.path.exists(user):
        print('User not exist')
        reg()
    else:
        with open(user,'r') as file:
            data = json.load(file)
        if (data['Username']==name and data['Id']==id):
            print("Login successfully")
            return data['Username']
        else:
            print("Invalid username or id")
            


