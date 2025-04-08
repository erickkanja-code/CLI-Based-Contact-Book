# 📇 CLI Contact Book

A simple command-line contact book built with Python. This project allows users to add, view, search, and delete contacts. It demonstrates basic file handling, object-oriented programming, exception handling, and Linux file permissions. Optionally, the project can be extended to use MySQL for persistent storage.

## 🚀 Features

- Add a new contact (name, phone, email)
- View all saved contacts
- Search a contact by name
- Delete a contact
- Data persistence using a text file
- Optional: MySQL integration for storing contacts
- Linux Bash script to launch the app and set file permissions
- Version controlled using Git

## 🛠️ Technologies Used

- Python 3
- Bash scripting
- Linux CLI
- Git & GitHub
- (Optional) MySQL + `mysql-connector-python`

## 🔧 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cli-contact-book.git
cd cli-contact-book
2. Run the App
bash
Copy
Edit
bash run.sh
run.sh will handle setting file permissions and running the Python script.

3. (Optional) Setup MySQL Version
Update the Python script with your MySQL credentials and ensure you have a contacts table created.

📂 Project Structure
bash
Copy
Edit
.
├── contact_book.py       # Main Python script
├── run.sh                # Bash script to run and set permissions
├── contacts.txt          # File for storing contacts
├── README.md             # Project README
✅ To-Do / Checklist
 Basic contact operations using file

 Input validation and error handling

 OOP structure

 Git version control

 MySQL integration

 Unit tests (optional improvement)

🙌 Author
Your Name
GitHub Profile
