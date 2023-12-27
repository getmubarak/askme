import sys
import os

sys.path.append(os.path.abspath('.'))

import streamlit as st
import time
import tiktoken
import openai

from AskMe.components.sidebar import sidebar
from sqlalchemy import create_engine, text

from llama_index import VectorStoreIndex, SQLDatabase
from llama_index.objects import ObjectIndex, SQLTableNodeMapping, SQLTableSchema
from llama_index.callbacks import CallbackManager, TokenCountingHandler
from llama_index.indices.struct_store import SQLTableRetrieverQueryEngine
from llama_index import ServiceContext
from llama_index.llms import OpenAI
import pandas as pd
import numpy as np
from decimal import *
import matplotlib.pyplot as plt

def load_tables():
    db_user = st.session_state.get("DB_USER")
    db_password = st.session_state.get("DB_PASSWORD")
    db_host = st.session_state.get("DB_HOST")
    db_name = st.session_state.get("DB_DATABASE") #sampleDB
    connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    engine = create_engine(connection_string)
    sql_database = SQLDatabase(engine)
    tables = list(sql_database._all_tables)
    table_node_mapping = SQLTableNodeMapping(sql_database)
    table_schema_objs = []
    for table in tables:
        #st.write(table)
        st.session_state['tables_dict'][table] = st.text_area(table,key= table)

st.header("Prompt Settings")

if 'tables_dict' not in st.session_state:
    st.session_state['tables_dict'] = {}

if st.session_state.get("database_configured"):
    load_tables()
else:
    st.write("Database not configured") 

st.write(st.session_state.get('tables_dict'))