from app import db

class administrator(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Name=db.Column(db.String(10),nullable=False)
    Email=db.Column(db.String(20),nullable=False)
    Password=db.Column(db.Text,nullable=False)
    def get_id(self):
        return self.Id
    def check_password(self,password):
        return self.Password==password

class users(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Name=db.Column(db.String(8),nullable=False)
    Email=db.Column(db.String(20),nullable=False)
    Password=db.Column(db.Text,nullable=False)
    def get_id(self):
        return self.Id
    def check_password(self,password):
        return self.Password==password