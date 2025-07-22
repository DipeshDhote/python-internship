import psycopg2
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()

# Load environment variable
db_name= os.getenv("DB_NAME")
user=os.getenv("USER_NAME")
password=os.getenv("PASS")
host=os.getenv("HOST")
port=os.getenv("PORT")


def connect_to_db():
    connection = psycopg2.connect(
        host=host,       
        database=db_name,    
        user=user,        
        password=password,
        port=port   
    )

    return connection

