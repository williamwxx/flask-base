from app import create_app
from flask_script import Manager

application = create_app('production')

if __name__ == '__main__':
    application.run()
