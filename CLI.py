import db_manager as DBM, time
try:
    while True:
        print(r" ______   ______   ______")
        print(r"/  ____| |  ____| /  __  \ ")
        print(r"|  |  __ |  |__   |  |  | |")
        print(r"|  | |_ | |   __| |  |  | |")
        print(r"|  |__| | |  |____|  |__| |")
        print(r" \______| |_______|\______/")
        print("Welcome to GEO ID")
        print("GEO ID v1.0")
        print("1. Register a user")
        print("2. Remove a user")
        print("3. View all users")
        print("4. Add flag")
        print("5. View user flags")
        print("6. Remove flag")
        print("input quit to exit")
        
        choice = input("Enter your choice (1-6): ").lower()
        
        if choice == "1":
            print("Running registration")
            print("Input menu to go back")
            while True:
                name_input = input("Enter a name too register: ")
                if name_input.lower() == "menu":
                    print("Reterning to menu...")
                    break
                result_message = DBM.register_user(name_input)
                print(result_message)
        
        elif choice == "2":
            target_id = input("Input user ID Remove: ")
            result_msg = DBM.remove_user(target_id)
            
            print(result_msg)
        
        elif choice == "3":
            users_output = DBM.getusers()
            print(users_output)
            input("\nPress any key to continue...")
        
        elif choice == "4":
            target_id = input("Input user ID to add flag: ")
            flag_text = input("Input flag to add: ")
            result_msg = DBM.addflag(target_id, flag_text)
            print(result_msg)

        
        elif choice == "5":
            target_id = input("Input user ID to view flags: ")
            flags_output = DBM.get_user_flags(target_id)
            if isinstance(flags_output, list):
                if flags_output:
                    print(f"Flags for user ID '{target_id}': {', '.join(flags_output)}")
                else:
                    print(f"No flags found for user ID '{target_id}'.")
            else:
                print(flags_output)
            input("\nPress any key to continue...")
    
        elif choice == "6":
            target_id = input("Input user ID to remove flag: ")
            flag_text = input("Input flag to remove: ")
            result_msg = DBM.remove_flag(target_id, flag_text)
            print(result_msg)

        elif choice == "quit":
            print("exiting program good bye")
            time.sleep(0.5)
            break
        else: 
            print("Invalid choice please pick 1, 2, 3, 4, 5, 6 or say quit to exit.")
except Exception as e:
    print(f"\nAn error occurred: {e}")
finally:
    input("\nPress Enter to exit... (This will be removed in future versions kept in for debugging purposes)")