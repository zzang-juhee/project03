from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()

class MenuModel(db.Model):
    __tablename__ = "menu"
 
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer(),unique = True)
    menu_name = db.Column(db.String(32), nullable = False)
    menu_price = db.Column(db.Integer(),nullable = False)
    menu_type = db.Column(db.String(32), nullable = False)
 
    def __init__(self, menu_id, menu_name, menu_price, menu_type):
        self.menu_id = menu_id
        self.menu_name = menu_name
        self.menu_price = menu_price
        self.menu_type = menu_type
 
    def __repr__(self):
        return f"{self.menu_name}:{self.menu_id}"