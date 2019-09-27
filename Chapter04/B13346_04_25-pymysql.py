# Create spatial database in MySQL

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='mysql')

cur = conn.cursor()

cur.execute("DROP DATABASE IF EXISTS spatial_db")

cur.execute("CREATE DATABASE spatial_db")

cur.close()

conn.close()

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='spatial_db')

cur = conn.cursor()

cur.execute("CREATE TABLE PLACES (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, Name varchar(50) NOT NULL, location Geometry NOT NULL)")

cur.execute("INSERT INTO PLACES (name, location) VALUES ('NEW ORLEANS', ST_GeomFromText('POINT(30.03 90.03)'))")

cur.execute("INSERT INTO PLACES (name, location) VALUES ('MEMPHIS', ST_GeomFromText('POINT(35.05 90.00)'))")

conn.commit()

cur.execute("SELECT ST_AsText(location) FROM PLACES")

p1, p2 = [p[0] for p in cur.fetchall()]

cur.execute("SET @p1 = ST_GeomFromText('{}')".format(p1))
cur.execute("SET @p2 = ST_GeomFromText('{}')".format(p2))

cur.execute("SELECT ST_Distance(@p1, @p2)")

d = float(cur.fetchone()[0])
print("{:.2f} miles from New Orleans to Memphis".format(d * 70))


cur.close()

conn.close()