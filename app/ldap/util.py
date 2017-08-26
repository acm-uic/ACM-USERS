# ldap/util.py
# Written by Jeff Kaleshi

def get_permissions(query):
    permissions = []
    for item in query:
        permission = item[3:item.find(',')]
        if permission != 'ACMPaid' and permission != 'ACMNotPaid':
            permissions.append(permission)

    return permissions

def get_paid_status(query):
    result = False
    permissions = get_permissions(query)

    if 'ACMPaid' in permissions:
        result = True
    
    return result

def generate_user_data(query):
    user_data = {
        'id': None if str(query.uidNumber) == '[]' else int(str(query.uidNumber)),
        'username': None if str(query.sAMAccountName) == '[]' else str(query.sAMAccountName),
        'full_name': None if str(query.name) == '[]' else str(query.name),
        'display_name': None if str(query.displayName) == '[]' else str(query.displayName),
        'personal_email': None if str(query.mail) == '[]' else str(query.mail),
        'acm_email': None if str(query.sAMAccountName) == '[]' else  str(query.sAMAccountName) + '@acm.cs.uic.edu',
        'permissions': get_permissions(query.memberOf),
        'is_paid': get_paid_status(query.memberOf),
        }
    return user_data