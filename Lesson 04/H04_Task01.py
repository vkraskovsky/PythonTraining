# Задача 1
# Определить, является ли введенное слово идентификатором,
# т.е. начинается ли оно с английской буквы в любом регистре или знака подчеркивания
# и не содержит других символов, кроме букв английского алфавита (в любом регистре),
# цифр и знака подчеркивания.



str_id = input('Enter string:')
if 'a' <= str_id[0].lower() <= 'z' or str_id[0] == '_':
    for i in range(1, len(str_id)):
        if not ('a' <= str_id[i].lower() <= 'z' or str_id[i] == '_' or '0' <= str_id[i].lower() <= '9'):
            print('Your string is NOT an identifier!')
            quit()
    print('Correct - our string is an identifier!')
else:
    print('Starts wit wrong symbol!')
