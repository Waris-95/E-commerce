from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_reviews():
    review1 = Review(
        user_id=1, product_type_id=1, description="The Navy Slim Fit Suit fits perfectly and looks very sharp. Highly recommend!",
        rating=5)
    review2 = Review(
        user_id=2, product_type_id=2, description="The Black Tuxedo is great, but the fit was a bit off for me. I suggest trying a size up.",
        rating=4)
    review3 = Review(
        user_id=3, product_type_id=3, description="The Brown Corduroy Pants were not as expected. The material felt cheap.",
        rating=2)

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
