from models.projects_tags import projects_tags
from models.shared_models import db

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    description = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    tags = db.relationship('Tag',
                           secondary=projects_tags,
                           backref='projects')
