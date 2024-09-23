# Member Management API (Python, Flask & SQLite)

This project is a RESTful API for managing a database of members using Python, SQLite, and Flask. The API allows you to perform CRUD operations (Create, Read, Update, Delete) on member data stored in the database. The project includes integration to update GitHub usernames for members and auto-populates sample members into the database.

## Prerequisites

- **Python:** Ensure Python is installed on your system. Verify the installation by running:

  ```sh
  python3 --version
  ```
- **SQLite:** This project uses SQLite for database management. No additional setup is required since Python includes SQLite by default.

- **Git:** Make sure Git is installed on your system to clone the repository. You can check this by running:

  ```sh
  git --version
  ```

## Project Structure
The project is organized into several key files, each serving a specific purpose:

```sh
flask_api_exercise/
│
├── app.py
├── database.py
├── data_dict.py
├── members.db
├── routes.py
├── requirements.txt
└── README.md
```
- **app.py:** Starts the Flask server, initializes the database, and updates GitHub usernames.
- **database.py:** Handles all database interactions like creating tables, inserting members, and performing CRUD operations.
- **data_dict.py:** Stores pre-populated data for members.
- **routes.py:** Defines the API endpoints for interacting with member data.
- **members.db:** SQLite database where all member data is stored.
- **requirements.txt:** Contains the required Python packages for the project.

## Setup Instructions

### 0. Navigate to the Desired Directory
Before cloning the repository, navigate to the directory where you want to clone it. For example:
```sh
cd /path/to/your/directory
```
Replace /path/to/your/directory with the path where you want to place the repository.

### 1. Clone the Repository
Clone the repository to your local machine using Git:
```sh
git clone https://github.com/marcus-rk/flask_api_exercise.git
```

### 2. Navigate to the Repository Directory
```sh
cd flask_api_exercise
```

### 3. Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run Flask API server
```sh
python3 app.py
```
This will:
- Create the members table in the members.db SQLite database.
- Populate the table with a predefined set of members (from data_dict.py) if the table is empty.
- Update the GitHub usernames of the first 10 members.

**Note:** By default, the API server runs on http://127.0.0.1:5000

## API Endpoints

The following are the available API endpoints for managing members:

### Fetch All Members

- **Endpoint**: `/members`
- **Method**: `GET`
- **Description**: Fetches all members from the database.

**Response**:
```json
[
  {
    "id": 1,
    "first_name": "Chad",
    "last_name": "Johnson",
    "birth_date": "1993-10-16",
    "gender": "Male",
    "email": "kristenwright@example.net",
    "phonenumber": "267-665-3149x1716",
    "address": "USS Bryant\nFPO AA 94943",
    "nationality": "Sudan",
    "active": 1,
    "github_username": "marcus-rk"
  },
  ...
]

### Fetch a Member by ID

- **Endpoint**: `/members/{id}`
- **Method**: `GET`
- **Description**: Fetches a specific member by their ID.

**Response**:
```json
{
  "id": 1,
  "first_name": "Chad",
  "last_name": "Johnson",
  "birth_date": "1993-10-16",
  "gender": "Male",
  "email": "kristenwright@example.net",
  "phonenumber": "267-665-3149x1716",
  "address": "USS Bryant\nFPO AA 94943",
  "nationality": "Sudan",
  "active": 1,
  "github_username": "marcus-rk"
}
```

### Add a New Member

- **Endpoint**: `/members`
- **Method**: `POST`
- **Description**: Adds a new member to the database.

**Request Body**:
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "birth_date": "1980-01-01",
  "gender": "Male",
  "email": "john.doe@example.com",
  "phonenumber": "123-456-7890",
  "address": "123 Main St, City, Country",
  "nationality": "CountryName",
  "active": 1,
  "github_username": "john-doe"
}
```

**Response**:
```json
{
  "message": "New member added successfully."
}
```

### Fetch Repositories of a GitHub User by Member ID

- **Endpoint**: `/members/{member_id}/repos`
- **Method**: `GET`
- **Description**: Fetches the public repositories of a member's GitHub account based on their ID. If the authenticated user fetches their own repositories (by including an authorization token), private repositories will also be included.

**Reqeust Headers (Optional)**
- `Authorization`: Token for GitHub API access. This is required only if the user wants to fetch their own private repositories.

**Response Example (Without Authentication - Public Repositories Only):**:
```json
[
  {
    "name": "public-repo-1",
    "visibility": "public",
    "url": "https://github.com/username/public-repo-1"
  },
  {
    "name": "public-repo-2",
    "visibility": "public",
    "url": "https://github.com/username/public-repo-2"
  }
]
```

**Response Example (With Authentication - Public and Private Repositories):**:
```json
[
  {
    "name": "public-repo-1",
    "visibility": "public",
    "url": "https://github.com/username/public-repo-1"
  },
  {
    "name": "private-repo-1",
    "visibility": "private",
    "url": "https://github.com/username/private-repo-1"
  }
]
```

**NOTE: There are more end-points than listed in this README**
