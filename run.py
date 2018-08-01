import os
from app import app


if __name__ == "__main__":
    # config_name = os.getenv('APP_SETTINGS')
    app.run()


# $ export FLASK_APP="run.py"
# $ export APP_SETTINGS="development"
# $ export SECRET="a-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
# $ export DATABASE_URL="postgresql://localhost/mydiary"
