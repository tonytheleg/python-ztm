import requests
from bs4 import BeautifulSoup
import pprint

# yeah yeah, lots of comments, im learning
# grab the story titles and links for stories with more than 100 points
res = requests.get('https://news.ycombinator.com/news')
res_pg2 = requests.get('https://news.ycombinator.com/news?p=2')

# parses the  HTML into a list
soup = BeautifulSoup(res.text, 'html.parser')
soup_pg2 = BeautifulSoup(res.text, 'html.parser')

# using select to find just the storylink classes in html
links = soup.select('.storylink')
links_pg2 = soup.select('.storylink')

# using select to find just the subtext classes in html
subtext = soup.select('.subtext')
subtext_pg2 = soup.select('.subtext')

all_links = links + links_pg2
all_subtext = subtext + subtext_pg2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    '''
    For each link found, grabs the title, grabs the url, and grabs the vote but only
    for stories with more than 100 points
    '''
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))    
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(all_links, all_subtext))