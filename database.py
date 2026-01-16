from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLite URL
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})


#PostgreSQL URL
# SQLALCHEMY_DATABASE_URL = "postgresql://todouser:secret123@localhost:5432/todosapp"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# PostgreSQL URL sur Render
SQLALCHEMY_DATABASE_URL = "postgresql://deployed_database_user:ByyNICh9Jqr3qkQ9LY96pK8x2sz5RAd2@dpg-d5l7780gjchc7387lrqg-a/deployed_database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()