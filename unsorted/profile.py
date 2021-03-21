#step 8-13
def build_profile(first, second, **user_profile):
    profile = {}
    profile['first name'] = first
    profile['last name'] = second
    for key, value in user_profile.items():
        profile[key] = value
    return profile

print('Описание пользователя: ')
print(build_profile('Максим', 'Мухин', location='Волгоград', age='24', height='2 метра'))