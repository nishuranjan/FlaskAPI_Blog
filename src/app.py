#src/app.py

from flask import Flask
from .config import app_config
from .models import db, bcrypt
from .views.UserView import user_api as user_blueprint
from .views.BlogpostView import blogpost_api as blogpost_blueprint

def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)
  #app.url_map.strict_slashes = False
  app.config.from_object(app_config[env_name])
  bcrypt.init_app(app)
  db.init_app(app)
  app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
  app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogposts')
  
  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your first endpoint is working'

  return app