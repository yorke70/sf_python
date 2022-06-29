import redis


red = redis.Redis(
    host='redis-13602.c300.eu-central-1-1.ec2.cloud.redislabs.com',
    port=13602,
    password='MTnIqelhXe9f71UnfCQEor7txRliJV6R'
)

const = True
while const:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
        else:
            print(f'{name}\'s phone not found')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f'{name}\'s phone deleted')
        else:
            print(f'Not found {name}')
    elif action == 'stop':
        break
    else:
        print('=' * 5 + 'Input correct action' + '=' * 5)
