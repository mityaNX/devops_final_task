from app import db

class LikedCat(db.Model):
    __tablename__ = "liked_cats"

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(500), nullable=False)
