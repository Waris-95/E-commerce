from flask_sqlalchemy import SQLAlchemy
import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.getenv("SCHEMA", "")

db = SQLAlchemy()

# helper function for adding prefix to foreign key column references in production
def add_prefix_for_prod(attr):
    if environment == "production" and SCHEMA:
        return f"{SCHEMA}.{attr}"
    return attr
