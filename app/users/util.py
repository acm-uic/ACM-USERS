# users/util.py
# Written by Jeff Kaleshi

def create_users_dictionary(users):
    '''
        Takes in a list of users and returns a list
        of dictionaries containing user information
        :users: [User, User, ...]
        :return: [{}, {}, ...]
    '''
    users_data = []
    for user in users:
        users_data.append(user.get_json())

    return users_data