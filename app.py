from flask import Flask
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
from src.models import db
from src.routes.character_routes import characters_bp
from sqlalchemy.exc import OperationalError
from src.routes import cache
from flask_cors import CORS
from src.utils.constants import ENVIRONMENTS

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

front_end_url = os.getenv("FRONT_END_URL")
environment = os.getenv("ENVIRONMENT")

origins_map = {
    ENVIRONMENTS.LOCAL.value: ["*"],
    ENVIRONMENTS.PRODUCTION.value: [front_end_url],
}

allowed_origin = origins_map.get(environment, origins_map[ENVIRONMENTS.PRODUCTION.value])

CORS(app, origins = allowed_origin)

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
