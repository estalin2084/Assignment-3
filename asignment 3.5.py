
meals_price = {
    "1": {
        "Name": "Poutine",
        "Price": 10.99, },
    "2": {
        "Name": "French Fries",
        "Price": 5.99, },
    "3": {
        "Name": "Cheese Burger",
        "Price": 13.99, },
    "4": {
        "Name": "Pumpkin Pie",
        "Price": 7.99, },
    "5": {
        "Name": "BLT Sandwich",
        "Price": 9.99, },
    "6": {
        "Name": "Chicken Salad",
        "Price": 12.99, }
}


order_data = {

}

customer_Data = {
    "FirstName": "",
    "LastName": "",
    "Address": "",
    "Unit": "",
    "City": "",
    "Province": "",
    "PostalCode": "",
    "PhoneNumber": "",
    "Delivery": False,
    "DeliveryCharge": 0.00,
    "Instructions": "",
    "Student": False,
    "Tips": "",
    "HST": "",

}

canada_provinces = {
    "AB" : "ALBERTA",
    "BC" : "BRITISH COLUMBIA",
    "NB" : "NEW BRUNSWICK",
    "NL" : "NEWFOUNDLAND AND LABRADOR",
    "NS" : "NOVA SCOTIA",
    "NT" : "NORTHWEST TERRITORIES",
    "NU" : "NUNAVUT",
    "MB" : "MANITOBA",
    "ON" : "ONTARIO",
    "PE" : "PRINCE EDWARD ISLAND",
    "QC" : "QUEBEC",
    "YK" : "YUKON"

}

def discount(): #this function calculates all the discounts and returns the percentages and quantiy in money.

    global percentage #this variable is set to be used globally
    global applied_disc #this variable is set to be used globally
    student_discount = .9 #this takes the .9% of the total
    global applied_student_disc #this applies the 10% to the student


    if total() < 100: #this calculates the 5% plus a 10% more in case the customer is a student
        total_w_disc = total() * 0.95
        percentage = "5%"
        applied_disc = total() *0.05 
        if customer_Data["Student"] == True: 
            applied_student_disc = total_w_disc * .1
            total_w_disc *= student_discount
        return total_w_disc
    
    elif total() >= 100 and total () <500: #this calculates the 10% plus a 10% more in case the customer is a student
        total_w_disc = total() * 0.90
        percentage = "10%"
        applied_disc = total() *0.10
        if customer_Data["Student"] == True:
            applied_student_disc = total_w_disc * .1
            total_w_disc *= student_discount
        return total_w_disc
    elif total() > 500: #this calculates the 15% plus a 10% more in case the customer is a student
        total_w_disc = total() * 0.85
        percentage = "15%"
        applied_disc = total() *0.15
        if customer_Data["Student"] == True:
            applied_student_disc = total_w_disc * .1
            total_w_disc *= student_discount
        return total_w_disc


def total():
    for i, k in enumerate(order_data):
        subtotal = order_data[k]["Price"]*order_data[k]["Quantity"] if i==0 else order_data[k]["Price"]*order_data[k]["Quantity"]+subtotal
        return  subtotal

def deli_or_pickup(customer_Data):  # This function calculates wheter the order will be delivered or pick up and calculates the delivery fee.
    delivery = 0
    while delivery not in range(1, 2):  # This while evaluates that the answer for choosing delivery is either 1 or 2. And displays a message if the wrong input is entered
        delivery = int(input('Please indicate if your order is pick up or delivery: 1) Delivery 2) Pick Up: '))
        if delivery == 1:
            customer_Data["Delivery"] = True
            customer_Data["Instructions"] = input("Please enter your delivery instructions: ")
            if total() > 30:
                customer_Data["DeliveryCharge"] = 0
                print("Your order is free or delivery charge!")
            else:
                customer_Data["DeliveryCharge"] = 5
                print("Your order has a 5$ delivery fee")
            tips(customer_Data)

        elif delivery == 2:
            customer_Data["Delivery"] = False
            break
        else:
            print("Please write 1 or 2 only! ")

def tips(customer_Data):
    tip = 0
    while tip not in range(1, 4):
        tip = int(input('Please select your tip: 1) 10% 2) 15% 3) 20%: '))
        if tip == 1:
            customer_Data["Tips"] = total() * 0.10
        elif tip == 2:
            customer_Data["Tips"] = total() * 0.15
        elif tip == 3:
            customer_Data["Tips"] = total() * 0.20
        else:
            print("Please only write numbers 1 to 3!")

def postalcodechecker(postalCode):
    try:
        postal = [i for i in postalCode]
        numbers = [postal[1], postal[4], postal[6]]
        letters = [postal[0], postal[2], postal[5]]
    except:
        return False
    else:
        return True if ("".join(numbers).isdigit() == True and "".join(letters).isalpha() == True and postal[3] == " ") else False
def addresschecker(address):
    a = address.split()
    return True if a[0].isdigit()==True and a[1].isalpha()==True and a[-1].upper() in streets else False

streets = ["STREET", "ROAD", "AVENUE", "FREEWAY", "HIGHWAY", "BOULEVARD", "DRIVE", "ST", "DR", "RD", "AVE"]

print("Welcome to Arnold Store II")
print("")
print("Please enter customer data")
print("")

while True:
    name = list(map(str, input("Please enter the customer's full name: ").split(" "))) #Input for customer's name, saves first name and last name within different variables
    customer_Data["FirstName"] = name[0]
    customer_Data["LastName"] = name[-1]
    customer_Data["Address"] = input("Please enter the customer's full address: ")
    while addresschecker(customer_Data["Address"])==False:
        customer_Data["Address"] = input("Please enter a valid address: ")
    customer_Data["Unit"] = input("Please enter the unit number: ")#This and the following inputs are inputs for customer's information
    customer_Data["City"] = input("Please enter the customer's city: ")
    customer_Data["Province"] = input("Please enter customer's province: ").upper()
    while customer_Data["Province"] not in canada_provinces.keys() and customer_Data["Province"] not in canada_provinces.values():
        customer_Data["Province"] = input("Please enter the province: ").upper()
    customer_Data["PostalCode"] = input("Please enter the customer's postal code. Use the following format [B1B 2C2]: ")
    while postalcodechecker(customer_Data["PostalCode"]) == False:
        customer_Data["PostalCode"] = input("Please enter the customer's postal code. Use the following format [B1B 3B3]: ")
    customer_Data["PhoneNumber"] = str(input("Please enter the customer's phone number: ")) 
    while customer_Data["PhoneNumber"].isdigit == False or len(customer_Data["PhoneNumber"]) != 10:
        customer_Data["PhoneNumber"] = str(input("Please a valid phone number: ")) 

    print("")
    print("Please choose your favorite dish")

    y = False
    while y == False:

        x = False

        while x == False:
            for k in meals_price.keys():
                print("{} - {} -  ${}".format(k, meals_price[k]["Name"], meals_price[k]["Price"]))

            meal_selection = input("Please select your food: ")
            while meal_selection not in meals_price.keys():
                print("Your selection does not exist")
                meal_selection = input("Please select your food: ")

            data = False
            while not data:

                try:
                    meal_quantity = int(input("How many do you wish?: "))
                except:
                    print("Please enter a valid value!")
                else:
                    data = True

            if meal_selection not in order_data:
                order_data[meal_selection] = {"Name": meals_price[meal_selection]["Name"],
                                            "Price": meals_price[meal_selection]["Price"], "Quantity": meal_quantity}


            elif meal_selection in order_data:
                order_data[meal_selection]["Quantity"] = meal_quantity + order_data[meal_selection]["Quantity"]

            add_more_food = input("Do you want add more food? [Yes/No]")
            while add_more_food.upper() != "YES" and add_more_food.upper() != "Y" and add_more_food.upper() != "NO" and add_more_food.upper() != "N":
                add_more_food = input("Do you want add more food? [Yes/No]")

            if add_more_food.upper() == "YES" or add_more_food.upper() == "Y":
                continue
            else:
                break

        for k in order_data.keys():
            print(order_data[k]["Quantity"], order_data[k]["Name"], order_data[k]["Price"], "each meal")

        confirmation = input("Please confirm your order [Yes/No]: ")
        while confirmation.upper() != "YES" and confirmation.upper() != "Y" and confirmation.upper() != "NO" and confirmation.upper() != "N":
            confirmation = input("Please confirm your order? [Yes/No]")

        if confirmation.upper() == "YES" or confirmation.upper() == "Y":
            break
        else:
            order_data.clear()
            continue

    student = input("Are you a student? [Yes/No]: ")
    while student.upper() != "YES" and student.upper() != "Y" and student.upper() != "NO" and student.upper() != "N":
        student = input("Are you a student? [Yes/No]:")

    if student.upper() == "YES" or student.upper() == "Y":
        customer_Data["Student"] = True
        print("You have a ten percent discount!!")

    else:
        customer_Data["Student"] = False
        print("You don't have student discount!! ")

    deli_or_pickup(customer_Data)
    discount()
    print("")

    print("{0} {1}.".format(customer_Data["FirstName"], customer_Data["LastName"]))  # this prints the customer first and last name before the receipt
    print("{0}.".format(customer_Data["PhoneNumber"]))   # prints the customer phone number
    if customer_Data["Delivery"] == True:  # if delivery is true it prints the customer address.
        print("{0}, {1}.".format(customer_Data["Address"], customer_Data["Unit"]))  # this print the address of the customer
        print("{0}, {1}, {2}. ".format(customer_Data["City"], customer_Data["Province"], customer_Data["PostalCode"]))  # this print the address of the customer
        print("Delivery instructions: " + "\t" "{0}.".format(customer_Data["Instructions"]))  # if delivery is true it prints the delivery instructions
    print(" ")  # this creates an space between the customer info and the recepit

    print("-" * 75)  # this creates the format of my recepit and the first line between the information in it
    print("Order {:>15s} Quantity {:>10s} Item Price {:>10s} Total {} ".format("", "", "", ""))  # this adds the headings of the recepit
    print("-" * 75)  # this creates the format of my recepit and the second line
    for k in order_data.keys():
        print(("{}").format(order_data[k]["Name"]), (("{:>15} \t {:>12}${:.2f}  {:>12}${:.2f} ".format(order_data[k]["Quantity"],"", order_data[k]["Price"], "", total()))))  # this prints the name, quantity, the price and the total
    print("Discount", percentage, ("{:>53}${:.2f}").format("", applied_disc))  # this prints the percentage discounted of the order
    if customer_Data["Student"] == True:  # if the student status is true it will print the 10% aditional discount
        print("10%" " Student savings", ("{:>43}- ${:.2f}").format("", applied_student_disc))  # if the student status is true it will print the 10% aditional discount
    print(("{:>45}Subtotal{:>12}${:.2f}").format("", "", discount()))  # this prints the subtotal of the recepit
    print(("{:>45}HST 13%{:>13}${:.2f}").format("", "", discount() * .13))  # this prints the tax
    if customer_Data['Delivery'] == True:  # If deliver is true it prints the deliver fee and tips along with the grand total
        print(("{:>45}Delivery Fee {:>7}${:.2f}").format("", "", customer_Data["DeliveryCharge"]))
        print(("{:>45}Tips {:>15}${:.2f}").format("", "", customer_Data["Tips"]))
        print(("{:>45}Grand Total {:>8}${:.2f}").format("", "", discount() * 1.13 + customer_Data["DeliveryCharge"] + float(customer_Data["Tips"]), "CAD"))  # this prints the grand total of the recepit
    else:  # prints the grand total without delivery fee and tips.
        print(("{:>45}Grand Total {:>10}${:.2f}").format("", "", discount() * 1.13))
    print("-" * 75)  # this creates the format of my recepit and is the last line

    

    receipt = open(r"C:\Users\Estalin Pena\Desktop\Programming-_Tasks\Assignment-3\receipt.txt", "w")
    receipt.write("-" * 75)  # this creates the format of my recepit and the first line between the information in it
    receipt.write("Order {:>15s} Quantity {:>10s} Item Price {:>10s} Total {} ".format("", "", "", ""))  # this adds the headings of the recepit
    receipt.write("\n-" * 75)  # this creates the format of my recepit and the second line
    for k in order_data.keys():
        receipt.write(("\n{}").format(order_data[k]["Name"]) + (("{:>15} \t {:>12}${:.2f} {:>12}${:.2f} ".format(order_data[k]["Quantity"],"", order_data[k]["Price"], "", total()))))  # this prints the name, quantity, the price and the total
    receipt.write("Discount" + percentage + ("\n{:>32s}${:.2f}").format("", applied_disc))  # this prints the percentage discounted of the order
    if customer_Data["Student"] == True:  # if the student status is true it will print the 10% aditional discount
        receipt.write("10%" " Student savings" + ("\n{:>43}- ${:.2f}").format("", applied_student_disc))  # if the student status is true it will print the 10% aditional discount
    receipt.write(("\n{:>45}Subtotal{:>20s}${:.2f}").format("", "", discount()))  # this prints the subtotal of the recepit
    receipt.write(("\n{:>45}HST 13%{:>20}${:.2f}").format("", "", discount() * .13))  # this prints the tax
    if customer_Data["Delivery"] == True:  # If deliver is true it prints the deliver fee and tips along with the grand total
        receipt.write(("\n{:>35}Delivery Fee {:>20}${:.2f}").format("", "", customer_Data["DeliveryCharge"]))
        receipt.write(("\n{:>35}Tips {:>20}${:.2f}").format("", "", customer_Data["Tips"]))
        receipt.write(("\n{:>35}Grand Total {:>20}${:.2f}").format("", "", discount() * 1.13 + customer_Data["DeliveryCharge"] + float(customer_Data["Tips"]), "CAD"))  # this prints the grand total of the recepit
    else:  # prints the grand total without delivery fee and tips.
        receipt.write(("\n{:>35}Grand Total {:>20}${:.2f}").format("", "", discount() * 1.13))
    receipt.write("\n-" * 75)  # this creates the format of my recepit and is the last line
    receipt.close()
    break