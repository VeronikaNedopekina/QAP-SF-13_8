def check_ticket_number(tickets):
    try:
        number = int(tickets)
        if number > 0:
            return number
        else:
            return False
    except ValueError:
        return False

def check_age(age):
    try:
        n = int(age)
        if 0 < n < 200:
            return n
        else:
            return False
    except ValueError:
        return False


while True:
    price = 0
    tickets = input('Enter number of tickets:\t')
    tickets_number = check_ticket_number(tickets)
    if tickets_number:
        break
    print(f'Please enter correct number of tickets you want to buy\n')

for i in range(tickets_number):
    while True:
        age = check_age(input('Enter age of the ' + str(i+1) + ' participant:\t'))
        if not age:
            print(f'Please enter correct age of the participant\n')
        else:
            break
    i += 1
    if 18 <= age <= 25:
        price += 990
    elif age > 25:
        price += 1390

if tickets_number > 3:
    price = price - ((price * 10) / 100)
    print(f'Total ticket price with 10% discount is {price} roubles')
else:
    print(f'Total ticket price is {price} roubles')
