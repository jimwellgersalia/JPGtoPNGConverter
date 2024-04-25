import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_by_vote_rev(hnlist):
    # return the hn list sorted desc
    hnlist.sort(key=lambda k: k['votes'], reverse=True)
    return hnlist
    # return sorted.(hnlist, key=lambda k: k['votes'], reverse= True)


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


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
