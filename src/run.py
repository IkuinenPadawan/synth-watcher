import smtplib
from email.message import EmailMessage
import requests
import time
from bs4 import BeautifulSoup
import json
import configparser
import os

def fetch_and_send(settings):
    EMAIL_ADDRESS = settings['from_email']
    EMAIL_PASSWORD = settings['from_email_pw']

    baseUrl = "https://muusikoiden.net"

    next_page = "/tori/?type=sell&category=31"

    classifieds = []
    content = []

    def get_classifieds():
        classifieds = []
        for table in tables:
            try:
                title = table.find(class_="tori_title").get_text()
                price = table.find("td", colspan = 2).find("p").get_text()
                title = title.split(':')
                price = price.split(':')
                link = table.find(class_="tori_title").find("a")['href']
                link = baseUrl + link
                obj = {
                    title[0]: title[1].strip(),
                    price[0]: price[1].strip(),
                    "url": link
                }
                classifieds.append(obj)
            except:
                None
        return classifieds

    def check_if_next_page_exists(soup):
        links = soup.find_all("a", href=True)

        for link in links:
            if link.get_text() == "seuraava sivu »":
                return link['href']
                break


    # Scrape until there is no next page
    while (next_page is not None):
        response = requests.get(f"{baseUrl}{next_page}")
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table", cellpadding = 2)
        classifieds = get_classifieds()
        next_page = check_if_next_page_exists(soup)
        for index in range(len(classifieds)):
            for key in classifieds[index]:
                for synth in settings['keywords']:
                    if synth in classifieds[index]['Myydään'].lower():
                        match = classifieds[index][key]
                        content.append(match)
        # Sleep 10s before changing page as per robots.txt
        time.sleep(10)


    def send_email(recipient, subject, body):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient
        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.send_message(msg)

    result = json.dumps(content, indent=4)

    # Finally send results
    send_email(settings['to_email'], 'subject', result)

def get_settings():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

    config.read(config_path)

    if 'Settings' in config.sections():
        return {
            'keywords': config.get('Settings', 'keywords').split(', '),
            'from_email': config.get('Settings', 'from_email'),
            'from_email_pw': config.get('Settings', 'from_email_pw'),
            'to_email': config.get('Settings', 'to_email')
        }
    else:
        return None

if __name__ == "__main__":
    settings = get_settings()
    fetch_and_send(settings)
