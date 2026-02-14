
print("---WELCOME---")
try:
    def main():
        user_input = str(int(input("enter your phone number: ")))
        user_input_name = input("enter the owners name: ")
        save = input("do you want to be save this number with this name??(y/n): ").lower()

        if save == 'y':
            with open("text.txt" , "a") as file:
                file.write (user_input_name + ":" + user_input + "\n")
            
                print(f"SAVED  {user_input_name} has {user_input} number ")
                contact_search = input("do you want to search any number in your contacts?? (y/n): ").lower()
                if contact_search == 'y':
                    with open("text.txt" , "r") as data:
                        contact = data.read()
                        contact_name = input("ENTER THE NAME FOR SEARCHING: ")
                        if contact_name in contact:
                            print(f'FOUND!! it is {contact}')
                        else: print("NOT FOUND!!")
    main()
except ValueError:
    print("INVALID!!")

