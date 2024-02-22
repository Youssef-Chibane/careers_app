from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# # Define the database connection URL
# # Replace 'username', 'password', 'hostname', 'port', and 'database_name' with your MySQL credentials
# db_url = 'mysql+pymysql://root:root@localhost:3306/joviancareers'

# # Create the SQLAlchemy engine
# engine = create_engine(db_url)

# # Create a base class for declarative class definitions
# Base = declarative_base()

# # Define your table model
# class User(Base):
#     __tablename__ = 'jobs'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String(250), nullable=False)
#     location = Column(String(250), nullable=False)
#     salary = Column(Integer)
#     currency = Column(String(10))

# # Create the tables
# Base.metadata.create_all(engine)

# # Create a session
# Session = sessionmaker(bind=engine)
# session = Session()

# # Add data to the database
# new_job = User(title="Data Analyst", location="Bengaluru, India", salary=1000000, currency="Rs.")
# session.add(new_job)


# # Commit and close the session
# session.commit()
# session.close()

from sqlalchemy import create_engine, MetaData

# Define the database connection URL
# Replace 'username', 'password', 'hostname', 'port', and 'database_name' with your MySQL credentials
db_url = 'mysql+pymysql://root:root@localhost:3306/joviancareers'

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create a MetaData object
metadata = MetaData()

# Reflect the tables from the database
metadata.reflect(bind=engine)

# Drop all tables
metadata.drop_all(bind=engine)

print("All tables have been dropped.")
