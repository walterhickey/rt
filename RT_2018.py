import requests


with open('RT2018_input.txt', 'r') as f:
    myNames = [line.strip() for line in f]

output = ""
count = 0
while count < 260:
	type = "tv"
	count = count + 1
	url = str(myNames.pop(0))
	try:
		r = requests.get(url)
	except:
		continue 
	derp = r.text
	if '<div class="meta-label subtle">Network:' in derp:
		network = derp[derp.find('<div class="meta-label subtle">Network: </div>'):]
		network = network[network.find("meta-value")+13:]
		network = network[:network.find('</div>')].strip()
	else:
		network = ""
		
	if '<div class="meta-label subtle">Premiere Date:' in derp:
		date = derp[derp.find('<div class="meta-label subtle">Premiere Date: </div>'):]
		date = date[date.find("meta-value")+13:]
		date = date[:date.find('</div>')].strip()
	else:
		date = ""	
	
	derp = derp[derp.find('<a href="#contentReviews"'):derp.find('"rating-root"')]
	
	
	if 'meter-value superPageFontColor"><span>' in derp:
		derp = derp[derp.find('meter-value superPageFontColor"><span>')+38:]
		crit_tom = derp[:derp.find("</span>")]
	else:
		crit_tom = ""
	
	if '"subtle superPageFontColor">Season Reviews:' in derp:	
		derp = derp[derp.find('"subtle superPageFontColor">Season Reviews: </span><span>')+57:]
		crit_cnt = derp[:derp.find("</span>")]
	else: 
		crit_cnt = ""
	
	if 'uperPageFontColor" style="vertical-align:top"' in derp:	
		derp = derp[derp.find('uperPageFontColor" style="vertical-align:top">')+46:]
		audi_tom = derp[:derp.find("</span>")]
	else:
		audi_tom = ""
	
	if 'User Ratings:</span>' in derp:	
		derp = derp[derp.find('User Ratings:</span>')+20:]
		audi_cnt = derp[:derp.find("</div>")].strip()
	else:
		audi_cnt = ""
	
	print url
	output = output + network + "|" + type + "|" + url  + "|" + date  + "|" + crit_tom  + "%|" + crit_cnt + "|" + audi_tom + "|" + audi_cnt  + "|\n"

tvout = open("RTTV2018Out.txt","w")
tvout.write(output)
tvout.close()

output = ""
		


while count < 1901:
	type = "mv"
	count = count + 1
	url = str(myNames.pop(0))
	try:
		r = requests.get(url)
	except:
		continue 
		
	derp = r.text

	
	derp = derp[derp.find('<a href="#contentReviews"'):derp.find('"rating-root"')]
	
	
	if 'meter-value superPageFontColor"><span>' in derp:
		derp = derp[derp.find('meter-value superPageFontColor"><span>')+38:]
		crit_tom = derp[:derp.find("</span>")]
	else:
		crit_tom = ""
	
	if '<span class="subtle superPageFontColor">Reviews Counted: </span><span>' in derp:	
		derp = derp[derp.find('<span class="subtle superPageFontColor">Reviews Counted: </span><span>')+70:]
		crit_cnt = derp[:derp.find("</span>")]
	else: 
		crit_cnt = ""
	
	if 'uperPageFontColor" style="vertical-align:top">' in derp:	
		derp = derp[derp.find('uperPageFontColor" style="vertical-align:top">')+46:]
		audi_tom = derp[:derp.find("</span>")]
	else:
		audi_tom = ""
	
	if 'User Ratings:</span>' in derp:	
		derp = derp[derp.find('User Ratings:</span>')+20:]
		audi_cnt = derp[:derp.find("</div>")].strip()
	else:
		audi_cnt = ""
	print url	
	output = output + "|" + type + "|" + url  + "|" + crit_tom  + "%|" + crit_cnt + "|" + audi_tom + "|" + audi_cnt  + "|\n"
		
		

tvout = open("RTMV2018Out.txt","w")
tvout.write(output)
tvout.close()



