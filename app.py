from app import create_app, db
from app.db_wait import wait_for_db

app = create_app()

if __name__ == "__main__":
    wait_for_db()

    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=8000)
