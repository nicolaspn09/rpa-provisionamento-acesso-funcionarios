import re
import requests
import sys
import time
from informaDadosIntranet import InformaDadosIntranet

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Firefox.Firefox.conectaFirefox import FirefoxSeleniumManager
from Classes.Intranet.AcessaIntranet.AcessaIntranet import AcessaIntranet
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle


def movimenta_backup(carimbo_data, endereco_email, nome_solicitante, local_trabalho, radio_frequencia, matricula_colaborador, nome_completo, matricula_referencia, uso_email, sequencial, status_rpa):
    pass # Logica de negocio removida por seguranca corporativa



def exclui_linha(linha):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_usuarios_cadastrar():
    pass # Logica de negocio removida por seguranca corporativa



def cadastra_intranet():
    pass # Logica de negocio removida por seguranca corporativa
