
import requests
import time 

out = ""

tv833 = 95
tv334 = 56
tv466 = 40
tv337 = 48


k = 0
while k < 95:
	k = k + 1
	print str(k)
	if k < tv833:
		r = requests.get("https://www.rottentomatoes.com/source-833?page=" + str(k) + "&filter=tv")
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	out = out + line + "\n"
	if k < tv334:
		r = requests.get("https://www.rottentomatoes.com/source-334?page=" + str(k) + "&filter=tv")
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	out = out + line + "\n"
	if k < tv466:
		r = requests.get("https://www.rottentomatoes.com/source-466?page=" + str(k) + "&filter=tv")
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	out = out + line + "\n"
	if k < tv337:
		r = requests.get("https://www.rottentomatoes.com/source-337?page=" + str(k) + "&filter=tv")
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	out = out + line + "\n"
oute = open("tv_out.txt","w")
oute.write(out)
oute.close()
