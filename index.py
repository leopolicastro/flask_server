from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import pprint

app = Flask(__name__)

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return jsonify(sort_stories_by_votes(hn))

@app.route('/')
def display():
  res = requests.get('https://news.ycombinator.com/news')
  res2 = requests.get('https://news.ycombinator.com/news?p=2')
  soup = BeautifulSoup(res.text, 'html.parser')
  soup2 = BeautifulSoup(res2.text, 'html.parser')
  links = soup.select('.storylink')
  subtext = soup.select('.subtext')
  links2 = soup2.select('.storylink')
  subtext2 = soup2.select('.subtext')
  mega_links = links + links2
  mega_subtext = subtext + subtext2

  return create_custom_hn(mega_links, mega_subtext)

if __name__=='__main__':
    app.run(debug=True, port=8080)