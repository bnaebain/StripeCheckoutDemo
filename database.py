import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table
conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		houseNumber TEXT,
		street TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT,
		currency TEXT,
		customerID TEXT
		)''')

conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT
		)''')

conn.execute('''CREATE TABLE kart
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.execute('''CREATE TABLE paymentMethods
		(userId INTEGER,
		pm1 TEXT,
		pm2 TEXT,
		pm3 TEXT,
		pm4 TEXT,
		pm5 TEXT,
		pm6 TEXT,
		pm7 TEXT,
		pm8 TEXT,
		pm9 TEXT,
		pm10 TEXT,
		pm11 TEXT,
		pm12 TEXT,
		pm13 TEXT,
		pm14 TEXT,
		pm15 TEXT,
		FOREIGN KEY(userId) REFERENCES users(userId)
		)''')

conn.close()

