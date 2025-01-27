# Email API Project

A simple email-sending API using Serverless Framework, Python, and AWS Lambda. Sends an email via SMTP on HTTP request.

## Setup

### 1. Install Dependencies
```bash
npm install
pip install -r requirements.txt
```

### 2. Configure Environment Variables
```bash
EMAIL_USER=your@gmail.com
EMAIL_PASS=password
```

### 3. Run Locally 
```bash
serverless offline start
```

### 4. Test API with Postman
POST request to http://localhost:3002/send-email:
```bash
{
  "receiver_email": "receiver@example.com",
  "subject": "Test Email",
  "body_text": "This is a test email."
}
```

## Error Handling
  - 400: Missing parameters
  - 500: SMTP issues

## License
MIT License
This version is concise and includes the essential setup, usage, and error handling information.