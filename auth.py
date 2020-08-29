from dbClient import db
currentUser = None


def login(_username, _password):
    user = db.getUser(_username)
    if user:
        if user['password'] == _password:
            global currentUser
            currentUser = str(user['_id'])
            print(f'Successfully logged in as {user["name"]}.')
        else:
            print('Wrong password.')
    else:
        print('Cannot find user.')

def getCurrentID():
    return str(currentUser)

def logout():
    global currentUser
    currentUser = None
    print('Logged out.')
