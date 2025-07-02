from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Format: mysql+pymysql://<username>:<password>@<host>/<dbname>
DATABASE_URL = "mysql+pymysql://root:Trankhacnhu132!@localhost/fastapi"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency lấy session DB
def getdatabase():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
