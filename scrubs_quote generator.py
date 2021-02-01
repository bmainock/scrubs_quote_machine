import pyttsx3
import os
import requests
import random
from bs4 import BeautifulSoup


def theQuotes():
    response = requests.get('https://www.quotes.net/movies/scrubs_106070')

    #response = requests.get(webaddress)
    soup = BeautifulSoup(response.text, 'html.parser')

    # direct
    snippet = soup.find_all(class_='disp-mquote-int')

    # p = soup.find_all('p')

    paragraphs = []
    for x in snippet:
        paragraphs.append(str(x))

    paragraphs.pop()
    print(len(paragraphs))

    for y in range(len(paragraphs)):
        paragraphs[y] = paragraphs[y].replace('<p>', '')
        paragraphs[y] = paragraphs[y].replace('</p><strong>', '')
        paragraphs[y] = paragraphs[y].replace('</p>', '')
        paragraphs[y] = paragraphs[y].replace('</strong><br/>', '')
        paragraphs[y] = paragraphs[y].replace('<strong>', '')
        paragraphs[y] = paragraphs[y].replace('<a href="/mquote/"><strong>', '')
        paragraphs[y] = paragraphs[y].replace('<div class="disp-mquote-int">', '')
        paragraphs[y] = paragraphs[y].replace('</a>\n</div>', '')
        paragraphs[y] = paragraphs[y][26:]
        print(paragraphs[y], "\n")
        #to print every quote on the list uncomment the code above

    # Navigation

    scrubs_quote = pyttsx3.init()
    scrubs_quote.say(random.choice(paragraphs))
    scrubs_quote.runAndWait()


if __name__ == '__main__':
    theQuotes()