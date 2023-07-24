import datetime
cart = []

def title():
    print('*'*40)
    print('  Welcome to the Lunar Costume Rental')
    print('*'*40)


def options():
    Option ='''
Select a desirable option:
(1) || Press 1 to rent a costume.
(2) || Press 2 to return a costume.
(3) || Press 3 to exit.
    '''
    print(Option)


def get_Costume_Details():
    file = open("costumes.txt","r")
    data = file.readlines()
    file.close()
    return data


def get_Costume_Dictionary(Costume_Details):
    data = {}
    for index in range(len(Costume_Details)):
        data[index+1] = Costume_Details[index].replace("\n","").split(",")
    return data


def display_Costume_Details():
    Costume_Details = get_Costume_Details()
    main_data = get_Costume_Dictionary(Costume_Details)
    print("-"*70)
    print("S.No","\t","Costume Name","\t","Manufacturer/Brand","\t","Price","\t  ","Quantity")
    print("-"*70)
    for key, value in main_data.items():
        try:
            print(key,"\t",value[0],"\t",value[1],"\t ",value[2],"\t    ",value[3])
        except IndexError:
            pass


def get_valid_S_No(main_data):
    valid_data = False
    while valid_data == False:
        try:
            print()
            SNo = int(input("Enter Serial Number: "))
            print()
            if SNo > 0 and SNo <= len(main_data):
                valid_data = True
                return SNo
            else:
                print("No costume with that serial number exists in the rental!, please select\ncostumes from the above table only ")
        except:
            print()
            print("Please enter numeric values only!!!")


def get_valid_quantity_rent(main_data, SNo):
    valid_quantity = False
    while valid_quantity == False:
        try:
            Quantity = int(input("How many of this do you want to rent?: "))
            if Quantity > 0 and Quantity <= int(main_data[SNo][3]):
                valid_quantity = True
                return Quantity
            else:
                print()
                print("Invalid input!!\nThe entered quantity exceeded the actual available quantity of the costume.\nPlease enter a valid quantity.")
                print()
        except:
            print()
            print("Please enter numeric values only!!!")
            print()

def get_valid_quantity_return(main_data, SNo):
    valid_quantity = False
    while valid_quantity == False:
        try:
            Quantity = int(input("How many of this do you want to return?: "))
            print()
            if Quantity > 0:
                valid_quantity = True
                return Quantity
            else:
                print()
                print("Invalid input!!")
                print()
        except:
            print()
            print("Please enter numeric values only!!!")
            print()
            

def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    date = year+":"+month+":"+day
    return date


def time():
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    time = str(hour+minute+second)
    return time


def rent_bill(main_data):
    total = []
    print()
    name = " "
    while True:

        name = input("Rented By: ")
        print()      
        if name:
            break
        
    contact = " "
    while True:
        contact = input("Contact number/E-mail: ")
        print()
        if contact:
            break
        
    print()
    print("RENT BILL:")
    print()
    print("Rented By: "+name+"\t\t\t" + "Date:" ,date())
    print()
    print("Contact/E-mail: " + contact)
    print()
    print("-"*70)
    print("S.No","\t","Costume Name","\t","Manufacturer/Brand","\t","Price","\t  ","Quantity")
    print("-"*70)
    for index in range(len(cart)):
        c_id = int(cart[index][0])
        c_quantity = int(cart[index][1])
        c_name = main_data[c_id][0]
        c_brand = main_data[c_id][1]
        c_price = int(main_data[c_id][2].replace("$",""))
        c_total = (c_price)*(c_quantity) 
        total.append(c_total)
        print(str(index+1)+"\t"+c_name+"\t"+c_brand+"\t\t  "+str(c_price)+"\t      "+str(c_quantity))
  
    print("-"*70)
    print(" "*46 + "Total Amount: " + "\t" + "$" + str(sum(total)))     
    print()
    print(" "*24 + "!!!Thankyou for renting!!!")
    print()

    file = open(str(name)+str(time())+".txt", "w")
    file.write("BILL:")
    file.write("\n" + "Rented By: "+str(name)+"\t\t\t\t\t\t" + "Date: " + str(date()))
    file.write(("\n" + "Contact/E-mail: " + contact))
    file.write("\n" + "-"*70)
    file.write("\n" + "S.No"+"\t"+"Costume Name"+"\t"+"Manufacturer/Brand"+"\t"+"Price"+"\t  "+"Quantity")
    file.write("\n" + "-"*70)
    for index in range(len(cart)):
        c_id = int(cart[index][0])
        c_quantity = int(cart[index][1])
        c_name = main_data[c_id][0]
        c_brand = main_data[c_id][1]
        c_price = int(main_data[c_id][2].replace("$",""))
        c_total = (c_price)*(c_quantity)
        total.append(c_total)
        file.write("\n" + str(index+1)+"\t"+c_name+"\t"+c_brand+"\t\t  "+str(c_price)+"\t      "+str(c_quantity)) 
    file.write("\n" + "-"*70)
    file.write("\n" + " "*46 + "Total Amount: " + "\t" + "$" + str(sum(total)))  
    file.close()
    
    cart.clear()
    total.clear()

def return_bill(main_data):
    print()
    loop = True
    while loop == True:
        try:
            lateDays = int(input("Enter the number of late days: "))
            loop = False
            break
        except:
            print()
            print("Please enter numeric values only!!!")
            print()
    
    print()
    
    name = " "
    while True:
        name = input("Returned By: ")
        print()      
        if name:
            break
        
    contact = " "
    while True:
        contact = input("Contact number/E-mail: ")
        print()
        if contact:
            break
        
    print("RETURN BILL:")
    print()
    print("Returned By: "+name+"\t\t\t\t\t\t" + "Date:", date())
    print()
    print("Contact/E-mail: " + contact)
    print()
    print("-"*70)
    print("S.No","\t","Costume Name","\t","Manufacturer/Brand","\t","Price","\t  ","Quantity")
    print("-"*70)
    for index in range(len(cart)):
        c_id = int(cart[index][0])
        c_quantity = int(cart[index][1])
        c_name = main_data[c_id][0]
        c_brand = main_data[c_id][1]
        c_price = int(main_data[c_id][2].replace("$","")) 
        print(str(index+1)+"\t"+c_name+"\t"+c_brand+"\t\t  "+str(c_price)+"\t      "+str(c_quantity))
    fee = lateDays*20
    print("-"*70)
    print(" "*46 + "Late Fee: " + "\t" + "$" + str(fee))     
    print()
    print(" "*24 + "!!!Thankyou for returning!!!")
    print()


    file = open(str(name)+str(time())+".txt", "w")
    file.write("RETURN BILL:")
    file.write("\n" + "Returned By: "+str(name)+"\t\t\t\t\t\t" + "Date: " + str(date()))
    file.write(("\n" + "Contact/E-mail: " + contact))
    file.write("\n" + "-"*70)
    file.write("\n" + "S.No"+"\t"+"Costume Name"+"\t"+"Manufacturer/Brand"+"\t"+"Price"+"\t  "+"Quantity")
    file.write("\n" + "-"*70)
    for index in range(len(cart)):
        c_id = int(cart[index][0])
        c_quantity = int(cart[index][1])
        c_name = main_data[c_id][0]
        c_brand = main_data[c_id][1]
        c_price = int(main_data[c_id][2].replace("$",""))
        file.write("\n" + str(index+1)+"\t"+c_name+"\t"+c_brand+"\t\t  "+str(c_price)+"\t      "+str(c_quantity)) 
    file.write("\n" + "-"*70)
    file.write("\n" + " "*46 + "Late Fee: " + "\t" + "$" + str(fee))  
    file.close()
                    

def rent_costume():
    loop = True
    while loop == True:
        print()
        print('Lets rent a costume!!')
        
        Costume_Details = get_Costume_Details()
        main_data = get_Costume_Dictionary(Costume_Details)

        display_Costume_Details()

        SNo = get_valid_S_No(main_data)

        if (main_data[SNo][3]) > "0":

            Quantity = get_valid_quantity_rent(main_data, SNo)
            cart.append([SNo, Quantity])

            main_data[SNo][3] = str(int(main_data[SNo][3])-Quantity)

            file = open("costumes.txt","w")
            for value in main_data.values():
                try:
                    write_data = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
                    file.write(write_data)
                except:
                    pass
            file.close()       

            print()   
            rentMore = input("Do you want to rent more? ")
            loop = True
            while loop == True:  
                if rentMore.lower() == "yes":
                    print()
                    print("Lets rent more!!!")
                    Costume_Details = get_Costume_Details()
                    main_data = get_Costume_Dictionary(Costume_Details)

                    display_Costume_Details()

                    SNo = get_valid_S_No(main_data)
                    if (main_data[SNo][3]) > "0":
                        
                        Quantity = get_valid_quantity_rent(main_data, SNo)
                        cart.append([SNo, Quantity])

                        main_data[SNo][3] = str(int(main_data[SNo][3])-Quantity)

                        file = open("costumes.txt","w")
                        for value in main_data.values():
                            write_data = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
                            file.write(write_data)
                        file.close()
                                
                        print()
                        rentMore = input("Do you want to rent more? ")
                    else:
                        print("It seems that we are out of stock for that costume right now!!!/nPlease choose other available costumes.")
                        
                elif rentMore.lower() == "no":
                    rent_bill(main_data)
                    break
                
                else:
                    print()
                    print("Please enter either yes or no")
                    print()
                    rentMore = input("Do you want to rent more? ")
            break
        else:
            print("It seems that we are out of stock for that costume right now!!!\nPlease choose other available costumes.")

    display_Costume_Details()

    print()
    print("Your costume has been rented!!!")
    options()


def return_costume():
    print()
    print('Lets return a costume!!')
    Costume_Details = get_Costume_Details()
    main_data = get_Costume_Dictionary(Costume_Details)

    display_Costume_Details()

    SNo = get_valid_S_No(main_data)

    Quantity = get_valid_quantity_return(main_data, SNo)
    cart.append([SNo, Quantity])

    main_data[SNo][3] = str(int(main_data[SNo][3])+ Quantity)

    file = open("costumes.txt","w")
    for value in main_data.values():
        write_data = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
        file.write(write_data)
    file.close()

    lateReturn = input("Is the return on time? ")
    loop = True
    while loop == True:
        if lateReturn.lower() == "yes":
            print()
            while True:
                name = input("Returned By: ")
                print()      
                if name:
                    break
            contact = " "
            while True:
                contact = input("Contact number/E-mail: ")
                print()
                if contact:
                    break

            print("RETURN BILL:")
            print()
            print("Returned By: "+name+"\t\t\t" + "Date:", date())
            print()
            print("Contact/E-mail: " + contact)
            print()
            print("-"*70)
            print("S.No","\t","Costume Name","\t","Manufacturer/Brand","\t","Price","\t  ","Quantity")
            print("-"*70)
            for index in range(len(cart)):
                c_id = int(cart[index][0])
                c_quantity = int(cart[index][1])
                c_name = main_data[c_id][0]
                c_brand = main_data[c_id][1]
                c_price = int(main_data[c_id][2].replace("$","")) 
                print(str(index+1)+"\t"+c_name+"\t"+c_brand+"\t\t  "+str(c_price)+"\t      "+str(c_quantity))
            print("-"*70)
            print(" "*46 + "Late Fee: " + "\t" + "$" + "0")     
            print()
            print(" "*24 + "!!!Thankyou for returning!!!")
            print()
            break
                
        elif lateReturn.lower() == "no":
           return_bill(main_data)
           break

        else:
            print()
            print("Please enter either yes or no")
            print()
            lateReturn = input("Is the return on time: ")

    
    display_Costume_Details()

    print()
    print("Your costume has been returned!!!")
    options()


def exit_system():
    print()
    print(" "*19+ "!!!Thank you for using our application!!!")
 

