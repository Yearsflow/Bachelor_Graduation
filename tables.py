from app import db

class administrator(db.Model):
    Id=db.Column(db.String(8),primary_key=True)
    Name=db.Column(db.String(10),nullable=False)
    Email=db.Column(db.String(20),nullable=False)
    Password=db.Column(db.text,nullable=False)

class users(db.Model):
    Id=db.Column(db.String(8),primary_key=True)
    Name=db.Column(db.String(8),nullable=False)
    Email=db.Column(db.String(20),nullable=False)
    Password=db.Column(db.text,nullable=False)