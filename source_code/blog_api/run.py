import os

from src import app

if __name__ == '__main':
    env_name = os.getenv('FLASK_ENV')
    app=create_app(env_name)
    app.run()