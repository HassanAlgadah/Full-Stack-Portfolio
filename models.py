from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine

database_name = "portfolio"
database_user = 'postgres'
database_pass = '123'
database_path = "postgres://fhomutmxyqjzqz:372dcc312cb85ded68430a74773a2a50c1c50af4cc6a4934791560ac01aede60@ec2-34-197-141-7.compute-1.amazonaws.com:5432/d5stmf6fnmshnp"
db = SQLAlchemy()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String(260))
    image = db.Column(db.String(1000))
    link = db.Column(db.String(120), nullable=False)

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'link': self.link
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, )
    email = db.Column(db.String(120), nullable=False)
    number = db.Column(db.String(10))
    message = db.Column(db.String(1000), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
