#!/usr/bin/env python3

import psycopg2
# Three Most popular articles
ques_1 = ("A. What are the most popular three articles of all time? ")
query_1 = (
    "select a.title, count(*) as v "
    "from articles a "
    "inner join "
    "log l "
    "on l.path like concat('%', a.slug) "
    "group by a.title order by v desc limit 3"
    )
# Most popular article  authors
ques_2 = ("B. Who are the most popular article authors of all time? ")
query_2 = (
    "select au.name, count(*) as v "
    "from articles a "
    "inner join "
    "authors au "
    "on a.author = au.id "
    "inner join "
    "log l "
    "on l.path like concat('%', a.slug)"
    "group by au.name order by v desc"
    )
# The days when more than 1% of requests lead to errors
ques_3 = ("C. On which days did more than 1% of requests lead to errors? ")
query_3 = (
    "select * from ("
    "select a.day,"
    "round(cast((100*b.hits) as numeric) / cast(a.hits as numeric),1)"
    " as errp "
    "from(select date(time) as day, count(*) as hits from log group by day)"
    " as a "
    "inner join "
    "(select date(time) as day, count(*) as hits from log"
    " where status like '%404%' group by day) as b "
    "on a.day = b.day) "
    "as t where errp > 1.0"
    )


# Function to connect to the PostgreSQL database and return connection
def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except Exception:
        print("Could not connect to the database")


# Function to return query results
def get_query(query):
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


# Function to display query results of 1 & 2
def display_1_2(q_results):
    # displaying title
    print("\n", q_results[1])
    # displaying actual result
    for i, results in enumerate(q_results[0]):
        print("   ", i+1, ":", results[0], " :- ", str(results[1])+" views")


# Function to display query result of 3
def display_3(q_result):
    # displaying title
    print("\n", q_result[1])
    # displaying actual result
    for results in q_result[0]:
        print("   ", results[0], ":-", str(results[1])+"% errors\n")


if __name__ == '__main__':
    popular_articles = get_query(query_1), ques_1
    popular_authors = get_query(query_2), ques_2
    error_days = get_query(query_3), ques_3
    display_1_2(popular_articles)
    display_1_2(popular_authors)
    display_3(error_days)
