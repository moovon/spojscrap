'''
JKM
Author :                 Sunny Mazumder aka moovon
Libraries required :     BeautifulSoup (pip install beautifulsoup4) ; requests (pip install requests)
Link :                   www.github.com/moovon
Details :                input: username only
						 output: scraps the spoj's website to get the fullname of the user, user's rank, # of problems solved and # of solution submitted.
'''


import requests,bs4

#header
print("\n")
print("|------------------------------------------|")
print("|---------------SPOJSCRAP V4.0-------------|")
print("|---AUTHOR SUNNY MAZUMDER--AKA--MOOVON-----|")
print("|------------------------------------------|")
print("\n")
#header


username=input("   Enter the Spoj's Username  : ")                   #input-username
r=requests.get("http://www.spoj.com/users/"+username+"/") 			


print("\n")                                                          #proper indentation



data=r.text															 #data stores the entire html of the web page scraped.
soup=bs4.BeautifulSoup(data,"html.parser")    #"html.parser or lxml or html5lib or xml or xml-lxml"




link=soup.find_all('dl',{'class':'dl-horizontal profile-info-data profile-info-data-stats'})        #tagetting the location where # of problems solved is located
problemssolved="invalid username"																			




userdetails=soup.find('div', {'class':'col-md-3'})                   #scrapping the full name,if provided
try:
	for name in userdetails.find_all('h3'):
		print("   Full Name : "+name.text+"\n")						 #printing the full name
except Exception:
	pass




flag=-1																 #scrapping world rank and total points 
try:
	for rankandpoints in userdetails.find_all('p'):					 #flag is used to scrap only world rank and total points, not other details
		flag+=1
		if flag==2:
			print("  "+rankandpoints.text+"\n")
except Exception:
	pass




for item in link:													#scrapping # of problems solved and # of solutions submittedself.
    problemssolved=item.text
for item in problemssolved:
	if problemssolved=="invalid username":										#checking validity of the username , if invalid, breaks the loop.					
		print(" ",end='  ')
		print(username+" is a "+problemssolved)
		break
	if item=='\n':													#prints the # of problems solved.
		print(" ",end=' ')
	elif item=='d':
		print("d by  "+username+": ",end='')
	elif item=='S':													#prints of # of solutions submitted.
		print('\n')
		print(" ",end='  ')
		print(item,end='')
	else:															
		print(item,end='')											#avoids printing a new line




#footer
print("\n\n")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~THANK YOU FOR USING SPOJSCRAP V4.0~~~|")
print("|~~~~~~~~~~www.github.com/moovon~~~~~~~~~~~|")
print("|~~~~~~~~~~~moovonjkm@gmail.com~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~jkm~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("Press any key to quit")
quit=input()

#footer