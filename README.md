# Synth Watcher
A little web scraping script running on Heroku cloud platform that sends every morning an email containing all the interesting synth classifieds depending on search words.

# Motivation
I got into synthesizers in late 2020 and if there is anything to know about synthesizer enthusiasm it is that there's always that one synth more you need but don't have. That's why I found myself spending a lot of time monitoring a finnish music websites' synthesizer marketplace where people can buy and sell used synthesizers. It got me thinking could I automate the whole thing. I wrote a little Python script that I could run from my terminal. It was nice but I still had to manually run the script every time I wanted to check if something noteworthy had appeared on the marketplace. It got me thinking, could I run the script in the cloud and send myself an automatic email every morning that lists interesting classifieds.

## Build status
First working test version released.

## Tech/framework used
- Python/Beautiful Soup
- Heroku cloud platform

## Features
Python script running in the cloud scrapes the muusikoiden.net marketplace (in the confines of robots.txt) for certain classifieds depending on given criteria and sends the summary to email every morning.
