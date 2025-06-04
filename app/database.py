import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "rootpass")
MYSQL_DB = os.getenv("MYSQL_DB", "dicodb")
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")  # <-- service name in K8s
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(DATABASE_URL, echo=True)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()