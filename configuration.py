
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.templates_folder = "/templates" #default--> whatwvwer the templates u have -- templates
#app.template_folder = "pages/" # abhi wo templates me nahi deikhega jab usko rename karenge tab deikhenga
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskk_db'
db = SQLAlchemy(app)
