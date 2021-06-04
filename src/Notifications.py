import webbrowser
import smtplib
from playsound import playsound

KEY_WORD = 'Online In Stock'
# Need to initialize these
MP3_PATH =
GMAIL_SENDER = 
GMAIL_PASSWORD = 

class Notifications:
    def sendEmail(self, url):
        try:
            server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server_ssl.ehlo()
            server_ssl.login(GMAIL_SENDER, GMAIL_PASSWORD)  
            server_ssl.sendmail(GMAIL_SENDER, GMAIL_SENDER, 'ITS HERE MOTHERFUCKER ' + url)
            server_ssl.sendmail(GMAIL_SENDER, 'meetinderlail@yahoo.ca', 'ITS HERE MOTHERFUCKER ' + url)
            server_ssl.sendmail(GMAIL_SENDER, 'brittany.naeckel@gmail.com', 'ITS HERE MOTHERFUCKER ' + url)
            server_ssl.close()
            print('Successfully sent the mail')
        except:
            print('Error occurred while sending email')

    def openBrowser(self, url):
         webbrowser.open(url)

    def playSound(self):
        playsound(MP3_PATH)
