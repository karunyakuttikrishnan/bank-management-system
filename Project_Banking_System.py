import pickle
import os.path
import random

class Account():
    acc_no=0
    acc_type=""
    balance=0
    username=""
    def Create(self):
        self.acc_no =random.randint(1000,9999)
        self.username =input("username = ")
        self.balance = int(input("Enter initial amount"))
        self.acc_type = input("Enter account type (C/S):")
        print("Your Account number is : ", self.acc_no)
        print("Account Created Succesfully")
        return self.username,self.balance,self.acc_type,self.acc_no

#CHOICE 1
def account_details():
    a1=Account()
    a1.Create()
    writeToFile(a1)

def writeToFile(a1):
    file="account_details.data"
    if os.path.isfile("account_details.data"):
        infile=open("account_details.data","rb")
        old_data=pickle.load(infile)
        old_data.append(a1)
        infile.close()
    else:
        old_data=[a1]
    #pickling again
    outfile = open('newaccounts.data','wb')
    pickle.dump(old_data, outfile)
    outfile.close()
    os.remove("account_details.data")
    os.rename('newaccounts.data', 'account_details.data')

#CHOICE 2
def getdetails(name,ac_no):
    file="account_details.data"
    if os.path.isfile("account_details.data"):
        infile=open("account_details.data","rb")
        data=pickle.load(infile)
        for i in data:
            if i.username == name and i.acc_no==ac_no:
                found=1
                print("Username =", i.username,"\n","Account number = ",ac_no,"\n","Account type =",i.acc_type, "\n","Balance = ",i.balance)
                break
            else:
                found=0
                continue
        if found==0:
            print("Invalid username or password")


#CHOICE 3
def DepositAmount(name,ac_no):
    file = "account_details.data"
    if os.path.isfile(file):
        infile = open("account_details.data", "rb")
        data = pickle.load(infile)
        infile.close()
        for i in data:
            if i.username == name and i.acc_no==ac_no:
                found=1
                deposit = int(input("Enter the amount to be deposited:"))
                i.balance += deposit
                print("Amount Deposited Successfully")
                print("Current balance = ",i.balance)
                break
            else:
                found=0
                continue
        if found==0:
            print("Invalid username or password")
    os.remove("account_details.data")
    outfile = open("newaccounts.data", "wb")
    pickle.dump(data, outfile)
    outfile.close()
    os.rename("newaccounts.data", "account_details.data")

#CHOICE=4
def WithdrawAmount(name,ac_no):
    file = "account_details.data"
    if os.path.isfile(file):
        infile = open("account_details.data", "rb")
        data = pickle.load(infile)
        infile.close()
        os.remove("account_details.data")
        for i in data:
            if i.username == name and i.acc_no==ac_no:
                found=1
                amount = int(input("Enter the amount to be withdrawn:"))
                i.balance-= amount
                print("Amount Withdrawn Successfully")
                print("Current balance =", i.balance)
                break
            else:
                found=0
                continue
        if found==0:
            print("Invalid username or password")
    outfile = open("newaccounts.data", "wb")
    pickle.dump(data, outfile)
    outfile.close()
    os.rename("newaccounts.data", "account_details.data")

#CHOICE=5
def getbalance(name,ac_no):
    file="account_details.data"
    if os.path.isfile("account_details.data"):
        infile=open("account_details.data",'rb')
        data=pickle.load(infile)
        for i in data:
            if i.username == name and i.acc_no==ac_no:
                found=1
                print("Balance = ",i.balance)
                break
            else:
                found=0
                continue
        if found==0:
            print("Invalid username and password")

#CHOICE 6
def getalldetails():
    file="account_details.data"
    if os.path.isfile("account_details.data"):
        infile=open("account_details.data",'rb')
        data=pickle.load(infile)
        infile.close()
        for i in data:
            print("Username =", i.username,"\n","Account number = ",i.acc_no,"\n","Account type =",i.acc_type,
                  "\n","Balance = ",i.balance)
    else:
        print("No records to show")

#CHOICE 7
def mofifyaccount(name,ac_no):
    file="account_details.data"
    if os.path.isfile(file):
        infile=open("account_details.data","rb")
        data = pickle.load(infile)
        infile.close()
        for i in data:
            if i.username==name and i.acc_no==ac_no:
                found=1
                print("""
                    1.MODIFY USERNAME
                    2.MODIFY ACCOUNT TYPE""")
                choice = int(input("Enter your choice:"))
                if choice == 1:
                    i.username=input("Enter new username:")
                    print("Username changed succesfully")
                    break
                elif choice == 2:
                    i.acc_type=input("Enter new account type(C/S):")
                    print("Account type changed succesfully")
                    break
                else:
                    print("Enter a valid choice")
                    break
            else:
                found=0
                continue
        if found==0:
            print("Username or account number incorrect")
    os.remove("account_details.data")
    outfile=open("new_accountdetails.data","wb")
    pickle.dump(data,outfile)
    outfile.close()
    os.rename("new_accountdetails.data","account_details.data")

#CHOICE 8
def deleteaccount(ac_no):
    file="account_details.data"
    if os.path.isfile(file):
        infile=open(file,"rb")
        data=pickle.load(infile)
        infile.close()
        newlist=[]
        for i in data:
            if i.acc_no!=ac_no:
                newlist.append(i)
        outfile=open("newaccounts.data","wb")
        pickle.dump(newlist,outfile)
        outfile.close()
        os.remove("account_details.data")
        os.rename("newaccounts.data","account_details.data")
        print("Account deleted")
    else:
        print("No reccords found")

def first():

    print("""
             ***************
             BANKING SYSTEM
             ***************\n
    1.ACCOUNT CREATION
    2.GET ACCOUNT DETAILS
    3.DEPOSIT
    4.WITHDRAW
    5.CHECK BALANCE
    6.GET ALL USER DETAILS
    7.MODIFY ACCOUNT
    8.DELETE ACCOUNT
    9.LOGOUT"""
          )
    option = int(input("Enter your option:"))

    if option==1:
        account_details()
        first()
    elif option==2:
        name = input("Enter your username:")
        ac_no = int(input("Enter account number: "))
        getdetails(name,ac_no)
        first()
    elif option==3:
        name = input("Enter your username:")
        ac_no = int(input("Enter account number: "))
        DepositAmount(name,ac_no)
        first()
    elif option==4:
        name = input("Enter your username:")
        ac_no = int(input("Enter account number: "))
        WithdrawAmount(name,ac_no)
        first()
    elif option==5:
        name = input("Enter your username:")
        ac_no = int(input("Enter account number: "))
        getbalance(name,ac_no)
        first()
    elif option==6:
        getalldetails()
        first()
    elif option==7:
        name = input("Enter your username:")
        ac_no = int(input("Enter account number: "))
        mofifyaccount(name,ac_no)
        first()
    elif option==8:
        name=input("Enter your username:")
        ac_no=int(input("Enter your account number: "))
        deleteaccount(ac_no)
        first()
    elif option==9:
        print("Loggged out succesfully")
    else:
        print("Please enter a valid option")
        first()

first()













