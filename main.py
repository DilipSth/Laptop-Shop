""" This is the main python file. import the operation. There are three options 1, 2, and 3. In this file are used in while loop and start the program. when user input the valid data the program is run in the system. The admin input 1 option then going to the selling process and
run the sell process but if admin input the 2 option then go to the buying process but user input the 3 option the exit the system and display the some of message"""
import operation

# This is the welcome text when we first login
operation.welcome()


#Asking the user with options
loop = True

while loop == True:
    # This are the question that we will be asked 
    operation.options() 

    option = False
    while option == False:
        try:
            user_input = int(input("Enter an option: "))
            option = True
        except:
            operation.invalid()
        
    #This is the selling laptop process
    if user_input == 1:
        operation.sell()

    #This is the laptop buying process
    elif user_input == 2:
        operation.buy()
    
    elif user_input == 3:
        operation.exit()
        loop = False
        option = False

    else:
        operation.invalid_Options()
        option = False
