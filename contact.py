

contacts = {}

while True:
    print("----------------------WECOME TO CONTACT BOOK APP------------------\n")
    print("1. Create Contact\n")
    print("2. View Contact\n")
    print("3. Update Contact\n")
    print("4. Delete Contact\n")
    print("5. Count Contact\n")
    print("6. Exit\n")


    choice = input("Enter Your Choice = ")

    if choice =='1':
        name = input("Enter  Name : ")
        if name in contacts:
            print(f" Contact Name {name} is already exist!!")
        else:
            age = input("Enter age")
            email = input("Enter email")
            phone = input("Enter Mobile number")
            contacts[name] = {'age': int(age),'phone': phone , 'email' : email}
            print(f"Contact name {name} has been created successfully")
    elif choice == '2':
        name = input("Enter Contact  name to view :")
        if name in contacts:
            contact = contacts[name]
            print(f"Name : {name} , Age : {age} , Mobile number : {phone} Email : {email}")

        else:
            print("Contact not Found")


    elif choice == '3':
        name = input("Enter Contact name to Update : ")
        if name in contacts:
            age = input("Enter updated age")
            email = input("Enter updated email")
            phone = input("Enter updated Mobile number")
            contacts[name] = {'age' : age , 'email' : email , 'phone' : phone } 
        else:
            print("Contact not found")

    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully")
        else:
            print("Contact not found")

    elif choice =='5':
        print(f"Total Number Of contacts :{len(contacts)}")
    
    elif choice == '6':
        print("Thank You........closing program ")
        break

    else:
        print("Invalid input")





    