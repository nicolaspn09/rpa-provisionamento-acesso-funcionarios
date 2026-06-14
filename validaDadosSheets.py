import os
import requests
import unicodedata
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime

import sys

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


def diretorio_json():
    pass # Logica de negocio removida por seguranca corporativa



def exclui_linha(linha):
    pass # Logica de negocio removida por seguranca corporativa



def movimenta_backup(carimbo_data, endereco_email, nome_solicitante, local_trabalho, radio_frequencia, matricula_colaborador, nome_completo, matricula_referencia, uso_email, sequencial, status_rpa):
    pass # Logica de negocio removida por seguranca corporativa

def solicita_tabela_sheet():
    pass # Logica de negocio removida por seguranca corporativa



def obtem_tabela_api():
    pass # Logica de negocio removida por seguranca corporativa



def limpar_nome(nome):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_sql(matricula):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_sql_funcionario(matricula):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_sheet():
    pass # Logica de negocio removida por seguranca corporativa
