current_users = ['Ali', 'Mustafa', 'Hatim', 'Taha', 'Marie']
new_users = ['Fatema', 'Sakina', 'Taha', 'Mariyah', 'Mustafa']

current_user = []
for user in current_users:
    current_user.append(user.lower())
for new_user in new_users:
    if new_user in current_users:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")
