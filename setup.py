from setuptools import setup, find_packages

setup(
    name='whatsapp-bot',
    version='0.1.0',
    author='Cauã Santos, Arthur Camboim',
    description='Bot para envio de mensagens via WhatsApp Web com base em planilha Excel',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'openpyxl',
        'pyautogui',
        'pyperclip'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
