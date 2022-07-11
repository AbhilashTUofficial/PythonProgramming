
#! To help keep your account secure, from May 30, 2022, ​​Google no longer 
#! supports the use of third-party apps or devices which ask you to sign 
#! in to your Google Account using only your username and password.

#! For more information, continue to read.
#! "https://support.google.com/accounts/answer/6010255?authuser=2&hl=en&authuser=2&visit_id=637981302967246483-1697523380&p=less-secure-apps&rd=1#zippy=%2Cif-less-secure-app-access-is-on-for-your-account"

#? This is a old noob code of mine, its not going to work if you try it now because google changed there policy or whatever.

# Import modules
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import credentials
import time

def attachResume(filename,content):
    #? Open the attachment file for reading in binary mode, 
    #? and make it a MIMEApplication class

    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())

    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Attach the file to the content
    emailContent.attach(file_attachment)


#? Gather necessary informations.
#* password, Email address, resume, etc.
def gatherContent():

    global email
    global recEmail
    global password
    global content
    global resume
    global emailContent
    global emailId

    #? Fetch necessary data.
    recEmail=input("Receiver Email: ")
    password=input("Password: ")
    content = open("Automations/EmailSender/content.txt","r")
    emailId=credentials.email


    emailContent = MIMEMultipart()
    emailContent['From'] = emailId
    emailContent['To'] = recEmail
    emailContent['Subject'] = "Job Application"


    
    attachResume("Abhilash TU.pdf",emailContent)

    #? Conformation
    print(f"Sender : {emailId} \nReceiver: {recEmail}")
    print("\n\n"+content.read()+"\n")

    loading()

    _=input("Okayge? (Y/N) : ")
    if _.lower()== "y":
        saveCopy()
        return True 
    return False


#? Loding bar
def loading():
    green='\033[92m'
    bold='\033[1m'


    s='.'
    for i in range(100):
        time.sleep(0.1)
        if len(s)>10:
            s=str('.'*1)
        else:
            s='.'*(len(s)+1)

        print(f"{green}{bold}{s}{bold}{green}",end="\r")



#? Save a copy of the email for future refferences.
def saveCopy():

    f = open("Automations/EmailSender/copy.json", "a")
    f.write(f"{email,}\n{recEmail}\n{content}")
    f.close()

#? Send Email.
def sendEmail():
     #? Convert it as a string
    email_string = emailContent.as_string()

    # Connect to the Gmail SMTP server and Send Email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(emailId, password)
        server.sendmail(emailId, recEmail, email_string) 


if __name__=="__main__":
    if(gatherContent()):
        sendEmail()