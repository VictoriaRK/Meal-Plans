from flask_sqlalchemy import SQLAlchemy

# Create the database interface
db = SQLAlchemy()

class Meal(db.Model):
    __tablename__='meal'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    def __init__(self, name):
        self.name = name

class Ingredient(db.Model):
    __tablename__='ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    def __init__(self, name):
        self.name = name

class Meal_Ingredient(db.Model):
    __tablename__='meal_ingredient'
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    def __init__(self, meal_id, ingredient_id):
        self.meal_id = meal_id
        self.ingredient_id = ingredient_id