print('car game--------->')
user = ""
started = False
while True:
    user = str(input('>>> ')).lower()
    if user.lower() == 'start':
        if started:
            print('Car Is Already Started...')
        else:
            started = True
            print('car Game Started...')
    elif user.lower() == 'stop':
        if not started:
            print('Car Is Already Stopped...')
        else:
            started = False
            print('car Game Stopped...')
    elif user.lower() == 'help':
        print("""
              start - to start the game
              stop - to stop the game
              quit - to quit the game
              """)
    elif user.lower() == 'quit':
        break
    else:
        print('I dont understand That...')
print('thankyou...')
