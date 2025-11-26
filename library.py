import json
import os
from datetime import datetime
from user import login1
# user1 = login1()
class library:
    #INITIALIZE CONSTRUCTOR 
    def __init__(self):
        self.bookslist = []
        self.user_files = login1()
    # LOAD JSON DATA FILE
    def load_data(self):
        if not os.path.exists(self.user_files):
            return {"Username": self.user_files, "Insert": []}
        else:
            with open(self.user_files,'r') as fp:
                return json.load(fp)
    # SAVE JSON DATA IN DATA BASE
    def save_file(self,user):
            with open(self.user_files,'w') as file:
                return json.dump(user,file)
    # LISTING OF BOOKS
    def list_books(self,lib):
        print(".................LISTING BOOKS...................")
        for i in range(0,len(lib)):
            self.bookslist.append(lib[i])
        print("\nAvailable Books:")
        for b in self.bookslist:
            print(b)
        print(self.bookslist)
    
    # CHOOSE AND ADD BOOK IN DATABASE
    def choose_book(self,choice):
        print(f'Your choice is {choice}')
        try:
            date = input("Enter date in format yyyy-mm-dd  or Enter 0 for taking automatically:")
            if date=='0':
                date = datetime.today().strftime("%Y-%m-%d")
            else:
                date = datetime.strptime(date ,'%Y-%m-%d').strftime("%Y-%m-%d")
        except:
            raise ValueError("Enter correct date")
        for n in range(0,len(self.bookslist)+1):
            match n:
                case n:
                    print(f"Your Book is {self.bookslist[choice-1]}")
                    break
        dict1 = {"Books: ": self.bookslist[choice-1],
                "Date":date}
        lab = self.load_data()
        if not dict1 in lab["Insert"]:
            
            if "Insert" not in lab:
                lab["Insert"] = []
            
                lab["Insert"].append(dict1)
        
            else:
                lab["Insert"].append(dict1)
        else:
            print("Book given")
        self.save_file(lab)
    # SHOW BOOKS IN DATABASE
    def show_lib_books(self):
        lab = self.load_data()
        load = lab.get("Insert",[])
        print("Your books record are:")
        if not load:
            print("No Record")
        else:
            for e in load:
                print(f'Books: {e["Books: "]} | Date: {e["Date"]}')
        
    def remove(self,choice):
        lab1 = self.load_data()
        load1 = lab1.get("Insert",[])
        if not load1:
            print("No record for remove")
        else:
            removed = load1.pop(choice -1)
            print(f'The Book You Returned Is {removed.get("Books: ")}')
        self.save_file(lab1)
        
        # print(f'Removed book is {removed.get('Books: ')} on date {removed.get('Date')}')
            
            
a= library()
# book = input("Enter book name:")
# a.add_books(book)

lib_Books = ["1.Python Crash Course — Eric Matthes","2.Automate the Boring Stuff with Python — Al Sweigart","3.Head First Python — Paul Barry",
    "4.Learn Python the Hard Way — Zed A. Shaw",
    "5.Think Python — Allen B. Downey",
    "6.Python for Everybody — Charles Severance",
    "7.A Smarter Way to Learn Python — Mark Myers",
    "8.Programming in Python — Mark Lutz",
    "9.Effective Python — Brett Slatkin",
    "10.Fluent Python — Luciano Ramalho",
    "11.Python Tricks — Dan Bader",
    "12.Learning Python — Mark Lutz",
    "13.Python Cookbook — David Beazley & Brian K. Jones",
    "14.Serious Python — Julien Danjou",
    "15.Introduction to Machine Learning with Python — Andreas Müller",
    "16.High Performance Python — Micha Gorelick & Ian Ozsvald",
    "17.Expert Python Programming — Michal Jaworski",
    "18.Python Design Patterns — Chetan Giridhar",
    "19.Mastering Python — Rick van Hattem",
    "20.Data Structures and Algorithms in Python — Goodrich, Tamassia, Goldwasser"]

while(1):
    input1 = int(input("\n\n1.Showing list\n2.choose book and add to your account\n3.show books in my account\n4.Remove Returned Book\n5.exit\nEnter Your Choice:"))
    match input1:
        case 1:
            a.list_books(lib_Books)
        case 2:
            a.list_books(lib_Books)
            print("Choose a book by entering serial number of book")
            choice = int(input("Enter choice:"))
            a.choose_book(choice)
        case 3:
            a.show_lib_books()
        case 4:
            print("Returned Book Remove")
            print("Choose a book by entering serial number of book in database")
            choice = int(input("Enter choice:"))
            a.remove(choice)
        case 5:
            exit()
        case _:
            print("Enter valid Choice")

            
