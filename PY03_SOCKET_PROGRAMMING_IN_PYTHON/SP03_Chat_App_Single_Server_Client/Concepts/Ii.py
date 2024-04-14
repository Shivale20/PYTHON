while True:
    msg = input('user' + ' - ')

    if msg == 'bye':
        print('connection failed')
        break
    elif msg.startswith('/file'):
        msg_parts = msg.split()
        if len(msg_parts) >=2 :
            en_msg = msg_parts[1]
            print(f'Sending file name: {en_msg}')
        else:
            print(f'No file is being sent.')
    else:
        print(f'Check below')