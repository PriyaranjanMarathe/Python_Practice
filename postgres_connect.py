import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="test", user='postgresUser', password='postgresPW', host='localhost', port= '5455'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT FIRST_NAME, LAST_NAME, COUNTRY FROM CRICKETERS''')

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
