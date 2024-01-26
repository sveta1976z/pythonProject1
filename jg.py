import sqlite3


con = sqlite3.connect('rrrrrr.db')
cursor = con.cursor()

cursor.execute("""CREATE TABLE sveta(namber INTENGEN, name text ,data text);""")

con.close()
git.init
