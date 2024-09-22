from database import create_table, insert_members, check_if_members_exist
from routes import app
import requests, threading

########################################################################################
# Database Initialization and GitHub username update in db
########################################################################################

# Initializes the database
def init_database():
    # Create/Connect database and create table
    create_table()

    # Insert members only if the table is empty
    if not check_if_members_exist():
        insert_members()

# Updates the GitHub usernames for the first 10 members in the database
def update_github_usernames():
    members_to_update = {
        1: "marcus-rk",
        2: "ChristianBT96",
        3: "NikoKiru",
        4: "behu-kea",
        5: "nicklasdean",
        6: "SofieAmalie44",
        7: "clbokea",
        8: "anderslatif",
        9: "DetGrey",
        10: "nathasjafink"
    }

    # Send PATCH request to update the GitHub username for each member
    for member_id, github_username in members_to_update.items():
        url = f'http://127.0.0.1:5000/members/{member_id}/github_username'
        data = {'github_username': github_username}
        requests.patch(url=url, json=data)

########################################################################################
# Start API-server
########################################################################################

def run_server():
    app.run(debug=False) # Set debug=False to prevent issues with threading

if __name__ == '__main__':
    init_database()
    
    # Start the API server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    
    # Update first 10 members github usernames
    update_github_usernames()