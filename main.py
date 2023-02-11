import tkinter
from tkinter import Tk,ttk
from tkinter import *

import messagebox
from pymsgbox import *


import requests
import json
import string



#cores
cor0 = '#000000' # preto
cor01 = '#fcfcfc' # branco
cor02 = '#668a62' # verde frame superior
cor03 = '#4bd938' # verde numeros
cor04 = '#5f8f59'# verde converter
cor05 = '#bababa' #cor fundo janela principal
cor06 = '#f0f0f0' # cor fundo frame de baixo


janela = Tk()
janela.title('Conversor de moedas via API')
janela.geometry('470x400')
janela.resizable(width=FALSE,height=FALSE)
janela.config(background=cor05)



#frame de cima
frame_cima = Frame(janela, width=460, height=80, background=cor02)
frame_cima.place(x=5,y=5)

l_title = Label(text=('Sistema de Conversão de moedas via API'),foreground=cor01, background=cor02, font=('verdana 14 bold'))
l_title.place(x=6, y=24)



#Frame de baixo
frame_debaixo = Frame(janela, width=458, height=380, background=cor06)
frame_debaixo.place(x=6, y=90)

l_inserir_valor = Label(frame_debaixo, text=('Insira o valor:'), foreground=cor0, background=cor06, font=('verdana 12'))
l_inserir_valor.place(x=10,y=10)

e_valor = Entry(frame_debaixo, width=25)
e_valor.place(x=135, y=12)

l_de = Label(frame_debaixo, text=('Converter de:'), foreground=cor0, background=cor06, font=('verdana 12'))
l_de.place(x=10, y=60)

l_para = Label(frame_debaixo, text=('Para:'), foreground=cor0, background=cor06, font=('verdana 12'))
l_para.place(x=250, y=60)



lista_moedas = ['USD', 'USDT', 'CAD', 'GBP', 'ARS', 'BTC', 'LTC', 'EUR', 'JPY', 'CHF', 'AUD', 'CNY', 'ILS', 'ETH', 'XRP', 'DOGE']

#Criando Combobox  ** DE ***
lista_moedas_entrada = lista_moedas
var01 = tkinter.StringVar()
combo_de = ttk.Combobox(frame_debaixo, textvariable=var01, width=10)
combo_de['values'] = lista_moedas
combo_de.place(x=130, y=60)



#Criando Combobox  ** PARA ***
lista_moedas_saida = lista_moedas
var02 = tkinter.StringVar()
combo_para = ttk.Combobox(frame_debaixo, textvariable=var02, width=10)
combo_para['values'] = lista_moedas
combo_para.place(x=300, y=60)








l_resultado = Label(frame_debaixo, text=('Resultado da conversão:'), foreground=cor0, background=cor06, font=('verdana 12'))
l_resultado.place(x=10,y=120)

l_resultado = Label(frame_debaixo, text="", width=20, height=4, font=('verdana 16 bold'), relief='raised', anchor='center', background=cor06, foreground=cor0)
l_resultado.place(x=80, y=150)


def calcular():

    cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
    cotacoes_dic = cotacoes.json()
    print(cotacoes_dic)

    valor01 = combo_de.get()
    formatar_valor01 = valor01.replace(",",".")
    valor01 = formatar_valor01

    valor02 = combo_para.get()
    formatar_valor02 = valor02.replace(",",".")
    valor02 = formatar_valor02


    multiplicador = e_valor.get()
    formatar_multiplicador = multiplicador.replace(",",".")
    multiplicador = formatar_multiplicador


    api1 = ('{}'.format(cotacoes_dic[valor01]['bid']))
    api2 =  ('{}'.format(cotacoes_dic[valor02]['bid']))

    print(api1)
    print(api2)


    conversao = float(api1) / float(api2) * float(multiplicador)
    print(conversao)



    l_resultado = Label(frame_debaixo, text=('{:.4f}'.format(conversao)), width=20, height=4, font=('verdana 16 bold'), relief='raised',
                        anchor='center', background=cor06, foreground=cor0)
    l_resultado.place(x=80, y=150)

    texto_resultado = Label(frame_debaixo, text=('De {} para {} sao:'.format(valor01,valor02)), width=20, height=1, font=('verdana 10 '),
                        anchor='center', background=cor06, foreground=cor0)
    texto_resultado.place(x=90, y=155)


bt_calcular = Button(frame_debaixo, text='Calcular', command=calcular)
bt_calcular.place(x=350, y=100)



janela.mainloop()