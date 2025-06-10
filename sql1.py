import sqlite3

conn = sqlite3.connect('customer.db')
cursor = conn.cursor()

#create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id integer primary key AUTOINCREMENT,
    name text NOT NULL,
    age INTEGER NOT NULL,
    email TEXT  NOT NULL UNIQUE)
               ''')

#insert data
customers= [
    ('john', 20, 'john@gmail.com'),
    ('jane', 22, 'jane@gmail.com'),
    ('doe', 33, 'doe@gmail.com'),
    ('alice', 34,'alice@gmail.com')
]
cursor.executemany('''
     INSERT OR IGNORE INTO customers (name,age,email) VALUES (?,?,?)
    ''', customers)

#commit changes and fetch data
conn.commit()
cursor.execute("select * from customers")
print(cursor.fetchall())
print(cursor.fetchone())

cursor.execute("SELECT name,email FROM customers WHERE age >30")
older_cust =cursor.fetchall()
print("\n customers over 30")
for customer in older_cust:
    print(customer)

#GET RESULTS AS PANDAS DATAFRAME
import pandas as pd
df = pd.read_sql_query("SELECT name FROM customers WHERE  age > 20",conn)
print("\nData as Dataframe:")
print(df)

#update data
cursor.execute("UPDATE customers SET age = ? WHERE name = ?", (45, 'alice'))
conn.commit()
#check updated data
cursor.execute("SELECT * FROM customers WHERE name = 'alice'")
print("\nUpdated data for alice:")

#delete data
cursor.execute("DELETE FROM customers where name = 'jane'")
conn.commit()
print("\nData after deletion:")
print(cursor.fetchall())


print("Data inserted successfully!") 
conn.close()