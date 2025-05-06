from openai import AzureOpenAI
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../alembic')))
from models import Embeddings

# Initialize DB Connection
engine = create_engine("postgresql://postgres:Admin123@localhost:5432/vector")
Session = sessionmaker(bind=engine)
session = Session()

def get_embeddings(text_clause):
    return 

def add_to_pg_vector(session, embeddings):
    return

def search_from_pg_vector(session, text_array, query_embedding, k=1):
    return

def main():
    print("")
