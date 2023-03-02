from models.shared_models import db

projects_tags = db.Table('projects_tags',
                         db.Column('project_id',
                                   db.Integer,
                                   db.ForeignKey('projects.id')),
                         db.Column('tag_id',
                                   db.Integer,
                                   db.ForeignKey('tags.id'))
                         )
