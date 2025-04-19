import business_logic

def main():
    users_data = [
        ('John Doe', 'john.doe@abc.com'),
        ('Jane Smith', 'jane.smith@abc.com'),
        ('Mike Gabe', 'mike.gabe@abc.com')
    ]

    business_logic.setup_database()
    business_logic.add_users(users_data)
    all_users = business_logic.get_all_users()
    print(all_users)

if __name__ == "__main__":
    main()
