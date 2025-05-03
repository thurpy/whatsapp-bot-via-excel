# WhatsApp Bot

Este projeto é um bot que envia mensagens via WhatsApp Web para contatos listados em uma planilha Excel, utilizando Python.

## Funcionalidades

- Carrega uma planilha e uma aba específica.
- Abre o WhatsApp Web.
- Envia mensagens personalizadas a partir de dados da planilha.
- Automatiza envio sequencial para vários contatos.

## Requisitos

- Python 3.7+
- Web WhatsApp previamente autenticado
- A planilha deve conter:
  - Coluna A: Mensagem
  - Coluna B: Número de telefone com DDD e código do país (ex: 5511999999999)

## Instalação

1. Clone o repositório:

git clone https://github.com/thurpy/whatsapp-bot.git
cd whatsapp-bot

2. Instale as dependências:
pip install -r requirements.txt

3. Uso
from bot import WhatsappBot

bot = WhatsappBot('caminho/para/planilha.xlsx', 'NomeDaAba')
bot.open_whatsappweb()
bot.send_messages_for_all()

