import pyttsx3
import os
import requests
import random
from multiprocessing import Process

from bs4 import BeautifulSoup


def theQuotes(webaddress):
    #response = requests.get('https://www.quotes.net/movies/scrubs_106070')

    response = requests.get(webaddress)
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
    # to print every quote on the list uncomment the code above

    # Navigation

    #scrubs_quote = pyttsx3.init()
    #scrubs_quote.say(random.choice(paragraphs))
    #scrubs_quote.runAndWait()


if __name__ == '__main__':
    print("check check")
    p10 = Process(target=theQuotes, args=('https://www.quotes.net/movies/scrubs_106070',))

    p10.start()
    # p = Process(target=theQuotes, args=('https://www.quotes.net/show/scrubs_,_season_1_1423',))
    # p1 = Process(target=theQuotes, args=('https://www.quotes.net/show/scrubs_,_season_2_1424',))
    # p2 = Process(target=theQuotes, args=('https://www.quotes.net/show/scrubs_,_season_3_1425',))
    # p3 = Process(target=theQuotes, args=('https://www.quotes.net/show/scrubs_,_season_4_1426',))
    # p4 = Process(target=theQuotes, args=('https://www.quotes.net/show/scrubs_,_season_5_1427',))
    # p5 = Process(target=theQuotes, args=('https://www.quotes.net/show/scrubs_,_season_6_1428',))
    # p6 = Process(target=theQuotes, args=('https://www.quotes.net/show/scrubs_,_season_7_1429',))
    # p7 = Process(target=theQuotes, args=('https://www.quotes.net/show/scrubs_,_season_8_1430',))
    # p8 = Process(target=theQuotes, args=('https://www.quotes.net/show/scrubs_,_season_9_1431',))
    #p.start()
    #p1.start()
    #p2.start()
    #p3.start()
    #p4.start()
    #p5.start()
    #p6.start()
    #p7.start()
    #p8.start()
