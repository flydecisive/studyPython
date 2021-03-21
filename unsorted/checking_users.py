#step 5-10
current_users = ['максим', 'таня', 'коля', 'марина', 'виктор']
new_users = ['Максим', 'Анатолий', 'тимофей', 'таня', 'Николя']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('К сожалению имя ' + new_user, end=' ')
        print('уже используется, вам необходимо ', end='')
        print('выбрать другое имя')
    else:
        print('Имя ' + new_user + ' доступно')