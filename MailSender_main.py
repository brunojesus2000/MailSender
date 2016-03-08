# -*- coding: UTF-8 -*-
#! /usr/bin/python

#Este codigo vai varrer uma lista especifica e mandar um email a todos que estão nela

import sys, os, smtplib, openpyxl


#Esta é a configuração de conexão com o servidor SMTP pelo modulo smtplib
gmailSMTP = smtplib.SMTP('smtp.gmail.com', 587)
gmailSMTP.ehlo()
gmailSMTP.starttls()

#Aqui você solicita os dados do usuário
SenderEmail = raw_input('Digite seu email: ')
SenderPwd = raw_input('Digite sua senha: ')
gmailSMTP.login(SenderEmail,SenderPwd)

#Aqui eu abro o documento xlsx pelo modulo openpyxl
PlanContatos = openpyxl.load_workbook('/Users/bruno/Documents/plan_teste.xlsx')
SheetContatos = PlanContatos.get_sheet_by_name('Plan1')
#Laço que percorre as celulas da planilha pela coluna
for cellObj in SheetContatos.columns[0]:
    print "Enviando email para", cellObj.value
    #Envio de modelo de email
    gmailSMTP.sendmail(SenderEmail, cellObj.value, 'Subject: Teste PyMail \nEste é um teste para envio de email pelo Python , seu endereço foi cadastrado na minha planilha' )
    print "Enviado com sucesso"
gmailSMTP.quit()


