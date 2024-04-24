import requests
from bs4 import BeautifulSoup
import pprint

web_add = 'https://news.ycombinator.com/'
for pages in range(1, 4):  # get how many pages you want by replacing the stop
    res = requests.get(web_add + '/?p=' + str(pages))
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline > a')
    subtext = soup.select('.subtext')


def sort_by_vote_rev(hnlist):
    # return the hn list sorted desc
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        if 'item?id=' in href:  # this will check if the href is not given a link and only posted it on hacker news
            href = res.url + href
        vote = subtext[idx].select('.score')
        if len(vote):
            # getting the value of subtext and converting to int
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_by_vote_rev(hn)


pprint.pprint(create_custom_hn(links, subtext))
