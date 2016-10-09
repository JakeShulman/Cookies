# Cookies

Scrape.py goes to a given allrecipes.com url, converts all values to metric system, sets batch size to 48, and returns a list of ingredients with associated amounts. In addition, it pulls the number of reviews, and rating. 

MassScrape.py finds all cookie recipes on allrecipes (approximately 1700) and runs scrape on all of them, writing the values to text files, which I have included. 

Still need to format data further by removing recipes that have too few ratings, or that have odd ingredients. 

Plan on implementing a filter that removes all recipes that have an ingredient that is not common to some percentage of all acceptable cookies. 

After data is cleaned and further formatted, I will use it as a ML data set to attempt to find the "perfect" cookie recipe. 
