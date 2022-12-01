import datetime
t_date=datetime.date.today()
t_time=datetime.datetime.now()
shopping = [{"id": 1001, "Name": "HP-AE12", "Available": 100, "Price": 25000, "Original_Price": 24000},
            {"id": 1002, "Name": "DELL", "Available": 100, "Price": 35000, "Original_Price": 34000},
            {"id": 1003, "Name": "ASUS", "Available": 100, "Price": 28000, "Original_Price": 27000},
            {"id": 1004, "Name": "APPLE", "Available": 100, "Price": 60000, "Original_Price": 59000},
            {"id": 1005, "Name": "ACER", "Available": 100, "Price": 24000, "Original_Price": 23000},
            {"id": 1006, "Name": "SAM", "Available": 100, "Price": 35000, "Original_Price": 34000},
            {"id": 1007, "Name": "OPPO", "Available": 100, "Price": 15000, "Original_Price": 14000},
            {"id": 1008, "Name": "XAOMI", "Available": 100, "Price": 45000, "Original_Price": 44000},
            {"id": 1009, "Name": "HUAWEI", "Available": 100, "Price": 20000, "Original_Price": 19000},
            {"id": 1010, "Name": "VIVO", "Available": 100, "Price": 12000, "Original_Price": 11000}]

shopping1 = shopping
temp = []
order = ""

def adminLoginWindow():
    print(" ")
    print("=" * 130)
    print(" ")
    print("E-COMMERCE TEXT-BASES APPLICATION".center(130))
    print(" ")
    print("=" * 130)
    print(" ")
    print("1. DISPLAY".center(130))
    print("2.ADD PRODUCT".center(130))
    print("3.REMOVE PRODUCT".center(130))
    print("4.PRODUCT AVAILABLE".center(130))
    print("5.TOTAL INCOME".center(130))
    print("6.LOGOUT".center(130))
    print(" ")
    print("=" * 130)
    print(" ")

##########ADMIN DISPLAY PRODUCT##########
    
def adminDisplayMenuWindow():
    print("Id\tName\tAvailable\tPrice\tOriginal Price".center(130))
    print("="*130)
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}\t{d["Original_Price"]}'.center(130))
        
############ADD PRODUCT###############
        
def addproducts():
    n = int(input("                                              ENTER THE NO OF ITEMS TO BE ADDED : "))
    for i in range(n):
        new_id = int(input("                                              ENTER ID : "))
        new_Name = input("                                              ENTER NAME : ")
        new_Available = int(input("                                              ENTER QUANTITY : "))
        new_Price = int(input("                                              ENTER PRICE : "))
        new_original = int(input(                                              "ENTER ORIGINAL PRICE : "))
        d = [{"id": new_id, "name": new_Name, "available": new_Available, "price": new_Price,
              "original_price": new_original}]
        shopping.extend(d)
        adminDisplayMenuWindow()

##########REMOVE PRODUCT##########
        
def removeproducts():
    dressId = int(input("                              ENTER ID OF PRODUCT : "))
    found = False
    for d in shopping1:
        found = d["id"] == dressId
        if found != True:
            temp.append(d)
            continue
        if found == True:
            d["Available"] -= 1
    print("DELETING ITEM..............".center(130))
    if len(temp) == d:
        print(f"{dressId} NOT FOUND".center(130))
    else:
        print(f"{dressId}'S ONE AVAILABLE IS REMOVED FROM THE LIST".center(130))
    adminDisplayMenuWindow()

##########AVAILABLE PRODUCT##########
def availableproducts():
    Total = 0
    print("\n")
    for d in shopping:
        print(f'{d["Name"]} = {d["Available"]}')
        Total += (d["Available"])
    print("\n                                              TOTAL PRODUCT AVAILABLE : ", Total)

##########MONTHLY INCOME##########

def monthlyincome():
    total = 0
    for d in shopping:
        total += ((d["Available"] * d["Price"]) - (d["Available"] * d["Original_Price"]))
    print("\n                                              TOTAL INCOME : ", total)

##########LOGOUT##########

def logoutwindow():
    login()

##########ADMIN OPTION##########

def adminOptions():
    choice = int(input("                                              ENTER YOUR CHOICE : "))
    if choice == 1:
        adminDisplayMenuWindow()
        print()
        print("="*130)
        print()
        adminLoginWindow()
        print()
        print("="*130)
        print()
        adminOptions()
    elif choice == 2:
        adminDisplayMenuWindow()
        print()
        print("="*130)
        print()
        addproducts()
        print()
        print("="*130)
        print()
        adminLoginWindow()
        print()
        print("="*130)
        print()
        adminOptions()
    elif choice == 3:
        adminDisplayMenuWindow()
        print()
        print("="*130)
        print()
        removeproducts()
        print()
        print("="*130)
        print()
        adminLoginWindow()
        print()
        print("="*130)
        print()
        adminOptions()
    elif choice == 4:
        availableproducts()
        print()
        print("="*130)
        print()
        adminLoginWindow()
        print()
        print("="*130)
        print()
        adminOptions()
    elif choice == 5:
        monthlyincome()
        print()
        print("="*130)
        print()
        adminLoginWindow()
        print()
        print("="*130)
        print()
        adminOptions()
    elif choice == 6:
        logoutwindow()
    else:
        print("\n                                              INVALID CHOICE".center(130))
        print()
        print("="*130)
        print()
        adminLoginWindow()
        print()
        print("="*130)
        print()
        adminOptions()

def userLoginWindow():
    print()
    print("="*130)
    print()
    print("1.DISPLAY MENU".center(130))
    print("2.PLACE ORDER".center(130))
    print("3.CANCEL ORDER".center(130))
    print("4.LOGOUT".center(130))
    print()
    print("="*130)
    print()
########## USER DISPLAY#########
    
def userDisplayMenuWindow():
    print("ID\tNAME\tAVAILABLE\tPRICE".center(130))
    print()
    print("="*130)
    print()
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t{d["Price"]}'.center(130))

##########USER ID##########

def user_id():
    userDisplayMenuWindow()
    p_id = int(input("                              ENTER THE ID : "))


def placeOrder():
    order_number = 10
    userDisplayMenuWindow()
    p_id = int(input("                              ENTER THE ID : "))

    for d in shopping:
        if d["id"] == p_id:
            print("\nID\tNAME\tAVAILABLE\tPRICE".center(130))
            print()
            print("="*130)
            print()
            print(f'{d["id"]}\t{d["Name"]}\t\{d["Available"]}\t{d["Price"]}'.center(130))
            order = '{d["id"]}\t{d["Name"]}\t{d["Available"]}\t{d["Price"]}'
            conform = input("DO YOU WANT TO PLACE AN ORDER ON THE ABOVE SHOWN PRODUCT : Y/N ")

            if conform == 'Y' or conform == 'y':
                print("\n SUCCESSFULLY PLACED THE ORDER ON THE PRODUCT {} {}".format(d["id"], d["Name"]))
                order_number += 1
                print("                                              YOUR ORDER NUMBER : ", order_number)
                d["Available"] -= 1
                break

            elif conform == 'N' or conform == 'n':
                print("THE ORDER IS NOT PLACED. YOU CAN CARRY ON WITH YOU PURCHASE. HAPPY SHOPPING!!!!")
                break
            else:
                print("\nYOU HAVE ENTERED WRONG OPTION.PLEASE ENTER AGAIN\n")
                conform = input("\nDO YOU WANT TO PLACE AN ORDER ON THE ABOVE SHOWN PRODUCT: Y/N")
                break

    if d["id"] != p_id:
        print("\nYOU HAVE ENTERED INVALID ID. PLEASE ENTER VALID ID\n")
        user_id()
    print("\nAVAILABLE PRODUCT : \n".center(130))
    userDisplayMenuWindow()

########## CANCEL ORDER###############
def cancelOrder():
    found = False
    temp = []
    order_id = input("                                              ENTER THE ORDER ID : ")
    for d in shopping:
        found = d["id"] == order_id
        if found != True:
            temp.append(d)
    if len(temp) == d:
        print(f'{order_id} IS NOT FOUND'.center(130))
    else:
        print(f'{order_id} IS REMOVED FROM THE PLACED ORDER'.center(130))

############ USER OPTTION#############
        
def userChoiceOptions():
    choice = int(input("                                              PLEASE ENTER USER CHOICE : "))
    if choice == 1:
        userDisplayMenuWindow()
        print()
        print("="*130)
        print()
        userLoginWindow()
        print()
        print("="*130)
        print()
        userChoiceOptions()
    elif choice == 2:
        placeOrder()
        print()
        print("="*130)
        print()
        userLoginWindow()
        print()
        print("="*130)
        print()
        userChoiceOptions()
    elif choice == 3:
        cancelOrder()
        print()
        print("="*130)
        print()
        userLoginWindow()
        print()
        print("="*130)
        print()
        userChoiceOptions()
    elif choice == 4:
        logoutwindow()
    else:
        print("INVALID CHOICE. PLEASE ENTER VALID CHOICE ".center(130))

###############  QUIT   ############
    
def quit():
    print(" ")
    print("="*130)
    print(" ")
    print("THANK YOU".center(130))
    print("ALL KIND OF SMALL OR BULK ORDERS CONTACT OUR E-COMMERCE APPLICATION".center(130))
    print(" ")
    print("="*130)
    print(" ")
    print("THANK YOU FOR USING THIS APPLICATION ".center(130))
    print(" ")
    print("DEVELOPER - ANKIT KUMAR YADAV".center(130))
    print("DEVELOPER - AMAN GUPTA".center(130))
    print("DEVELOPER - AVINASH KUMAR SINGH".center(130))
    print("="*130)

def login():
    print("*"*130)
    print(" ")
    print("E-COMMERENCE TEXT-BASED APPLICATION".center(130))
    print(" ")
    print(" "*9,"DATE:",t_date.day,"/",t_date.month,"/",t_date.year,"                                                                                TIME:",t_time.hour ,":",t_time.minute)
    print(" ")
    print("*"*130)
    print(" ")
    print(" "*62,"1.ADMINISTRATOR")
    print(" "*62,"2.CUSTOMER")
    print(" "*62,"3.QUIT")
    print(" ")
    print(" ")
    tp=input("                                                            ENTER YOUR CHOICE :")
    print(" ")
    #####  ADMIN  #####
    if tp=='1':
        for i in range(3):
            op = input("                                                            ENTER PIN PASSWORD :")
            if(op=="1234"):
                print("CORRECT".center(130))
                adminLoginWindow()
                adminOptions()
                break
            else:
                j=2
                print("                                  INCORRECT PASSWORD",j-i,"CHANCES ARE LEFT ")
                if(j-i==0):
                    print("TRY AGAIN LATER".center(130))
                    break
            
        ##### CUSTOMER  #####
    elif tp=='2':
        for i in range(3):
            op = int(input("                                                            ENTER PIN PASSWORD :"))
            if(op==1234):
                print("CORRECT".center(130))
                userLoginWindow()
                userChoiceOptions()
                break
            else:
                j=2
                print("                                  INCORRECT PASSWORD ",j-i," CHANCES ARE LEFT ")
                if(j-i==0):
                    print("TRY AGAIN LATER".center(130))
                    break
    else:
        quit()

login()
