from app.models import db, Favorite, environment, SCHEMA
from sqlalchemy import text

# Adds a demo user, you can add other users here if you want
def seed_favorites():
    favorite1 = Favorite(
        user_id=1, product_id=1, product_type_id=1,
        image="https://www.mrporter.com/variants/images/1647597340198467/ou/w1200_q60.jpg",
    )
    db.session.add(favorite1)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_favorites():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM favorites"))
    db.session.commit()
