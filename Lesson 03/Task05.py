# Задача 4
# Обращение в письмах начинаются с фразы “Dear Mr . /Mrs . /Mis s /Ms. ...“.
# Необходимо определить и вывести пол человека, которому данное письмо адресовано.
# Приглашение письма запрашивается у пользователя.

addr_list = ['Dear Mr.', 'Dear Mrs.', 'Dear Miss.', 'Dear Ms.']
# Here we propose the user to choose what will be used in the message.
for i, k in enumerate(addr_list):
    print(i + 1, k)
mail_address = input('Please select an option:')
# If the option entered above is correct we're composing the mail body
# using the option chosen above and verifying the gender
if mail_address.isnumeric() and (int(mail_address) in range(1, 5)):
    mail_body = addr_list[int(mail_address) - 1] + input(addr_list[int(mail_address) - 1])
    print('Mail body is: ', mail_body)
    if mail_body.find(addr_list[0]) != -1:
        print('The gender is male.')
    else:
        print('The gender is female.')
else:
    print('Wrong Option!')
