from re import L
from sqlite3 import Cursor
import psycopg2
import sys

# read all entries in table actore with given firstName and lastName
def read_db_entries(cur: Cursor, firstName, lastName):
    cur.execute("SELECT * FROM actor WHERE first_name = %s AND last_name = %s", (firstName, lastName))
    lines = cur.fetchmany()
    print(f'{len(lines)} result(s) for {firstName} {lastName}')
    for line in lines:
        print(line)
    return len(lines)

# insert new actore into table actor with given firstName and lastName
def insert_actor(cur: Cursor,  firstName, lastName):
    cur.execute("INSERT INTO actor (first_name, last_name) VALUES (%s, %s)", (firstName, lastName))

# get first parameter 1 and 2 from command line. parameter 0 is the filename of the python script
firstName = sys.argv[1];
lastName = sys.argv[2];

print(f'Argument List: fist_name={firstName}, last_name={lastName}')

# connection with dvdrental database. Starts transaction 
conn = psycopg2.connect("dbname=dvdrental user=postgres password=postgrespw")
with conn:
    with conn.cursor() as cur:
        amount = read_db_entries(cur, firstName, lastName)
        if amount == 0:
            insert_actor(cur, firstName, lastName)
            amount = read_db_entries(cur, firstName, lastName)
            if amount == 1:
            ## commit transaction after new actor has been inserted
                conn.commit()
        



