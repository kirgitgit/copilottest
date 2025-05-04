import data_access

def setup_database():
    data_access.create_users_table()

def add_users(users):
    data_access.insert_users(users)

def get_all_users():
    return data_access.fetch_all_users()

def clear_users_table():
    data_access.clear_users_table()
