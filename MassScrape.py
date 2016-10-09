'''
Created on Mar 27, 2016

@author: Jake Shulman
'''
import Scrape
from bs4 import BeautifulSoup
from urllib2  import urlopen
import urllib2
from selenium.common.exceptions import NoSuchElementException

INGREDIENTS=[]
RATINGS=[]
REVIEWS=[]
LINKS=[]
def instantiate(pageCount):
    URL = 'http://allrecipes.com/search/results/?wt=chocolate%20chip%20cookies&sort=re&page='+pageCount
    p = urllib2.build_opener(urllib2.HTTPCookieProcessor).open(URL)
    html= p.read()
    soup= BeautifulSoup(html,"html.parser")
    links=[]
    
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            if("/recipe" in str(link['href'])):
                links.append(str(link['href']))
    
    #print links
    links = links[links.index("/recipes/")+1:]
    links = set(links)
    links = list(links)
    print (links)
    links=set(links)
    links=list(links)
    for x in links:
        LINKS.append(x)
   
    for x in links:
            try:
                url="http://allrecipes.com"+x
                INGREDIENTS.append(Scrape.getIngredients(url))
                RATINGS.append(Scrape.getRating(url))
                REVIEWS.append(Scrape.getReviews(url))
            except urllib2.HTTPError,err:
                if err.code==301:
                    pass
            except NoSuchElementException, err:
                pass
            INGREDIENTS.append("*")
             
    # URL+=
                
if __name__ == '__main__':
    for x in range(1,5):
        instantiate(str(x))               
    print "Done"
    print len(INGREDIENTS)
    print len(RATINGS)
    print len(REVIEWS)
    print len(LINKS)
    
    #TO WRITE TO FILES UNCOMMENT THESE
    
#     with open('links.txt', 'w') as f:
#         for item in LINKS:
#                 f.write(item+"\n")
#         f.close()  
#     with open('ingredients.txt', 'w') as f:
#         for item in INGREDIENTS:
#             for x in item:
#                 f.write(x+"\n")
#         f.close() 
#     with open('ratings.txt', 'w') as f:
#         for item in RATINGS:
#             f.write(item+"\n")
#         f.close() 
#     with open('reviews.txt', 'w') as f:
#         for item in REVIEWS:
#             f.write(item+"\n")
#         f.close() 
    print "done"
    