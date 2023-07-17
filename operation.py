import datetime
import read
import write


# This is the welcome text when we first login
def welcome():
    print("\n")
    print("\n")
    print("-"*113)
    print("\n")
    print("\t \t \t \t  DilliBazar, Kathmandu | Phone No: 9845125893 ")
    print("\n")
    print("\t\t\t Welcome to the system Admin! I hope you have a good day ahead!")
    print("-"*113)
    print("\n")


# This are the question that we will be asked 
def options():       
    print("-"*113)
    print("\t\t\t   Given below are some of the options for you to carryout")
    print("-"*113)
    print("\n")
    print("Press 1 to Sale the laptop to customer.")
    print("Press 2 to Purchase from Manufacture.")
    print("Press 3 to Exit")
    print("\n")
    print("-"*113)
    print("\n")

    print("\n")

#Invalid message
def invalid():
    print("-"*30)
    print("\tInvalid Data")
    print("-"*30)
    print("\n")


# If user enter option no 1
customer_name = []
phone_number = []
def sell():
    #create an list and delared the variable
    Laptop_sold = []
    Laptops = []
    Company = []
    Total_price = 0
    Total_qty = 0
    
    #using the while loop
    selling = True
    while selling == True:

        #Import the Rent.py file and written process by renting process
        valid_id = laptop_vaild_id()
        the_dict = read.dictionary()
        valid_quantity = valid_q(valid_id, the_dict)
        
        #import the some of value in dictionary
        laptop =  the_dict[valid_id][0]
        company = the_dict[valid_id][1]
        price =  the_dict[valid_id][2].replace("$","")
        Total_price = (Total_price + (float(price) * valid_quantity))
        Total_qty = (Total_qty + valid_quantity)
        
        #create a list and append the values in list
        Company.append(company)
        Laptops.append(laptop)
        Laptop_sold.append([Company, Laptops])
        
        #ask the customer again rent or not rent
        ask = True
        while ask == True:
            ask_Q = input("Do you want to buy mor laptop enter the 'Y' or 'N': ").upper()
            print("\n")
            if ask_Q == 'Y':
                break
               
                
            elif ask_Q == 'N':
                print("\n")
                print("-----------------------------------------------------------------------------------------")
                print("For Bill Generation you will have to enter your deatils first: ")
                print("-----------------------------------------------------------------------------------------")
                print("\n")
                customer_name=input("Please enter the name of the Customer: ")
                print("\n")
                phone_number = input ("Please enter the phone number of the Customer: ")
                print("\n")
                print("-----------------------------------------------------------------------------------------")
                print("\n")
                #custom rent bill generated and write in txt file
                bill_one(customer_name, Total_price, Total_qty, Laptop_sold,phone_number)
                write.write_bill_one(customer_name, Total_price, Total_qty, Laptop_sold,phone_number)
                ask = False
                selling = False

            else:
                invalid()


def laptop_vaild_id():
    #call the laptop_details() funcation and display the custom details
    read.laptop_details()
    print("\n")
    ID = True
    while ID == True:
        try:
            valid_lap = int(input("Please enter valid Laptop id: "))
            while valid_lap <= 0 or  valid_lap> len(read.dictionary()):
                print("\n")
                print("-"*113)
                print("\t\t\t    The laptop id",valid_lap,"is not available. ")
                print("-"*113)
                valid_lap = int(input("So, please enter the valid Laptop id: "))
                print("\n")
            
            ID = False
            
        except:
            #dsplay the invalid message
            invalid()
    #print the custom details   
    return valid_lap  


"""Quantity validation of the dictionary"""
#create a funcation and check the quantity valitation or return the quantity
def valid_q(valid_lap,laptop_dictionary):
    available_quantity = int(laptop_dictionary[valid_lap][3])
    QTY = True
    while QTY == True:
        try:
            Quantity = int(input("Please provide the number of quantity of the laptop you want to buy:  "))
            while Quantity <= 0 or Quantity > available_quantity:
                print("\n")
                print("-"*113)
                print("\t\t\t    The laptop quantity",Quantity,"is not available.  ")
                print("-"*113)
                Quantity = int(input("So, please enter the valid laptop quantity: "))
                
            print("\n")
            print("-"*113)
            print("\t\t\t    The laptop quantity",Quantity,"is available.")
            print("-"*113)
            QTY = False
            
        except:
            #import the message file and call the invalid_id() funcation
            invalid()
    #call the text_file_update() funcation
    text_file_update(laptop_dictionary, valid_lap, Quantity)
    return Quantity


#This is the six funcation, which used to updated dictionary values are append by the txt file of the system
def text_file_update(laptop_dictionary, valid_lap, Quantity):
    laptop_dictionary[valid_lap][3] = int(laptop_dictionary[valid_lap][3]) - int(Quantity)
    file = open("laptop_Details.txt","w")
    for value in laptop_dictionary.values():
        file.write(str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3])+","+str(value[4]+","+str(value[5])))
        file.write("\n")
    file.close()
    price = laptop_dictionary[valid_lap][2].replace("$","")
    first_price = (float(price) * Quantity)
    print("The Total price is: ",first_price)
    print("\n")
    return first_price


#create a bill funcation and display the bill details
def bill_one(customer_name, Total_price, Total_qty, Laptop_sold, phone_number):
    Datetime_obj = datetime.datetime.now()
    shipping_cost = 500
    print("-"*113)
    print("\t\t\t                    Bill Details                       ")
    print("-"*113)
    print("\n")
    print("Name of Customer: Mr/Mrs."+customer_name)
    print("Phone Number: "+phone_number)
    print("Total Price (Excluding Shipping Cost): ", Total_price)
    print("Date time of Sold laptops: ",Datetime_obj)
    print("Total laptop quantity: ",Total_qty,"qty") 
    print("\n")  
    print("Laptop's Name: ",Laptop_sold[0][0])
    print("Company Name: ",Laptop_sold[0][1])
    print("\n")
    print("Your Grand Total with shipping cost is: ",Total_price + shipping_cost)
    print("\n")
    print("-"*113)
    print("\n")


# Buy fromthe manufacture
def buy():
    #create an list and delared the variable
    Laptop_buy = []
    Laptops = []
    Company = []
    Total_price = 0
    Total_qty = 0
    
    #using the while loop
    buying = True
    while buying == True:

        #Import the Rent.py file and written process by renting process
        valid_id = laptop_vaild_id()
        the_dict = read.dictionary()
        valid_quantity = valid_qb(valid_id, the_dict)
        
        #import the some of value in dictionary
        laptop =  the_dict[valid_id][0]
        company = the_dict[valid_id][1]
        price =  the_dict[valid_id][2].replace("$","")
        Total_price = (Total_price + (float(price) * valid_quantity))
        Total_qty = (Total_qty + valid_quantity)
        
        #create a list and append the values in list
        Company.append(company)
        Laptops.append(laptop)
        Laptop_buy.append([Company, Laptops])
        
        #ask the customer again rent or not rent
        ask = True
        while ask == True:
            ask_Q = input("Do you want to buy mor laptop enter the 'Y' or 'N': ").upper()
            print("\n")
            if ask_Q == 'Y':
                break
               
                
            elif ask_Q == 'N':
                print("\n")
                print("-----------------------------------------------------------------------------------------")
                print("For Bill Generation you will have to enter your deatils first: ")
                print("-----------------------------------------------------------------------------------------")
                print("\n")
                customer_name=input("Please enter the name of the Customer: ")
                print("\n")
                phone_number = input ("Please enter the phone number of the Customer: ")
                print("\n")
                print("-----------------------------------------------------------------------------------------")
                print("\n")

                #custom rent bill generated and write in txt file
                bill_two(customer_name, Total_price, Total_qty, Laptop_buy,phone_number)
                write.write_bill_two(customer_name, Total_price, Total_qty, Laptop_buy,phone_number)
                ask = False
                buying = False

            else:
                invalid()



def valid_qb(valid_lap,laptop_dictionary):
    available_quantity = int(laptop_dictionary[valid_lap][3])
    QTY = True
    while QTY == True:
        try:
            Quantity = int(input("Please provide the number of quantity of the laptop you want to buy:  "))
            while Quantity <= 0 or Quantity > available_quantity:
                print("\n")
                print("-"*113)
                print("\t\t\t    The laptop quantity",Quantity,"is not available.  ")
                print("-"*113)
                Quantity = int(input("So, please enter the valid custom quantity: "))
                
            print("\n")
            print("-"*113)
            print("\t\t\t    The laptop quantity",Quantity,"is available.")
            print("-"*113)
            QTY = False
            
        except:
            #import the message file and call the invalid_id() funcation
            invalid()
    #call the text_fileb_update() funcation
    text_fileb_update(laptop_dictionary, valid_lap, Quantity)
    return Quantity


#This is the six funcation, which used to updated dictionary values are append by the txt file of the system
def text_fileb_update(laptop_dictionary, valid_lap, Quantity):
    laptop_dictionary[valid_lap][3] = int(laptop_dictionary[valid_lap][3]) + int(Quantity)
    file = open("laptop_Details.txt","w")
    for value in laptop_dictionary.values():
        file.write(str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3])+","+str(value[4]+","+str(value[5])))
        file.write("\n")
    file.close()
    price = laptop_dictionary[valid_lap][2].replace("$","")
    first_price = (float(price) * Quantity)
    print("The Total price is: ",first_price)
    print("\n")
    return first_price


def bill_two(customer_name, Total_price, Total_qty, Laptop_buy, phone_number):
    Datetime_obj = datetime.datetime.now()
    vat = Total_price * 0.13
    grand_total = Total_price + vat

    print("-"*113)
    print("\t\t\t                    Bought Laptop Bill                       ")
    print("-"*113)
    print("\n")
    print("Name of Customer: Mr/Mrs. " + customer_name)
    print("Phone Number: " + phone_number)
    print("Total Laptop Quantity: ", Total_qty, "qty")
    print("Date and Time of Purchase: ", Datetime_obj)
    print("\n")
    print("Laptop Details:")
    print("Laptop Name: ",Laptop_buy[0][0])
    print("Company Name: ",Laptop_buy[0][1])
    print("\n")
    print("Total Price (excluding VAT): ", Total_price)
    print("VAT (13%): ", vat)
    print("Grand Total (including VAT): ", grand_total)
    print("\n")
    print("-"*113)
    print("\n")


# If the user press 3 button
def exit():
    print("\t\t     Thank you for using the system. Have a good day!!       ")
    print("\n")


# If the user enter other number then 1,2,3
def invalid_Options():
    print("\t\t\t-------------------------------------------------------------")
    print("\t\t\t   Invalid input!! Please input the options '1' or '2' or '3'  ")
    print("\t\t\t-------------------------------------------------------------")
    print("\n")

