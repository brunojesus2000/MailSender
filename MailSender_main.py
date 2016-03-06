# -*- coding: UTF-8 -*-
#! /usr/bin/python

#Este codigo vai varrer uma lista especifica e mandar um email a todos que estão nela

import sys, os, smtplib

#Esta é a configuração de conexão com o servidor SMTP
gmailSMTP = smtplib.SMTP('smtp.gmail.com', 587)
gmailSMTP.ehlo()
gmailSMTP.starttls()

#Aqui você solicita os dados do usuário
SenderEmail = raw_input('Digite seu email: ')
SenderPwd = raw_input('Digite sua senha: ')
gmailSMTP.login(SenderEmail,SenderPwd)

gmailSMTP.sendmail(SenderEmail, 'brunojesus2000@yahoo.com.br', 'Subject: Teste PyMail \nEste é um teste para envio de email pelo Python ' )
gmailSMTP.quit()
