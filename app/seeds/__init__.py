from flask.cli import AppGroup
from .favorite_items import seed_favorites, undo_favorites
from .order_details import seed_order_items, undo_order_items
from .orders_management import seed_orders, undo_orders
from .product_categories import seed_product_types, undo_product_types
from .product_reviews import seed_reviews, undo_reviews
from .products_info import seed_products, undo_products
from .style_details import seed_styles, undo_styles
from .styles_management import seed_style_items, undo_style_items
from .users import seed_users, undo_users

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_reviews()
        undo_styles()
        undo_style_items()
        undo_order_items()
        undo_orders()
        undo_favorites()
        undo_products()
        undo_product_types()
        undo_users()
    seed_users()
    seed_product_types()
    seed_products()
    seed_favorites()
    seed_orders()
    seed_order_items()
    seed_style_items()
    seed_styles()
    seed_reviews()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_product_types()
    undo_products()
    undo_favorites()
    undo_orders()
    undo_order_items()
    undo_style_items()
    undo_styles()
    undo_reviews()
    # Add other undo functions here
