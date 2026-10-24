import db_manager, time
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
        print("2. View all users")
        print("3. Add flag")
        print("4. To remove a user")
        print("input quit to exit")
        choice = input("Enter your choice (1-4): ").lower()
        if choice == "1":
            print("Running registration")
            print("Input menu to go back")
            while True:
                name_input = input("Enter a name too register: ")
                if name_input.lower() == "menu":
                    print("Reterning to menu...")
                    break
                result_message = db_manager.register_user(name_input)
                print(result_message)
        elif choice == "2":
            result_message = db_manager.getusers()
            print(result_message)
        elif choice == "3":
            print("--- add flag mode ---")
            target_id = input("Enter the user id of the user: ")
            flag_text = input("Enter the flag reson: ")
            result = db_manager.addflag(target_id, flag_text)
            print(result)
        elif choice == "4":
            target_id = input("Input user ID Remove: ")
            result_msg = db_manager.remove_user(target_id)
            print(result_msg)
        elif choice == "quit":
            print("exiting program good bye")
            time.sleep(0.5)
            break
        else: 
            print("Invalid choice please pick 1, 2, 3, 4 or say quit to exit.")
except Exception as e:
    print(f"\nAn error occurred: {e}")
finally:
    input("\nPress Enter to exit...")