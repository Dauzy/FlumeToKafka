import psycopg2


class PyPost:
	"""docstring for PyPost"""
	def __init__(self, url, portToPost):
		self.url = url
		self.portToPost = portToPost
		
	def saveData(self, dbname, usrdb, pswd, logs_date, logs_hots, logs_code,logs_message):
		global conn 

		try:
			#print(dbname+"  "+usrdb+" "+pswd+" "+self.url+" "+self.portToPost)
			conn = psycopg2.connect(database=dbname, user = usrdb, password = pswd, host = self.url, port = self.portToPost)
			print("Opened database successfully")
		except BaseException as e:
			print("Can't Opened database.")

		

		try:
			query = "INSERT INTO DUMMYLOGS VALUES (default, %s, %s, %s, %s)"
			data = (logs_date,logs_hots, logs_code, logs_message)
			cur = conn.cursor()
			cur.execute(query,data)
			conn.commit()
			print("Data is write!")
			
		except BaseException as e: 
			print("can't connecto to db: ERROR ", e)

#		rows = cur.fetchall()
#		for row in rows:
#			print("   ",row)

	def saveDataApache(self, dbname, usrdb, pswd, logs_chi, logs_space, logs_caun, logs_cqtd, logs_cqtx, logs_pssc, pscl):
		global conn 

		try:
			conn = psycopg2.connect(database=dbname, user = usrdb, password = pswd, host = self.url, port = self.portToPost)
			print("Opened database successfully")
		except BaseException as e:
			print("Can't Opened database.")

		try:
			query = "INSERT INTO APACHEDUMMYLOGS2 VALUES (default, %s, %s,%s, %s, %s, %s, %s)"
			data = (logs_chi, logs_space,logs_caun, logs_cqtd, logs_cqtx, logs_pssc, pscl)
			cur = conn.cursor()
			cur.execute(query,data)
			conn.commit()
			print("APACHE: Data is write!")
			
		except BaseException as e: 
			print("can't connecto to db: ERROR ", e)
#prueba = PyPost('127.0.0.1','5432')
#prueba.saveData('dummydb','postgres','secretpass', '2017-04-26 16:03:50','localhost','fprintd: ** Message: entering main loop')