# test_db.py
from app.db.session import SessionLocal

def test_db():
    try:
        db = SessionLocal()
        print("✅ Connected to the database!")
    except Exception as e:
        print("❌ Failed to connect:", e)
    finally:
        db.close()

test_db()
