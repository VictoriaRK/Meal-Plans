from flask import Flask, render_template
import secrets # For secret key generation
import os # Import blueprint
from routes.webpages import webpage_blueprint

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

########################################################### Create Database ##########################################################

# Select the database filename
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///junction_modeller.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# import database
from db_schema import Meal, Ingredient, Meal_Ingredient, db

# Initialise the database so it can connect with our app
db.init_app(app)

def clean_db():
    """ Gives the ability to reset the database via the first_time.txt file.  """
    # If first_time.txt does not exist, reset the database
    first_time = 'first_time.txt'
    if not os.path.exists(first_time):
        with app.app_context():
            db.drop_all()
            db.create_all()

        # Create the first_time_file to show that the database is live
        with open(first_time, 'w') as first_time:
            first_time.write('Database is active')
            os.chmod(f"{os.getcwd()}/first_time.txt", 0o755)

clean_db()

######################################################################################################################################

# Route to the index
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/main-config-input")
def main_config():
    return 

# Route to it's filename in templates
@app.route('/<filename>')
def templateFilename(filename):
  return render_template(f'{filename}.html')

# Enable routes from routes/webpages.py to be used here
app.register_blueprint(webpage_blueprint)