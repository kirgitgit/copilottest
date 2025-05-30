"""
Business logic module that handles user data operations.
This module provides an interface between the application and the data access layer.
"""

# Import the data_access module which contains database interaction functions
import data_access

def setup_database():
    """
    Initialize the database by creating the users table.
    
    This function should be called when the application starts
    to ensure the required database structure exists.
    """
    data_access.create_users_table()

def add_users(users):
    """
    Add multiple users to the database.
    
    Args:
        users (list): A list of user dictionaries containing user information
                     Each dictionary should have the required user fields
    """
    data_access.insert_users(users)

def get_all_users():
    """
    Retrieve all users from the database.
    
    Returns:
        list: A list of dictionaries where each dictionary represents a user
              with their corresponding data
    """
    return data_access.fetch_all_users()

def clear_users_table():
    """
    Remove all records from the users table.
    
    This function is typically used for testing purposes or when
    resetting the application to its initial state.
    """
    data_access.clear_users_table()
