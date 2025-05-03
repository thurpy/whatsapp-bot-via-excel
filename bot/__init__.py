# Libraries.

import openpyxl as op
from openpyxl.worksheet.worksheet import Worksheet
from time import sleep
import webbrowser
import pyautogui as pa # Reading the buttons and "pressing" the keyboard.
from urllib.parse import quote # Library to encode the message.
import pyperclip as pc

# Class WhatsappBot.

class WhatsappBot():

    def __init__(self, spreadsheet_path: str, sheet_name: str) -> None:
        '''
        Starts the bot by loading a tab from a spreadsheet.

        Args: 
            spreadsheet_path (str): Path to the spreadsheet file.
            sheet_name (str): Sheet tab that will be loaded.

        Attributes: 
            self.sheet: Contains the data for the requested tab, accessed through the "load_sheet()" method.
        '''
        self.spreadsheet_path = spreadsheet_path
        self.sheet_name = sheet_name
        self.sheet = self.load_sheet()

    def load_sheet(self) -> Worksheet:
        '''
        Use the openpyxl library to create a file containing data from the spreadsheet and a specific tab.

        Returns: 
            workbook[self.sheet_name] (Worksheet): Data from the requested spreadsheet tab.
        '''
        workbook = op.load_workbook(self.spreadsheet_path)
        return workbook[self.sheet_name]
    
    def open_whatsappweb(self) -> None:
        webbrowser.open('https://web.whatsapp.com')
        sleep(10)

    def send_single_message(self, phone: int, message: str, delay: int = 10) -> None:
        '''D
        Send a message through web WhatsApp to a specific person.

        Args:
            phone: Number to which the message will be sent.
            message: Message that will be sent.
            delay: Time between the actions "open web WhatsApp" and "send message".
        '''
        link_message = f'https://web.whatsapp.com/send?phone={phone}&text={quote(message)}'
        pa.hotkey('ctrl', 'l') # Close the conversation tab.
        sleep(1)
        pc.copy(link_message)
        pa.hotkey('ctrl', 'v')
        sleep(1)
        pa.hotkey('enter')
        sleep(delay)
        pa.hotkey('enter')
            
    
    def send_messages_for_all(self, delay_between_messages: int = 15) -> None:
        '''
        Sends messages to all numbers in the spreadsheet and indicates when a sending is successful.

        Args: 
            delay_between_messages (int): Parameter for the "send_single_message" function, time between opening the browser and sending.
        '''
        customer_index = 1
        for customer in self.sheet.iter_rows(min_row=2): # Starts on the second row of the spreadsheet.

            # Assuming that the first column of the spreadsheet is made up of messages and the second is made up of phone numbers.
            message = customer[0].value
            phone = customer[1].value

            self.send_single_message(phone, message, delay_between_messages)
            print(f'Message successfully sent to the customer {customer_index}.')
            customer_index += 1
