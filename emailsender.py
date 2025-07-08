import smtplib

to = input("Enter the email of recipent: \n")

content = input("Enter the content of the email: \n")

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com' , 'password') # Replace with your email and password
    server.sendmail('senderemail@gmail.com', to, content) # And enable your email to allow less secure apps(https://myaccount.google.com/lesssecureapps)
    server.close()

if __name__ == "__main__":
    send_email(to, content)
    print("Email sent successfully!")