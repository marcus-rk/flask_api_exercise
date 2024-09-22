import sqlite3
from data_dict import random_users

# Create/Connect to database (members.db)
def create_connection():
    connection = sqlite3.connect('members.db')
    # Allow rows to be returned as dictionaries
    connection.row_factory = sqlite3.Row
    return connection

# Create members table if it doesn't exist
def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT,
                        last_name TEXT,
                        birth_date TEXT,
                        gender TEXT,
                        email TEXT,
                        phonenumber TEXT,
                        address TEXT,
                        nationality TEXT,
                        active BOOLEAN,
                        github_username TEXT
                    )''')

    connection.commit()
    connection.close()

# Insert members into the members table. NOTE: Should only be run once
def insert_members():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.executemany('''INSERT INTO members 
        (first_name, last_name, birth_date, gender, email, phonenumber, address, nationality, active, github_username)
        VALUES (:first_name, :last_name, :birth_date, :gender, :email, :phonenumber, :address, :nationality, :active, :github_username)
        ''', random_users)

    connection.commit()
    connection.close()

# Returns number of rows in members table
def check_if_members_exist():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM members')
    count = cursor.fetchone()[0]
    connection.close()
    return count > 0

# Fetch all members from members table
def fetch_all_members():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM members')
    members = cursor.fetchall()
    # Convert each row to a dictionary using dict(row)
    members_list = [dict(member) for member in members]
    connection.close()
    return members_list

# Fetch member by ID
def fetch_member_by_id(member_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM members WHERE id = ?', (member_id,))
    member = cursor.fetchone()
    connection.close()
    # Return converted member as dictionary
    return dict(member)

# Insert a new member
def insert_member(new_member):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO members 
                      (first_name, last_name, birth_date, gender, email, phonenumber, address, nationality, active, github_username)
                      VALUES (:first_name, :last_name, :birth_date, :gender, :email, :phonenumber, :address, :nationality, :active, :github_username)''', 
                   new_member)
    connection.commit()
    connection.close()

# Update a member by ID
def update_member(member_id, updated_data):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''UPDATE members 
                      SET first_name = :first_name, last_name = :last_name, birth_date = :birth_date, 
                          gender = :gender, email = :email, phonenumber = :phonenumber, 
                          address = :address, nationality = :nationality, active = :active, github_username = :github_username 
                      WHERE id = :id''', {**updated_data, "id": member_id})
    connection.commit()
    connection.close()

# Update github username by ID
def update_github_username_by_id(member_id, new_github_username):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE members SET github_username = ? WHERE id = ?', (new_github_username, member_id))
    connection.commit()
    connection.close()

# Delete a member by ID
def delete_member(member_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM members WHERE id = ?', (member_id,))
    connection.commit()
    connection.close()