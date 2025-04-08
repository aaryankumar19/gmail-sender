# Gmail Sender

This project allows you to send emails using the Gmail API with OAuth2 authentication.

---

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/aaryankumar19/gmail-sender.git
cd gmail-sender
```

### 2. Install Dependencies
Either create a virtual environment(like .venv) or download the packages globally.

Make sure you have Python installed. Then, install the required packages:
```
pip install -r requirements.txt
```
### 3. Set Up Google Cloud Project
1. Go to the Google Cloud Console.

2. Create a new project.

3. After creating the project:

4. Click on the hamburger icon (☰) > APIs & Services > Library

5. Search for Gmail API and enable it.

### 4. Set Up OAuth Credentials
1. Go to APIs & Services > Credentials

2. Click + Create Credentials > OAuth client ID

3. Choose the application type and fill in the required details.

4. After the credentials are created:

5. Download the credentials JSON file

6. Rename it if needed and place it in the project directory

### 5. ▶️ Run the Application
```
python index.py
```
1. You will be prompted to log in with your Google account.

2. After granting permission, a token.json file will be created.

3. The email will be sent using the logged-in account.

✅ Done!
Now your application is successfully sending emails using Gmail API!