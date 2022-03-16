
import pandas as pd
from sqlalchemy import false
import streamlit as st
import psycopg2

def cadastrarContato():
    tipo = st.selectbox('Selecione o tipo de agendamento', ('Telefone', 'Grupo'))
    if tipo == 'Telefone':
        contact_wpp = st.text_input('Insira o Telefone')
    else:
        contact_wpp = st.text_input('Insira o ID do Grupo')

    contact_name = st.text_input('Insira o nome do contato')

    def add_data():
        db_connection = psycopg2.connect(host='ec2-54-235-98-1.compute-1.amazonaws.com', database='da9l8k9c6ulbd5',
                                         user='lcmulsicvhazdl', password='0101b23af78c44e6bf095833662077d9909afdc669962f0fd8b7ef593916fd91', port='5432')
        db_cursor = db_connection.cursor()
        db_cursor.execute(f'''
          INSERT INTO public.contacts
          (contact_wpp, contact_name)
          VALUES('{contact_wpp}', '{contact_name}');
        ''')
        db_connection.commit()

    if st.button("Salvar"):
        if contact_wpp == '' or contact_name == '':
            st.error("Preencha todos os dados")
        else:
            add_data()
            st.success('Registrado com sucesso!')

