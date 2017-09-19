# Import psycopg2 as the PostGREsql engine
import psycopg2

# Create a connection to the news database
conn = psycopg2.connect(database='news')

# Create a cursor to search database
cur = conn.cursor()

# First query: Joining log with articles if the article's slug
# is present in the log's path.
# Groups by articles.title since each article is reached through
# multiple paths
# DESC to get highest number of views first
# Limits to 3 for Top 3 articles
cur.execute("""
    SELECT articles.title, count(*)
    FROM log
    JOIN articles
    ON log.path LIKE CONCAT('%',articles.slug,'%')
    GROUP BY articles.title
    ORDER BY count(*)
    DESC
    LIMIT 3;""")

# Begin output
print "**********"
print "The three most popular articles are:"

# Fetches result and iterates through (outputs) each
# as Article Title - 888888 views
rows = cur.fetchall()
for row in rows:
    print str(row[0]) + " - " + str(row[1]) + " views"
print "**********"

# Second query: Joins log and articles to count total views
# of each articles.author,
# then joins with table 'authors' to ascribe a name to each row.
# This list of Author Name and Total view count is sorted so
# that more-viewed authors are listed first.
cur.execute("""
    SELECT authors.name, A.count
    FROM authors
    JOIN (     (SELECT articles.author, count(*)
                FROM log
                JOIN articles
                ON log.path LIKE CONCAT('%',articles.slug,'%')
                GROUP BY articles.author)
         ) A
    ON authors.id=A.author
    ORDER BY A.count
    DESC
;""")

# Fetches result and iterates through (outputs) each
# as Author Name - 88888 views
rows = cur.fetchall()
print "The most popular authors, in order of pageviews, are:"
for row in rows:
    print str(row[0]) + " - " + str(row[1]) + " views"
print "**********"

# Third query: Uses two subqueries
# Subquery 1 returns the number of 404 errors per date
# Subquery 2 returns the total number of requests per dare
# These two tables are joined on 'Date"
# and then the percent of failures is calculated and only returned
# if it's more than 1%
cur.execute("""
    SELECT C.d, C.percentfailed*100
    FROM (      SELECT A.d, CAST(A.fails as float)/B.reqs as percentfailed
                FROM (      SELECT DATE(time) as d, count(*) as fails
                            FROM log
                            WHERE status='404 NOT FOUND'
                            GROUP BY DATE(time)
                     ) A
                JOIN (
                            SELECT DATE(time) as d, count(*) as reqs
                            FROM log
                            GROUP BY DATE(time)
                     ) B
                ON A.d=B.d
         ) C
    WHERE C.percentfailed>0.01;
""")

# Fetches result and iterates through (outputs) each
# as Author Name - 88888 views
rows = cur.fetchall()
print "Days on which the server failure rate was more than 1%:"
for row in rows:
    print str(row[0]) + " - " + str(row[1]) + "%"
print "**********"

# Marks end of calculations
print "End of output"

# Close cursor
cur.close()

# Close connection
conn.close()
