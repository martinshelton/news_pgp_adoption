import urllib2, time
from bs4 import BeautifulSoup, SoupStrainer

#We're only going to look at <pre> HTML tags where the relevant data can be found.
only_pre_tags = SoupStrainer("pre")

# We scrape from the following list, using domains for our sample of 10 news orgs.
# Expect some "misses" -- especially for Forbes. We'll have to clean those later.
# I didn't realize it was such a popular last name until I started scraping.

# Our list
url_list = [
	'https://pgp.mit.edu/pks/lookup?search=cnn+com',
	'https://pgp.mit.edu/pks/lookup?search=nytimes+com',
	'https://pgp.mit.edu/pks/lookup?search=espn+com',
	'https://pgp.mit.edu/pks/lookup?search=huffingtonpost+com',
	'https://pgp.mit.edu/pks/lookup?search=foxnews.com',
	'https://pgp.mit.edu/pks/lookup?search=washingtonpost+com',
	'https://pgp.mit.edu/pks/lookup?search=washpost+com', # I found two different WaPo domains.
	'https://pgp.mit.edu/pks/lookup?search=buzzfeed+com',
	'https://pgp.mit.edu/pks/lookup?search=usatoday+com',
	'https://pgp.mit.edu/pks/lookup?search=forbes+com',
	'https://pgp.mit.edu/pks/lookup?search=cnet+com',
		]

# Iterate through our news orgs.
for org_url in url_list:
	ks_page = urllib2.urlopen(org_url).read()
	time.sleep(5)
	soup_b = BeautifulSoup(ks_page, 'html.parser', parse_only=only_pre_tags)
	print soup_b.get_text().encode('ascii', 'ignore')