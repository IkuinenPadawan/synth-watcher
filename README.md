# Synth Watcher

A little dockerised web scraping script platform that sends every morning an email containing all the interesting synth classifieds depending on search words.

# Motivation

I got into synthesizers in late 2020 and if there is anything to know about synthesizer enthusiasm it is that there's always that one synth you need but don't have. That's why I found myself spending a lot of time monitoring a finnish music websites' synthesizer marketplace where people can buy and sell used synthesizers. It got me thinking could I automate the whole thing. I wrote a little Python script that I could run from my terminal. It was nice but I still had to manually run the script every time I wanted to check if something noteworthy had appeared on the marketplace. It got me thinking once more, could I run the script in the cloud and send myself an automatic email every morning that lists interesting classifieds.

## Build status

April 2022
First working test version released. Email message formatting needs work.

July 2023
Heroku free tier is no more so app was dockerised for ease of use in private or public cloud.

## Tech/framework used

- Python/Beautiful Soup
- Docker
- Cron

## Features

Cron job executes a python script on set interval that scrapes the muusikoiden.net marketplace (in the confines of robots.txt) for certain classifieds depending on given criteria and sends the summary to email every morning.

## How to use

Prerequisites:

- Docker installed
- Gmail account with app password enabled to send emails from that account

Set up container:

- Clone repository:

  ```
  $ git clone https://github.com/IkuinenPadawan/synth-watcher.git
  ```

- Change settings in config.ini

  ```
  [Settings]
  keywords = separated by comma
  from_email = gmail address sent from
  from_email_pw = app password for the above gmail
  to_email = email address sent to
  ```

- Modify crontab if interval to run the script needs to be changed

- Build container:
  ```
  $ docker build -t synth-watcher:latest .
  ```
- Run container:
  ```
  $ docker run -d synth-watcher
  ```

## Screenshots

Example of an automated email:

![Alt text](img/examplemail.JPG?raw=true "Example email")
