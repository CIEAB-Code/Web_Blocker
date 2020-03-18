from datetime import datetime as dt
import time
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_path_temp = "hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "mail.google.com", "www.mail.google.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()


    time.sleep(5)

