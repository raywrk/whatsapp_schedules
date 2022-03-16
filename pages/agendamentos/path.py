import pandas as pd
import streamlit as st
import psycopg2

def path():
    diretorio = st.text_input('Insira o diretorio')
    def add_data():
        db_connection = psycopg2.connect(host='ec2-54-235-98-1.compute-1.amazonaws.com', database='da9l8k9c6ulbd5',
                                         user='lcmulsicvhazdl', password='0101b23af78c44e6bf095833662077d9909afdc669962f0fd8b7ef593916fd91', port='5432')
        db_cursor = db_connection.cursor()
        db_cursor.execute(f'''
          INSERT INTO public."path"
          (diretorio)
          VALUES('{diretorio}');
        ''')
        db_connection.commit()

    if st.button("Salvar"):
        if diretorio == '':
            st.error("Preencha o campo diretorio")
        else:
            add_data()
            st.success('Registrado com sucesso!')
            
