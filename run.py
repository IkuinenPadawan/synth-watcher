import smtplib
from email.message import EmailMessage
import requests
import time
from bs4 import BeautifulSoup
import json


def fetch_and_send():
    EMAIL_ADDRESS = 'sender address'
    EMAIL_PASSWORD = 'password'


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
                # Find a better way to check all criteria words
                if 'volca' in classifieds[index]['Myydään'].lower() or 'moog' in classifieds[index]['Myydään'].lower() or 'dreadbox' in classifieds[index]['Myydään'].lower():
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
    send_email('recipient email', 'subject', result)