import os
from tkinter.tix import Form
from sqlalchemy import case, true
import streamlit as st
import pages.agendamentos.incluir as IncluirCliente
import pages.agendamentos.path as IncluirPath
import pages.agendamentos.cadastrarContato as IncluirContato
import pages.agendamentos as pages
import pandas as pd

st.set_page_config(page_title='Agendamento Whatsapp | Assessoria',
                   page_icon='chart_with_upwards_trend',
                   layout='wide',
                   initial_sidebar_state="expanded")

menu = st.sidebar.selectbox(
  'Selecione a pagina',
  ['Agendamento Mensagem', 'Alterar Agendamento', 'Excluir Agendamento', 'Cadastro Diretorio', 'Cadastrar Contatos']
)

if menu == 'Agendamento Mensagem':
  IncluirCliente.incluir()
elif menu == 'Cadastro Diretorio':
  IncluirPath.path()
elif menu == 'Cadastrar Contatos':
  IncluirContato.cadastrarContato()