import sqlite3

conn = sqlite3.connect('my_Factory.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS "workers_list" (
	"worker_id"	INTEGER PRIMARY KEY,
	"name"	TEXT,
	"birthday"	TIMESTAMP,
	"role"	TEXT,
	"first_working_day"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cur.execute("INSERT INTO 'workers_list' VALUES (1,'Дмитро Петров','11.01.1987','manufacture head','12.07.2020')")
cur.execute("INSERT INTO 'workers_list' VALUES (2,'Василь Карась','23.04.1991','manufacture master','25.09.2016')")
cur.execute("INSERT INTO 'workers_list' VALUES (3,'Сергій Ковальов','25.06.1992','manufacture worker','12.04.2017')")
cur.execute("INSERT INTO 'workers_list' VALUES (4,'Степан Ковальов','25.06.1992','manufacture worker','02.03.2022')")
cur.execute("INSERT INTO 'workers_list' VALUES (5,'Олег Мельник','22.11.1988','manufacture worker','25.09.2022')")
cur.execute("INSERT INTO 'workers_list' VALUES (6,'Давід Ольха','31.12.1982','stock head','27.11.2009')")
cur.execute("INSERT INTO 'workers_list' VALUES (7,'Михайло Корбан','11.11.2000','stock worker','26.09.2023')")
cur.execute("INSERT INTO 'workers_list' VALUES (8,'Юрій Стус','22.09.1999','stock worker','22.07.2016')")
cur.execute("INSERT INTO 'workers_list' VALUES (9,'Ірина Дубова','12.12.1991','sales manager','22.08.2019')")
cur.execute("INSERT INTO 'workers_list' VALUES (10,'Катерина Носова','31.07.1994','sales manager','09.09.2022')")
cur.execute("INSERT INTO 'workers_list' VALUES (11,'Галина Карпова','22.04.1989','sales top-manager','22.07.2016')")
cur.execute("INSERT INTO 'workers_list' VALUES (12,'Василь Голуб','24.04.1982','accounting head','12.04.2017')")
cur.execute("INSERT INTO 'workers_list' VALUES (13,'Марина Єрмак','30.10.1997','accounting worker','12.08.2019')")
cur.execute("INSERT INTO 'workers_list' VALUES (14,'Олена Іванова','06.11.1973','cleaning worker','25.09.2022')")
cur.execute("INSERT INTO 'workers_list' VALUES (15,'Ганна Гречка','28.12.1980','cleaning worker','21.11.2014')")


cur.execute('''CREATE TABLE IF NOT EXISTS "roles_list" (
	"role_id"	INTEGER PRIMARY KEY,
	"role"	TEXT,
	"hourly_wage"	REAL
);
''')

cur.execute("INSERT INTO 'roles_list' VALUES (1,'manufacture head','98')")
cur.execute("INSERT INTO 'roles_list' VALUES (2,'manufacture master','75.6')")
cur.execute("INSERT INTO 'roles_list' VALUES (3,'manufacture worker','49.3')")
cur.execute("INSERT INTO 'roles_list' VALUES (4,'stock head','82')")
cur.execute("INSERT INTO 'roles_list' VALUES (5,'stock worker','45.2')")
cur.execute("INSERT INTO 'roles_list' VALUES (6,'sales manager','39')")
cur.execute("INSERT INTO 'roles_list' VALUES (7,'sales top-manager','56.7')")
cur.execute("INSERT INTO 'roles_list' VALUES (8,'accounting head','95.2')")
cur.execute("INSERT INTO 'roles_list' VALUES (9,'accounting worker','45.2')")
cur.execute("INSERT INTO 'roles_list' VALUES (10,'cleaning worker','21')")

conn.commit()
conn.close()
