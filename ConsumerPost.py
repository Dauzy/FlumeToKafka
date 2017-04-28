import parsedatetime
import re 
import pytz
from time import mktime
from pytz import timezone
from datetime import datetime
from kafka import KafkaConsumer
from PyPost import PyPost


class ConsumerPost:

	def __init__(self, url, topic, urlPost, portPost):
		self.topic = topic
		self.url = url
		self.urlPost = urlPost
		self.portPost = portPost
		self.consumer = KafkaConsumer(topic,bootstrap_servers=[url])
		self.postsql = PyPost(urlPost, portPost)

	def sendData(self):

		p = parsedatetime.Calendar()
		
		for msg in self.consumer:
			
			#cadena = str(msg.value)
			#print(">>>>>>>>>completo")
			#print(str(msg.value.decode('utf8')))
			sppls = str(msg.value.decode('utf8')).split(" ")
			
			if sppls[0] == '::1' or re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",sppls[0]):
				
				print(">>>>>>>>>>>APACHE")
				#print("dir: "+sppls[0])
				chi = sppls[0]
				space1 = sppls[1]
				caun = sppls[2]
				fechita = sppls[3]
				fechita = fechita.replace("[", "")
				#print(">>>>>>>>"+fechita)
				time_struct1, parse_status1 = p.parse(fechita)
				#print(time_struct1)
				print(">>>>>"+fechita)
				cqtd = datetime(*time_struct1[:6])
				cqtx_es = " "
				cqtx = (str(cqtx_es.join(sppls[5:8])))
				# print(sppls)
				pssc = sppls[8]
				pscl = sppls[9]
				print(chi +" "+ space1+" "+caun+" "+ str(cqtd)+" >>"+cqtx +" "+pssc+" "+pscl)
				self.postsql.saveDataApache('dummydb','postgres','secretpass', chi, space1, caun, cqtd, cqtx, pssc, pscl)
			else:
				
				#cadena = str(msg.value)
				#print(">>>>>>>>>>>MESSAGESS")
				time_struct, parse_status = p.parse(str(msg.value))
				fecha = datetime(*time_struct[:6])
				fecha = str(fecha)
				cadena = str(msg.value)
				dirhost =  cadena.split(" ")[3]
				codeLog = cadena.split(" ")[4]
				logMessage = cadena.split(" ")[5:]
				#print(fecha)
				#print(dirhost)
				es = " "
				#print(codeLog)
				#print(es.join(logMessage))
				self.postsql.saveData('dummydb','postgres','secretpass', fecha, dirhost, codeLog,str(es.join(logMessage)))


consu = ConsumerPost('localhost:9092','syslogs3','localhost','5432')
consu.sendData()
