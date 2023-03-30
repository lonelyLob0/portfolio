from flask import Flask, render_template, redirect, url_for
from models.projects import Project
from models.shared_models import db
from flask_migrate import Migrate
from models.forms import ContactForm
from models.tags import Tag
import os
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -------------------- Flask variables --------------------
app = Flask('__app__')
app.config['SECRET_KEY'] = os.environ.get('PORTFOLIO_FLASK_KEY')

# It is a rich text editor.
ckeditor = CKEditor(app)

Bootstrap(app)

POSTGRES_DB_PW = os.environ.get('POSTGRES_DB_PW')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{POSTGRES_DB_PW}' \
                                        f'@localhost/portfolio_db'
db.init_app(app)

migrate = Migrate(app, db)

# -------------------- Email variables --------------------
SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
EMAIL_APP_PW = os.environ.get('EMAIL_APP_PW')

print(SENDER_EMAIL)

def send_email(subject, body, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = SENDER_EMAIL
    sender_password = EMAIL_APP_PW

    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = to_email
    message.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()


@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        send_email(subject=f'Portfolio message from: {form.name.data}',
                   body=form.comment.data,
                   to_email=SENDER_EMAIL)
        return redirect(url_for('home'))

    return render_template('contact.html', form=form)


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)


