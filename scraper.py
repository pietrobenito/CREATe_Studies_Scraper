# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("http://www.ssrn.com/link/Intellectual-Property-Copyright-Law.html")

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
data = []
for linkText in root.cssselect("a[class='textlink']"):
  data.append({'title' : linkText.text_content(), 'url' : linkText.get('href')})


print data
scraperwiki.sqlite.save(unique_keys=['url'], data=data)

print scraperwiki.sqlite.show_tables()
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
