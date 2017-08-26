# users/models.py
# Written by Jeff Kaleshi

# Groups
ACM_PAID = 'ACMPaid'
ACM_NOT_PAID = 'ACMNotPaid'
ACM_MEMBERS = 'ACMMembership'
ACM_WEB_ADMINS = 'ACMWebAdmins'
ACM_OFFICERS = 'ACMOfficers'

# User search properties
ID = 'uidNumber'
EMAIL = 'mail'
NAME = 'name'
USERNAME = 'sAMAccountName'


class User():
    '''
        Structure to store user data
    '''
    def __init__(
        self, id,username, full_name, display_name, 
        personal_email, acm_email, permissions, is_paid):

        self.id = id
        self.username = username
        self.full_name = full_name
        self.display_name = display_name
        self.personal_email = personal_email
        self.acm_email = acm_email
        self.permissions = permissions
        self.is_paid = is_paid

    def get_json(self):
        '''
            Creates a python dictionary ready to be parsed by jsonify
            :return: {}
        '''
        user_dict = {
            'id': self.id,
            'username': self.username,
            'fullName': self.full_name,
            'displayName': self.display_name,
            'personalEmail': self.personal_email,
            'acmEmail': self.acm_email,
            'permissions': self.permissions,
            'isPaid': self.is_paid,
        }

        return user_dict

    def __str__(self):
        return ("<User: {}>".format(self.full_name))

    def __repr__(self):
        return ("<User: {}>".format(self.full_name))
    