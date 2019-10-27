import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("rovanova.nuthan@gmail.com", "rovanova7@")

# message to be sent
message = "Hola, amigo. Testing mail"

# sending the mail
s.sendmail("rovanova.nuthan@gmail.com","nuthanchandra1997@gmail.com", message)

# terminating the session
s.quit()
