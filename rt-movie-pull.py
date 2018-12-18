
import requests
import time 

out = ""
mv833 = 126
mv334 = 62
mv213 = 215
mv466 = 282
mv337 = 330
mv67 = 178
mv1708 = 73

k = 0
while k < 331:
	k = k + 1
	print str(k)
	if k < mv833:
		r = requests.get("https://www.rottentomatoes.com/source-833?page=" + str(k))
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	if line in out:
   			 		time.sleep(0)
   			 	else:	
   			 		out = out + line + "\n"
	if k < mv334:
		r = requests.get("https://www.rottentomatoes.com/source-334?page=" + str(k))
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	if line in out:
   			 		time.sleep(0)
   			 	else:	
   			 		out = out + line + "\n"
	if k < mv213:
		r = requests.get("https://www.rottentomatoes.com/source-213?page=" + str(k))
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	if line in out:
   			 		time.sleep(0)
   			 	else:	
   			 		out = out + line + "\n" 
	if k < mv466:
		r = requests.get("https://www.rottentomatoes.com/source-466?page=" + str(k))
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	if line in out:
   			 		time.sleep(0)
   			 	else:	
   			 		out = out + line + "\n"
	if k < mv337:
		r = requests.get("https://www.rottentomatoes.com/source-337?page=" + str(k))
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	if line in out:
   			 		time.sleep(0)
   			 	else:	
   			 		out = out + line + "\n"			 	
	if k < mv67:
		r = requests.get("https://www.rottentomatoes.com/source-67?page=" + str(k))
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	if line in out:
   			 		time.sleep(0)
   			 	else:	
   			 		out = out + line + "\n"			 	
	if k < mv1708:
		r = requests.get("https://www.rottentomatoes.com/source-1708?page=" + str(k))
		for line in r.iter_lines():
   			 if 'class="movie-link"' in line:
   			 	if line in out:
   			 		time.sleep(0)
   			 	else:	
   			 		out = out + line + "\n"   			 	   			 	

   			 	
oute = open("mv_out.txt","w")
oute.write(out)
oute.close()
