# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki,lxml.html,sqlite3,urllib
#
# # Read in a page
html = scraperwiki.scrape("http://www.ssrn.com/link/economics-entrepreneurship.html")

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
data = []
for linkText in root.cssselect("a[class='textlink']"):
  data.append({"title" : linkText.text_content().encode('utf-8'), "url" : linkText.get('href').encode('utf-8')})

for row in data:
  print row['title'].decode("ascii", "ignore")
  scraperwiki.sqlite.save(unique_keys=['url'], data={"title" : row['title'].decode("ascii", "ignore"), "url" : row['url'].decode("ascii", "ignore")})
#  scraperwiki.sqlite.save(unique_keys=['url'], data={"title" : "test123", "url" : "test456"})
#scraperwiki.sqlite.save(unique_keys=['url'], data=data)
#scraperwiki.sqlite.save(unique_keys=['url'], data={"title":"test123","url":"test456"})
#scraperwiki.sqlite.save(unique_keys=['a'], data={"a":1, "bbb":"Hi there"})


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
