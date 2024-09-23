from flask import Flask, jsonify, request
from database import fetch_all_members, fetch_member_by_id, insert_member, update_member, update_github_username_by_id, delete_member
import requests

app = Flask(__name__)

# GET: Get all members
@app.route('/members', methods=['GET'])
def get_members():
    try:
        members = fetch_all_members()
        if members:
            return jsonify(members), 200
        else:
            return jsonify({"error": "Members not found"}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred", "message": str(e)}), 500

# GET: Get member by ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = fetch_member_by_id(member_id)
        if member:
            return jsonify(member), 200
        else:
            return jsonify({"error": "Member not found"}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred", "message": str(e)}), 500

# POST: Create a new member
@app.route('/members', methods=['POST'])
def create_member():
    new_member = request.json
    insert_member(new_member)
    return jsonify(new_member), 201

# PUT: Update a member by ID
@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member_route(member_id):
    updated_data = request.json
    update_member(member_id, updated_data)
    return jsonify({"message": "Member updated successfully"}), 200

# PATCH: Update GitHub username of a member by ID
@app.route('/members/<int:member_id>/github_username', methods=['PATCH'])
def update_github_username(member_id):
    new_github_username = request.json.get('github_username')
    update_github_username_by_id(member_id, new_github_username)
    return jsonify({"message": "GitHub username updated successfully"}), 200

# DELETE: Delete a member by ID
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member_route(member_id):
    delete_member(member_id)
    return jsonify({"message": "Member deleted successfully"}), 200

# GET: Fetch repositories of a GitHub user by ID
# Note: If the authenticated user searches for their own ID, 
# private repositories will also be included in the response
@app.route('/members/<int:member_id>/repos', methods=['GET'])
def list_github_repos(member_id):
    member_github_username = fetch_member_by_id(member_id)['github_username']
    
    # Fetch and format public repositories
    public_repos = fetch_public_repos(member_github_username)
    repo_list = [
        {
            "name": repo["name"],
            "visibility": "private" if repo["private"] else "public",
            "url": repo["html_url"]
        } for repo in public_repos
    ]

    # Check for GitHub access token in headers
    github_access_token = request.headers.get('Authorization')
    if github_access_token:
        headers = {'Authorization': github_access_token}
        current_user_username = get_current_user_username(headers)

        # If the authenticated user is the member, fetch their private repositories and add to repo_list
        if current_user_username == member_github_username:
            private_repos = fetch_private_repos(headers)
            for repo in private_repos:
                repo_list.append({
                    "name": repo["name"],
                    "visibility": "private",
                    "url": repo["html_url"]
                })

    return jsonify(repo_list), 200

########################################################################################
# Helping functions
########################################################################################

# Fetch public repositories of a GitHub user
def fetch_public_repos(username):
    public_repos_url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url=public_repos_url)
    return response.json()

# Fetch private repositories of the authenticated user
def fetch_private_repos(headers):
    private_repos_url = 'https://api.github.com/user/repos?type=private'
    response = requests.get(url=private_repos_url, headers=headers)
    return response.json() if response.ok else []

# Get the GitHub username of the authenticated user
def get_current_user_username(headers):
    user_info_url = 'https://api.github.com/user'
    response = requests.get(url=user_info_url, headers=headers)
    return response.json().get('login')