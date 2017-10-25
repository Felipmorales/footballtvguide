from classes.match import Match
import urllib, json, datetime, re

#Function that gets the JSON and parses it
def grabMatchesDay(date, liveornot):
	matches = []

	#Replace date in the kava.ee url
	simple_date = str(date.day)+'-'+str(date.month)+'-'+str(date.year)
	url = "https://www.kava.ee/programme/listing/football/%s?filter=sports" % (simple_date)

	response = urllib.urlopen(url)
	data = json.loads(response.read())

	programmes = data['schedule']['programme']

	for i in range(len(programmes)):
		title = programmes[i]['title']

		#Make the description the title if the title doesn't show the teams.
		pattern = ['-',' v ',' - ']
		containsit = False
		for p in pattern:
			x = re.search(p,title)
			if x != None:
				containsit = True
				break
			else:
				containsit = False

		if containsit == False and programmes[i]['description'] != '':
			title = programmes[i]['description']

		start_time = datetime.datetime.fromtimestamp(programmes[i]['start_unix'])
		end_time = datetime.datetime.fromtimestamp(programmes[i]['stop_unix'])
		status = programmes[i]['status']
		channel = programmes[i]['channel']['name']
		id_kava = programmes[i]['id']
		match = Match(title,start_time,end_time,status,channel,id_kava)

		matches.append(match)

	if (liveornot):
		filtered_matches = []
		for i in range(len(matches)):
			if matches[i].live:
				filtered_matches.append(matches[i])

		matches = filtered_matches

	return matches

#To get the matches for the week
def thisWeekMatches(liveornot):
	weekMatches = []

	today = datetime.datetime.now()

	for i in range(8):
		daymatches = grabMatchesDay(today + datetime.timedelta(days=i),liveornot)
		for j in range(len(daymatches)):
			weekMatches.append(daymatches[j])

	return weekMatches

#This is to filter only for the international matches
def onlyIntFootball(matchlist):
	intMatches = []

	intChannels = ['Setanta Eurasia', 'Eurosport 2 (Bundesliga)', 'Viasat Sport Baltic', 'Eurosport 1', 'Eurosport 2']

	for i in range(len(matchlist)):
		channel = matchlist[i].channel
		if channel in intChannels:
			intMatches.append(matchlist[i])

	return intMatches

result = onlyIntFootball(thisWeekMatches(True))

for i in range(len(result)):
	print result[i].__str__() + '\n'
