# -*- coding: UTF-8 -*-
#! /usr/bin/python

#TODO: Este codigo vai varrer uma lista especifica e mandar um email a todos que estão nela

#Importando modulo de SMTP(smtplib), de leitura de Excel(openpyxl)
import smtplib, openpyxl

# Importando modulos de email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Aqui eu abro o documento xlsx pelo modulo openpyxl
PlanContatos = openpyxl.load_workbook('/Users/bruno/Documents/plan_teste.xlsx')
SheetContatos = PlanContatos.get_sheet_by_name('Plan1')

#Esta é a configuração de conexão com o servidor SMTP pelo modulo smtplib
gmailSMTP = smtplib.SMTP('smtp.gmail.com', 587)
gmailSMTP.ehlo()
gmailSMTP.starttls()

#Aqui você solicita os dados do usuário
SenderEmail = raw_input('Digite seu email: ')
SenderPwd = raw_input('Digite sua senha: ')

#Login no SMTP
gmailSMTP.login(SenderEmail,SenderPwd)


#Laço que percorre as celulas da planilha pela coluna
for cellObj in SheetContatos.columns[0]:

    # Construção do email
    addr_to = cellObj.value
    msg = MIMEMultipart('alternative')
    msg['From'] = SenderEmail
    msg['To'] = addr_to
    msg['Subject'] = 'Test Email From RPi'

    # Criando o corpo da mensagem (um texto plano e uma versão HTML).
    text = "Esta é uma mensagem de teste.\nTexto e HTML."
    html = """\
    <html>
      <head><title>Infosolution</title></head>
      <body>
        Não consegue visualizar?<a href="http://meninoapple.com/wp-content/uploads/2016/01/profile-image-display.png">clique aqui</a>!<br>
        <img src="http://meninoapple.com/wp-content/uploads/2016/01/profile-image-display.png" />
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    print "Enviando email para", cellObj.value
    #Envio de modelo de email
    gmailSMTP.sendmail(SenderEmail, addr_to, msg.as_string())
    print "Enviado com sucesso"
gmailSMTP.quit()