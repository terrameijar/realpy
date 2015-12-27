from urllib2 import urlopen
import re

my_address = "https://realpython.com/practice/dionysus.html"

html_page = urlopen(my_address)
html_text = html_page.read()

match_results = re.search("<title .*?>.*</title .*?>", html_text, re.IGNORECASE)
title = match_results.group()


#remove HTML tags
title = re.sub("<.*?>", "", title)
print title