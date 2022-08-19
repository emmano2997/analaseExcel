import pandas as pd
from twilio.rest import Client
 
# Your Account SID from twilio.com/console
account_sid = "ACe893140314e60a95a16d0a75cbe0d8dd"
# Your Auth Token from twilio.com/console
auth_token  = "06fc6f3fb6e3eb9046bf1b2373c4cd52"
client = Client(account_sid, auth_token)
 
# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
 
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5581999953007",
            from_="+12029464619",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
        