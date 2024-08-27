import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

username = 'usinag87_matheus'  # Seu nome de usuário
password = '%40Elohim32'  # Sua senha
host = 'usinagemelohim.com.br'  # O endereço do servidor MySQL
port = '3306'  # Porta padrão do MySQL
database = 'usinag87_controleprod'  # O nome do banco de dados

# Criando a URL de conexão usando SQLAlchemy
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'

# Criando a engine
engine = create_engine(connection_string)

# Lendo a tabela em um DataFrame
query_ordens = "SELECT * FROM ordens"
query_pedidos = "SELECT * FROM pedidos"
ordens = pd.read_sql(query_ordens, engine)
pedidos = pd.read_sql(query_pedidos,engine)

col1,col2 = st.columns(2)

with col1:
    col1.table(ordens)

