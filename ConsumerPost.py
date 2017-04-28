import parsedatetime
import re 
import pytz
from time import mktime
from pytz import timezone
from datetime import datetime
from kafka import KafkaConsumer
from PyPost import PyPost


class ConsumerPost:
	""" Clase consumidor, desde aqui se lee el topico de kafka
		y se guarda en postgres """

	def __init__(self, url, topic, urlPost, portPost):
		self.topic = topic
		self.url = url
		self.urlPost = urlPost
		self.portPost = portPost
		self.consumer = KafkaConsumer(topic,bootstrap_servers=[url])
		self.postsql = PyPost(urlPost, portPost)

	def sendData(self):
		# inicializacomos el parser

		p = parsedatetime.Calendar()
		
		for msg in self.consumer:
			# decodificamos
			sppls = str(msg.value.decode('utf8')).split(" ")
			
			# Condicion, si inicia con una ip lo manda a la tabla de apache 
			# caso contrario lo guarda en la tabla de log messages			
			if sppls[0] == '::1' or re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",sppls[0]):
				# asignamos valores basandonos en el indice del arreglo 

				chi = sppls[0]
				space1 = sppls[1]
				caun = sppls[2]
				fechita = sppls[3]
				fechita = fechita.replace("[", "")
				time_struct1, parse_status1 = p.parse(fechita)
				cqtd = datetime(*time_struct1[:6])
				cqtx_es = " "
				cqtx = (str(cqtx_es.join(sppls[5:8])))
				pssc = sppls[8]
				pscl = sppls[9]
				#mandamos los datos a postgres
				self.postsql.saveDataApache('dummydb','postgres','secretpass', chi, space1, caun, cqtd, cqtx, pssc, pscl)
			
			else:
				
				time_struct, parse_status = p.parse(str(msg.value))
				fecha = datetime(*time_struct[:6])
				fecha = str(fecha)
				cadena = str(msg.value)
				dirhost =  cadena.split(" ")[3]
				codeLog = cadena.split(" ")[4]
				logMessage = cadena.split(" ")[5:]
				es = " "
				#mandamos datos a postgres
				self.postsql.saveData('dbname','userpostgres','secretpass', fecha, dirhost, codeLog,str(es.join(logMessage)))


consu = ConsumerPost('localhost:9092','topic_name','localhost','5432')
consu.sendData()
