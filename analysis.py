#!/usr/bin/python2.7
# Udacity FSND Log Analytics Project

# import modules that we need
import datetime
import psycopg2
import time

DBNAME = "news"  # Our database name

db = psycopg2.connect(database=DBNAME)

# Query for Part 1
print("Running query to get the 3 most popular articles of all time...")
start1 = time.time()
c1 = db.cursor()
c1.execute("select a.title, count(*) as num from titles as a, articles as b" +
           " where b.slug like a.title group by a.title" +
           " order by num desc limit 3")
# c1.execute("select title, num from titles2 order by num desc limit 3")
rows1 = c1.fetchall()
print('...done in %.2f seconds' % (time.time() - start1))

# Query for Part 2
print("Running query to get the most popular authors ...")
start2 = time.time()
c2 = db.cursor()
c2.execute("select a.name, b.num from author_titles as b, authors as a where" +
           " b.author = a.id")
rows2 = c2.fetchall()
print('...done in %.2f seconds' % (time.time() - start2))

# Query for Part 3
print("Running query to find days with > 1% of requests with errors...")
start3 = time.time()
c3 = db.cursor()
c3.execute("select request_date, percent from final where percent > 1")
rows3 = c3.fetchall()
print('...done in %.2f seconds' % (time.time() - start3))

# Queries done, close the DB connection
db.close()

# Now we print the results
print("\nWhat are the most popular three articles of all time?")
for a in range(len(rows1)):
    print(" * {} - {} views").format(rows1[a][0], rows1[a][1])

print("\nWho are the most popular article authors of all time?")
for b in range(len(rows2)):
    print (" * {} - {} views").format(rows2[b][0], rows2[b][1])

print("\nOn which days did more than 1% of requests lead to errors?")
for c in range(len(rows3)):
    # Change the date format to be like July 2, 2018
    request_date = rows3[c][0]
    # Rounding the percentage to two decimals
    percent = round(rows3[c][1], 2)
    print(" * {} - {}% errors").format(request_date, percent)
