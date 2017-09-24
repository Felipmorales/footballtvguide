from classes.match import Match
import urllib, json, datetime

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
		description = programmes[i]['description']
		start_time = datetime.datetime.fromtimestamp(programmes[i]['start_unix'])
		end_time = datetime.datetime.fromtimestamp(programmes[i]['stop_unix'])
		status = programmes[i]['status']
		channel = programmes[i]['channel']['name']
		id_kava = programmes[i]['id']
		match = Match(title,description,start_time,end_time,status,channel,id_kava)

		matches.append(match)

	if (liveornot):
		filtered_matches = []
		for i in range(len(matches)):
			if matches[i].live:
				filtered_matches.append(matches[i])

		matches = filtered_matches

	return matches

print 'STARTING!'

result = grabMatchesDay(datetime.datetime.now(),True)

for i in range(len(result)):
	print result[i].__str__() + '\n'


