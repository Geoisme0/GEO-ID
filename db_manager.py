import json, uuid, os
base_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(base_dir,"users.json")

def register_user(name):
    user_id = str(uuid.uuid4())[:8]
    new_user = {"name":name, "id": user_id, "flags":[]}
    try: 
        with open(filename, "r") as file:
            users_list = json.load(file)
    except FileNotFoundError:
        users_list = []
    users_list.append(new_user)
    with open(filename, "w") as file:
        json.dump(users_list, file, indent=4)
    return f"Saved {name} with ID:{user_id}"

def remove_user(target_id):
    try:
        with open(filename, "r") as file:
            users_list = json.load(file)
    except FileNotFoundError:
        return "No users found"
    initial_length = len(users_list)
    updated_list = [user for user in users_list if user["id"] != target_id]

    if len(updated_list) == initial_length:
        return f"User ID '{target_id}' not found."
    with open(filename, "w") as file:
        json.dump(updated_list, file, indent=4)
    return f"Removed User ID: '{target_id}'"

def getusers():
    output_lines = []
    try: 
        with open(filename, "r") as file:
            users_list = json.load(file)
        for user in users_list:
            user_flags = user.get("flags", [])
            flags_str = ", ".join(user_flags) if user_flags else "None"
            output_lines.append(f"Name: {user['name']} - ID: {user['id']} - Flags: {flags_str}")
        return "\n".join(output_lines)
    except FileNotFoundError: 
        return "Save a user first"

def addflag(target_id, flag_text):
    try: 
        with open(filename, "r") as file:
            users_list = json.load(file)
    except FileNotFoundError:
        return "Save a user first"
    found = False

    for user in users_list:
        if user["id"] == target_id:
            found = True
            if "flags" not in user:
                user["flags"] = []
            user["flags"].append(flag_text)
            break
    if not found:
        return f"User ID '{target_id}' not found."
    with open(filename, "w") as file:
        json.dump(users_list, file, indent=4)
    return f"Added flag{flag_text}" 