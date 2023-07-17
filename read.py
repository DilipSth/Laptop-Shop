import operation

#create a funcation open the txt file and show the babular funcation
def laptop_details():
    print("                                    Sun Electronics                                         ")
    print("-"*90)
    print("ID    \tCompany Name \tLaptop Name \tPrice \tQuality     Processor       GPU")
    print("-"*90)
    file = open("laptop_Details.txt","r")
    values = 1
    for line in file:
        print(values,"\t"+line.replace(",", "\t"))
        values = values + 1
    print("-"*90)
    file.close()

def dictionary():#create a dectionary funcation and opent the txt or read; initialize the new custom dictionary
    file = open("laptop_Details.txt","r")
    laptop_dictionary = {}
    lap_Id = 1
    for line in file:
        line = line.replace("\n", "")
        laptop_dictionary.update({lap_Id: line.split(",")})
        lap_Id = lap_Id + 1
    file.close()
    return laptop_dictionary