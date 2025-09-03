customers = ["robin gonzales", "diin", "dimor", "samuel", "robin arnimo", "ilyass", "robert"]
while True:
    menu_customers = int(input("Menu: \n1. Show all customers \n2. Add a new customer \n3. Remove a customer \n4. Search for a customer \n5. Exit program \nType number 1-5: "))

    if menu_customers == 1:
        for customer in customers:
            print(customer)
        enter = input("Press Enter to continue: ")
    elif menu_customers == 2:
        new_customer = input("Write the new customers name: ")
        customers.append(new_customer)
        print("Updated customer list: ")
        for customer in customers:
            print(customer)
        enter = input("Press Enter to continue: ")
    elif menu_customers == 3:
        for index, customer in enumerate(customers):
            print(f"{index}, {customer}")
        remove_customer = int(input("Write the name of the customer you wanna remove: "))
        customers.pop(remove_customer)
        print("Updated customer list: ")
        for customer in customers:
            print(customer)
        enter = input("Press Enter to continue: ")
    elif menu_customers == 4:
        search_result = []
        search = input("Write the name of the customer you want to search up: ").lower()
        for customer in customers:
            if search in customer:
                search_result.append(customer) 
        
        result_string = "We found the following persons for your search: "
        for result in search_result:
            result_string += f"{result}, "

        
        if len(search_result) == 0:
            print("No customers found")
        else:
            print(result_string)
        enter = input("Press Enter to continue: ")
        

    elif menu_customers == 5:
        break 