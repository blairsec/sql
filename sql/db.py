import sqlite3

db = sqlite3.connect('static.db')
c = db.cursor()

c.execute('CREATE TABLE users (username text, password text)')
c.execute('INSERT INTO users VALUES ("admin", "super_secure_password!!!")')

c.execute('CREATE TABLE sequels (title text, author text, rating integer)')
c.execute('INSERT INTO sequels VALUES ("Harry Potter and the Chamber of Secrets", "J. K. Rowling", 8)')
c.execute('INSERT INTO sequels VALUES ("Catching Fire", "Suzanne Collins", 4)')
c.execute('INSERT INTO sequels VALUES ("Exodus", "Moses", 1)')
c.execute('INSERT INTO sequels VALUES ("Point Blanc", "Anthony Horowitz", 5)')
c.execute('INSERT INTO sequels VALUES ("Prince Caspian", "C. S. Lewis", 6)')
c.execute('INSERT INTO sequels VALUES ("The Reptile Room", "Lemony Snicket", 6)')
c.execute('INSERT INTO sequels VALUES ("The Knight at Dawn", "Mary Pope Osborne", 2)')
c.execute('INSERT INTO sequels VALUES ("A Clash of Kings", "George R. R. Martin", 7)')
c.execute('INSERT INTO sequels VALUES ("Tintin in the Congo", "Herge", 10)')
c.execute('INSERT INTO sequels VALUES ("New Moon", "Stephenie Meyer", 3)')

c.execute('CREATE TABLE hidden_table (flag text)')
c.execute('INSERT INTO hidden_table VALUES ("flag{no_more_sqls_please}")')

db.commit()
db.close()