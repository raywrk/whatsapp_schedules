from operator import index
import pandas as pd
from sqlalchemy import false
import streamlit as st
import psycopg2


def consultaPath():
    db_connection = psycopg2.connect(host='ec2-54-235-98-1.compute-1.amazonaws.com', database='da9l8k9c6ulbd5',
                                         user='lcmulsicvhazdl', password='0101b23af78c44e6bf095833662077d9909afdc669962f0fd8b7ef593916fd91', port='5432')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f'''
        select diretorio from "path" p 
        ''')
    result = db_cursor.fetchall()
    for row in result:
        result = row[0]

    db_connection.close()
    return result

def incluir():
    tipo = st.selectbox('Selecione o tipo de agendamento', ('Telefone', 'Grupo'))
    if tipo == 'Telefone':
        telefone = st.text_input('Telefone')
    else:
        grupo = st.text_input('Grupo')
    mensagem = st.text_area('Mensagem')
    start_date = st.date_input(
        "Data início", value=pd.to_datetime("2022-01-01", format="%Y-%m-%d"))
    hora = st.number_input('Hora')
    minuto = st.number_input('Minuto')
    f = st.file_uploader("Upload a file")
    if f is not None:
        path_in = f.name
        arquivo =  consultaPath() + '/' + path_in
    else:
        path_in = None


    def add_data():
        db_connection = psycopg2.connect(host='ec2-54-235-98-1.compute-1.amazonaws.com', database='da9l8k9c6ulbd5',
                                         user='lcmulsicvhazdl', password='0101b23af78c44e6bf095833662077d9909afdc669962f0fd8b7ef593916fd91', port='5432')
        db_cursor = db_connection.cursor()
        db_cursor.execute(f'''
          INSERT INTO public.contacts
          (phone_wpp, group_wpp, message, image_path,
           data_send, hour_send, minute_send)
          VALUES('{telefone}', '{grupo}', '{mensagem}',
                 '{arquivo}', '{start_date}', {hora}, {minuto})
        ''')
        db_connection.commit()

    if st.button("Salvar"):
        if telefone == '':
            st.error("Preencha todos os dados")
        else:
            add_data()
            st.success('Registrado com sucesso!')

