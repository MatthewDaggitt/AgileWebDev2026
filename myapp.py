from flask_migrate import Migrate

from app import create_app, db
from app.config import DeploymentConfig

app = create_app(DeploymentConfig)
migration = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)