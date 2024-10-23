import os
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Set the secret key
app.config['SECRET_KEY'] = os.urandom(24)  # Generates a random secret key

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ayusao034@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    message_content = request.form['message']
    
    # Compose the email
    msg = Message('New Contact Form Submission',
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[app.config['MAIL_USERNAME']])
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}"
    
    # Send the email
    mail.send(msg)
    
    # Flash success message
    flash('Message submitted successfully!', 'success')
    
    # Redirect back to the index page
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
