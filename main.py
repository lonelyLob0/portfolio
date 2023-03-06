from flask import Flask, render_template, render_template
from models.projects import Project
from models.tags import Tag
from models.projects_tags import projects_tags
from flask_sqlalchemy import SQLAlchemy
from models.shared_models import db
from flask_migrate import Migrate
import os


# -------------------- Flask variables --------------------
app = Flask('__app__')
app.config['SECRET_KEY'] = os.environ.get('PORTFOLIO_FLASK_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:z2)F!WRQu1Ntx@localhost/portfolio_db'
db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)


