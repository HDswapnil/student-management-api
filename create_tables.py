from database.connection import Base, engine
from models.student import Student

# Create the database tables
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")