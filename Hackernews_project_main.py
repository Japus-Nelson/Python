import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')    # Requests to use to get the html file from the webpage
next_page = requests.get('https://news.ycombinator.com/?p=2')
print(res, next_page)        # prints the response code if success! it has collected the data.


soup = BeautifulSoup(res.text, 'html.parser')        # (htmldata, 'parser')
# Later we can manipulate the data as per the requirement,
# Parser is something that cleans the unwanted data and helps convert string to object.
soup1 = BeautifulSoup(next_page.text, 'html.parser')


# l  Grabbing the class titleline
link1 = soup.select('.titleline')  # For just the link, use soup.a['href']) or for getting whole line use the code
link2 = soup1.select('.titleline')

# 5 either combine both the links, to view it in the same page
mega_link = link1 + link2

# 2. Grabbing the class subtext
votes1 = (soup.select('.subtext'))    # score gives the no of votes the link has got.
votes2 = soup1.select('.subtext')

# 6. Same like links, combine the votes
mega_votes = votes1 + votes2


# 4. sorting the based on high number of votes.


def sort_stories_by_points(hackernews):
    return sorted(hackernews, key=lambda x: x['votes'], reverse=True)    # sorting based on high votes
# 5. Create a custom Hackernews that filters the content based on the votes.


def custom_hacker_news(link, votes):
    hacker_news = []
    for index, links in enumerate(link):
        title = links.getText()
        title_link = links.a['href']
        vote = votes[index].select('.score')
        if len(vote):                             # see if score exists, else ignore
            vote_numbers = int(vote[0].getText().replace(' points', ''))
            if vote_numbers > 100:           # Printing the title, link, and votes only if satisfies the condition.
                hacker_news.append({'title': title,
                                   'Links': title_link,
                                    'votes': vote_numbers})
    return sort_stories_by_points(hacker_news)      # calling the function that performs the sorting.


pprint.pprint(custom_hacker_news(link1, votes1))    # first page
pprint.pprint(custom_hacker_news(link2, votes2))    # second page # pretty print makes our output looks good.
pprint.pprint(custom_hacker_news(mega_link, mega_votes))   # Both Pages

# Look at scrapy for scrapping huge website.
# Collect the data and store it somewhere in the db.
