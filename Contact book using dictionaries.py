contact = {}
n = int(input('enter the no.of contacts you would like to save:'))

for i in range(n):
    name = input('enter name:')
    number = int(input('enter the mobile no.: '))
    contact[name] = number

print(contact)
# making change in number or name

anychange = input('dou you want to make changes in the book(y/n): ')



if 'y' in anychange:
    a = input('do u want to make changes in name or number(na/nu): ')
    if 'na' in a:
            name_change = input('enter the name you want to change: ')
            contact[name_change] = input('enter the renamed version: ')
    elif'nu' in a:
            number_change = input('enter the nameof the number u want to change:')
            contact[number_change] = input('enter the new number: ')
        
        
elif 'n' in anychange:
    add_name = input('do u want to add any new number:(y/n)')
    if 'y' in add_name:
            nam = input('enter name:')
            num = int(input('enter num:'))
            contact.update({nam:num})
print(contact)   

