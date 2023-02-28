from flask import Flask, render_template, render_template
from models.projects import Project
from flask_sqlalchemy import SQLAlchemy
from models.shared_models import db
import os

# -------------------- Flask variables --------------------
app = Flask('__app__')
app.config['SECRET_KEY'] = os.environ.get('PORTFOLIO_FLASK_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:z2)F!WRQu1Ntx@localhost/portfolio_db'
db.init_app(app)


@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)


