#step 5-8 and 5-9
users = ['admin', 'Максим', 'Таня', 'Катя', 'Никита']
#users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello ' + user + ', would you like to see a status report?')
        else:
            print('Hello ' + user + ', thank you for logging again')
else:
    print('We need to find some users')