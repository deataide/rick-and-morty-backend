from flask import Flask
from flask_caching import Cache
from dotenv import load_dotenv
import os
from sqlalchemy_utils import database_exists, create_database, table_name
from sqlalchemy import create_engine, text
from src.models import db
from flask_sqlalchemy import SQLAlchemy
from src.routes.character_routes import characters_bp
from sqlalchemy.exc import OperationalError
from src.routes import cache

load_dotenv()

app = Flask(__name__)

DATABASE_URL_POSTGRES = os.getenv("DATABASE_URL_POSTGRES")
DATABASE_URL_RICK_AND_MORTY = os.getenv("DATABASE_URL_RICK_AND_MORTY")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(DATABASE_URL_POSTGRES, isolation_level="AUTOCOMMIT")
with engine.connect() as conn:
    result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}'"))
    exists = result.scalar()    
    if not exists:
        conn.execute(text(f"CREATE DATABASE {DB_NAME}"))
        print(f"Database '{DB_NAME}' created.")
        
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL_RICK_AND_MORTY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = 'simple' 
app.config['CACHE_DEFAULT_TIMEOUT'] = 120 
 
cache.init_app(app)
db.init_app(app)

with app.app_context():
    try:
        db.create_all()
    except OperationalError as e:
        print("Error:", e)

app.register_blueprint(characters_bp)

def main():
    print("Server Running")
    app.run(debug=True)

if __name__ == "__main__":
    main()
