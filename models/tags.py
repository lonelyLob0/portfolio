from models.shared_models import db
from models.projects_tags import projects_tags


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    projects = db.relationship('Project',
                               secondary=projects_tags,
                               backref='tags')
