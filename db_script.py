import psycopg2
import sys

# read all entries in table actore with given firstName and lastName
def read_db_entries(cursor, firstName, lastName):
    cursor.execute("SELECT * FROM actor WHERE first_name = %s AND last_name = %s", (firstName, lastName))
    lines = cursor.fetchmany()
    print(f'{len(lines)} result(s) for {firstName} {lastName}')
    for line in lines:
        print(line)
    return len(lines)

# insert new actore into table actor with given firstName and lastName
def insert_actor(cursor,  firstName, lastName):
    cursor.execute("INSERT INTO actor (first_name, last_name) VALUES (%s, %s)", (firstName, lastName))

# get first parameter 1 and 2 from command line. parameter 0 is the filename of the python script
firstName = sys.argv[1];
lastName = sys.argv[2];

print(f'Argument List: fist_name={firstName}, last_name={lastName}')

# connection with dvdrental database. Starts transaction 
connection = psycopg2.connect("dbname=dvdrental user=postgres password=postgrespw")
with connection:
    with connection.cursor() as cursor:
        amount = read_db_entries(cursor, firstName, lastName)
        if amount == 0:
            insert_actor(cursor, firstName, lastName)
            amount = read_db_entries(cursor, firstName, lastName)
            if amount == 1:
            ## commit transaction after new actor has been inserted
                connection.commit()
        else:
            print(f'{firstName} {lastName} existiert bereits')
        



