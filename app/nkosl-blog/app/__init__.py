from flask import Flask

nkosl_app = Flask(__name__)
nkosl_app.config['SECRET_KEY'] = 'du_bist_mein_sofa'

from app import routes
