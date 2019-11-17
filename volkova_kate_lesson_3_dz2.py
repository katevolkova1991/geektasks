def user_data (name = '', surname = '', year_of_birth = '', city = '', email = '', phone_number = ''):
    return f'{name} {surname}, {year_of_birth}, проживает в городе {city}, электронный адрес {email}' \
           f', номер телефона {phone_number}'

print(user_data(name = "Kate", surname = "Volkova", year_of_birth = 1991, city = "LA"))