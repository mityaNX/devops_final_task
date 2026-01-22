from flask import Blueprint, render_template, request, redirect, url_for
import requests
from app import db
from app.models import LikedCat

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/random_cat")
def random_cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search", timeout=5)
    response.raise_for_status()
    cat_url = response.json()[0]["url"]
    return render_template("index.html", cat_url=cat_url)

@main.route("/like", methods=["POST"])
def like():
    cat_url = request.form.get("cat_url")
    if cat_url:
        db.session.add(LikedCat(image_url=cat_url))
        db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/liked_cats")
def liked_cats():
    cats = LikedCat.query.all()
    return render_template("liked_cats.html", cats=cats)
