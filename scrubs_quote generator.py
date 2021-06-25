import pyttsx3
import os
import requests
import random
from bs4 import BeautifulSoup

def theQuotes():

    response = requests.get('https://www.quotes.net/movies/scrubs_106070') #Website with best list of quotes
    copied_site = BeautifulSoup(response.text, 'html.parser')

    html_quote_snippets = copied_site.find_all(class_='disp-mquote-int')
    quote_list = []

    for x in html_quote_snippets:
        quote_list.append(str(x))
    quote_list.pop()
    #print(len(quote_list))
    for y in range(len(quote_list)):
        quote_list[y] = quote_list[y].replace('<p>', '')
        quote_list[y] = quote_list[y].replace('</p><strong>', '')
        quote_list[y] = quote_list[y].replace('</p>', '')
        quote_list[y] = quote_list[y].replace('</strong><br/>', '')
        quote_list[y] = quote_list[y].replace('<strong>', '')
        quote_list[y] = quote_list[y].replace('<a href="/mquote/"><strong>', '')
        quote_list[y] = quote_list[y].replace('<div class="disp-mquote-int">', '')
        quote_list[y] = quote_list[y].replace('</a>\n</div>', '')
        quote_list[y] = quote_list[y][26:]
        #print(quote_list[y], "\n")
        #to print every quote on the list uncomment the code above

    # Navigation
    chosen_one = random.choice(quote_list)
    print(chosen_one)
    scrubs_quote = pyttsx3.init()
    scrubs_quote.say(chosen_one)
    scrubs_quote.runAndWait()


if __name__ == '__main__':
    theQuotes()