# Запросить у пользователя строку. В строке должна содержаться минимум одна цифра.
# Если цифры в введенной строке нет, завершить программу с сообщением об отсуствии цифры.
# Если строка введена правильно запросить у пользователя цифру.
# Результатом работы программы должно быть сообщение есть искомая цифра в исходной строке или нет.
nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
my_data = set(input('Enter string containing number:'))
if my_data.intersection(nums):
    my_num = set(input('Enter your number'))
    if my_data.intersection(my_num):
        print('Number {} is present in you string'.format(*my_num))
    else:
        print('There\'s no number {} in your string'.format(*my_num))
else:
    print('There\'s no number in your string. End!!!')

