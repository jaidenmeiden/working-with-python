PHONE = '+600213813'

def get_phone():
    phone = input('Give me your phone:')
    if not phone:
        return PHONE.round()
    return int(phone)

def run():
    my_phone = get_phone()
    print(f'Phone is: {my_phone}')

run()