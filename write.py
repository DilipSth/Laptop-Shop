import operation
import datetime

#create a bill funcation and display the bill details
def write_bill_one(customer_name, Total_price, Total_qty, Laptop_sold, phone_number):
    Datetime_obj = datetime.datetime.now()
    shipping_cost = 500

    file = open("laptop_bill.txt","w")
    file.write("-"*50+"\n")
    file.write("\t\t  Bill Details  \n")
    file.write("-"*50+"\n")
    file.write("\n")
    file.write("Name of Customer: Mr/Mrs."+str(customer_name)+"\n")
    file.write("Phone Number: "+str(phone_number)+"\n")
    file.write("Date time of sold laptops: "+str(Datetime_obj)+"\n")
    file.write("Total laptop quantity: "+str(Total_qty)+ "qty\n")  
    file.write("Total Price (Excluding Shipping Cost): "+str(Total_price)+"\n")
    file.write("Laptop's Name: "+str(Laptop_sold[0][0])+"\n")
    file.write("Company Name: "+str(Laptop_sold[0][1])+"\n")
    file.write("\n")
    file.write("Your Grand Total with shipping cost is: "+str(Total_price + shipping_cost)+"\n")
    file.write("\n")
    file.write("-"*50)
    file.write("\n")

#create a bill funcation and display the bill details of purchase laptop
def write_bill_two(customer_name, Total_price, Total_qty, Laptop_sold, phone_number):
    Datetime_obj = datetime.datetime.now()
    vat = Total_price * 0.13
    grand_total = Total_price + vat

    file = open("bought_laptop_bill.txt", "w")
    file.write("-"*113 + "\n")
    file.write("\t\t\t                    Bought Laptop Bill                       \n")
    file.write("-"*113 + "\n")
    file.write("\n")
    file.write("Name of Customer: Mr/Mrs. " + customer_name + "\n")
    file.write("Phone Number: " + phone_number + "\n")
    file.write("Total Laptop Quantity: " + str(Total_qty) + " qty" + "\n")
    file.write("Date and Time of Purchase: " + str(Datetime_obj) + "\n")
    file.write("\n")
    file.write("Laptop Details:\n")
    file.write("Laptop Name: " + str(Laptop_sold[0][0]) + "\n")
    file.write("Company Name: " + str(Laptop_sold[0][1]) + "\n")
    file.write("\n")
    file.write("Total Price (excluding VAT): " + str(Total_price) + "\n")
    file.write("VAT (13%): " + str(vat) + "\n")
    file.write("Grand Total (including VAT): " + str(grand_total) + "\n")
    file.write("\n")
    file.write("-"*113 + "\n")
    file.write("\n")
