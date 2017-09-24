class Match(object):
	"""Class that represents a Match in TV"""

	def __init__(self, title, description, start_time, end_time, status, channel, id_kava):
		super(Match, self).__init__()
		self.title = title
		self.description = description
		#datetime.datetime to store the times
		self.start_time = start_time
		self.end_time = end_time
		self.live = self.validateStatus(status)
		self.channel = channel
		self.id_kava = id_kava

	#To store a boolean if the match is Live
	def validateStatus(self, statusText):
			return statusText == 'live'

	def __str__(self):
		return self.title+'\n'+self.description+'\n'+str(self.start_time)+'\n'+str(self.end_time)+'\n'+str(self.live)+'\n'+str(self.channel)+'\n'+str(self.id_kava)


		