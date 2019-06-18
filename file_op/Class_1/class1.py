class Log:
	def __init__(self,name,tm,duration):
		self.name = name
		self.time  = tm
		self.dura  = duration
		
	def __str__(self):
		return self.name + " "+ str(self.time) + " " + str(self.dura)
		
test = Log("WiFi", 100,"day")
print (test)

