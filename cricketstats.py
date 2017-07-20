import requests
from bs4 import BeautifulSoup

r=requests.get('http://www.cricbuzz.com/profiles/265/ms-dhoni')
soup=BeautifulSoup(r.content,"html.parser")
print ('First Batsman:-')
print (' ')
h1=soup.find('h1', attrs={'class':'cb-font-40'})
Name=h1.text
h3=soup.find('h3', attrs={'class':'cb-font-18'})
RemoveString=h3.text
country=RemoveString
Name=Name.replace(RemoveString,'')
print (Name)
print (country)


div=soup.find('div', attrs={'class':'cb-col cb-col-40 text-bold'})
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
battingstyle=div.text
print ("Battin style:%s"%battingstyle)

print ("Test career:")
print ("                   ")
#Test Matches
table = soup.find('table', attrs={'class':'table cb-col-100 cb-plyr-thead'})
table_body = table.find('tbody')
td=table_body.find('td',{'class':'cb-plyr-tbody text-right'})
test_matches=td.text
print ("Test Matches played:%s"%test_matches)

td=td.findNext('td')
text_inns=td.text
print ("Test Innings played:%s"%text_inns)

td=td.findNext('td')
td=td.findNext('td')
TestRuns=td.text
print ("Test runs: %s" %TestRuns)

td=td.findNext('td')
THS=td.text
print ("Test Highest Score: %s" %THS)

td=td.findNext('td')
TAvg=td.text
print ("Test Average: %s" %TAvg)

td=td.findNext('td')
td=td.findNext('td')
tSR=td.text
print ("Test Strike Rate: %s" %tSR)

td=td.findNext('td')
THundreds=td.text
print ("Test Hundreds: %s" %THundreds)

td=td.findNext('td')
TDHundreds=td.text
print ("Test Double Hundreds: %s" %TDHundreds)

td=td.findNext('td')
TFifties=td.text
print ("Test Fifties: %s" %TFifties)

#ODI
print ("                   ")
print ("ODI career:")
print ("                   ")

tr=table_body.find('tr')
tr=tr.findNext('tr')
td=tr.find('td',{'class':'cb-plyr-tbody text-right'})
odi_matches=td.text
print ("ODI Matches played:%s"%odi_matches)

td=td.findNext('td')
odi_inns=td.text
print ("ODI Innings played:%s"%odi_inns)

td=td.findNext('td')
td=td.findNext('td')
odiRuns=td.text
print ("ODI runs: %s" %odiRuns)

td=td.findNext('td')
OHS=td.text
print ("ODI Highest Score: %s" %OHS)

td=td.findNext('td')
OAvg=td.text
print ("ODI Average: %s" %OAvg)

td=td.findNext('td')
td=td.findNext('td')
OSR=td.text
print ("ODI Strike Rate: %s" %OSR)

td=td.findNext('td')
OHundreds=td.text
print ("ODI Hundreds: %s" %OHundreds)

td=td.findNext('td')
ODHundreds=td.text
print ("ODI Double Hundreds: %s" %ODHundreds)

td=td.findNext('td')
OFifties=td.text
print ("ODI Fifties: %s" %OFifties)
#T20
print ("                   ")
print ("T20 career:")
print ("                   ")

tr=table_body.find('tr')
tr=tr.findNext('tr')
tr=tr.findNext('tr')
td=tr.find('td',{'class':'cb-plyr-tbody text-right'})
t20_matches=td.text
print ("T20 Matches played:%s"%t20_matches)

td=td.findNext('td')
t20_inns=td.text
print ("T20 Innings played:%s"%t20_inns)

td=td.findNext('td')
td=td.findNext('td')
t20Runs=td.text
print ("T20 runs: %s" %t20Runs)

td=td.findNext('td')
t20HS=td.text
print ("T20 Highest Score: %s" %t20HS)

td=td.findNext('td')
t20Avg=td.text
print ("T20 Average: %s" %t20Avg)

td=td.findNext('td')
td=td.findNext('td')
t20SR=td.text
print ("T20 Strike Rate: %s" %t20SR)

td=td.findNext('td')
t20Hundreds=td.text
print ("T20 Hundreds: %s" %t20Hundreds)

td=td.findNext('td')
t20DHundreds=td.text
print ("T20 Double Hundreds: %s" %t20DHundreds)

td=td.findNext('td')
t20Fifties=td.text
print ("T20 Fifties: %s" %t20Fifties)
print (' ')

print ('---------------------------------------------------')

#second part
print ('Second Batsman:-')
print (' ')
r=requests.get('http://www.cricbuzz.com/profiles/1413/virat-kohli')
soup=BeautifulSoup(r.content,"html.parser")

h1=soup.find('h1', attrs={'class':'cb-font-40'})
Name2=h1.text
h3=soup.find('h3', attrs={'class':'cb-font-18'})
RemoveString=h3.text
country=RemoveString
Name2=Name2.replace(RemoveString,'')
print (Name2)
print (country)



div=soup.find('div', attrs={'class':'cb-col cb-col-40 text-bold'})
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
div=div.findNext('div')
battingstyle=div.text
print ("Battin style:%s"%battingstyle)

print ("Test career:")
print ("                   ")
#Test Matches
table = soup.find('table', attrs={'class':'table cb-col-100 cb-plyr-thead'})
table_body = table.find('tbody')
td=table_body.find('td',{'class':'cb-plyr-tbody text-right'})
test_matches2=td.text
print ("Test Matches played:%s"%test_matches2)

td=td.findNext('td')
text_inns2=td.text
print ("Test Innings played:%s"%text_inns2)

td=td.findNext('td')
td=td.findNext('td')
TestRuns2=td.text
print ("Test runs: %s" %TestRuns2)

td=td.findNext('td')
THS2=td.text
print ("Test Highest Score: %s" %THS2)

td=td.findNext('td')
TAvg2=td.text
print ("Test Average: %s" %TAvg2)

td=td.findNext('td')
td=td.findNext('td')
tSR2=td.text
print ("Test Strike Rate: %s" %tSR2)

td=td.findNext('td')
THundreds2=td.text
print ("Test Hundreds: %s" %THundreds2)

td=td.findNext('td')
TDHundreds2=td.text
print ("Test Double Hundreds: %s" %TDHundreds2)

td=td.findNext('td')
TFifties2=td.text
print ("Test Fifties: %s" %TFifties2)

#ODI
print ("                   ")
print ("ODI career:")
print ("                   ")

tr=table_body.find('tr')
tr=tr.findNext('tr')
td=tr.find('td',{'class':'cb-plyr-tbody text-right'})
odi_matches2=td.text
print ("ODI Matches played:%s"%odi_matches2)

td=td.findNext('td')
odi_inns2=td.text
print ("ODI Innings played:%s"%odi_inns2)

td=td.findNext('td')
td=td.findNext('td')
odiRuns2=td.text
print ("ODI runs: %s" %odiRuns2)

td=td.findNext('td')
OHS2=td.text
print ("ODI Highest Score: %s" %OHS2)

td=td.findNext('td')
OAvg2=td.text
print ("ODI Average: %s" %OAvg2)

td=td.findNext('td')
td=td.findNext('td')
OSR2=td.text
print ("ODI Strike Rate: %s" %OSR2)

td=td.findNext('td')
OHundreds2=td.text
print ("ODI Hundreds: %s" %OHundreds2)

td=td.findNext('td')
ODHundreds2=td.text
print ("ODI Double Hundreds: %s" %ODHundreds2)

td=td.findNext('td')
OFifties2=td.text
print ("ODI Fifties: %s" %OFifties2)

#T20
print ("                   ")
print ("T20 career:")
print ("                   ")

tr=table_body.find('tr')
tr=tr.findNext('tr')
tr=tr.findNext('tr')
td=tr.find('td',{'class':'cb-plyr-tbody text-right'})
t20_matches2=td.text
print ("T20 Matches played:%s"%t20_matches2)

td=td.findNext('td')
t20_inns2=td.text
print ("T20 Innings played:%s"%t20_inns2)

td=td.findNext('td')
td=td.findNext('td')
t20Runs2=td.text
print ("T20 runs: %s" %t20Runs2)

td=td.findNext('td')
t20HS2=td.text
print ("T20 Highest Score: %s" %t20HS2)

td=td.findNext('td')
t20Avg2=td.text
print ("T20 Average: %s" %t20Avg2)

td=td.findNext('td')
td=td.findNext('td')
t20SR2=td.text
print ("T20 Strike Rate: %s" %t20SR2)

td=td.findNext('td')
t20Hundreds2=td.text
print ("T20 Hundreds: %s" %t20Hundreds2)

td=td.findNext('td')
t20DHundreds2=td.text
print ("T20 Double Hundreds: %s" %t20DHundreds2)

td=td.findNext('td')
t20Fifties2=td.text
print ("T20 Fifties: %s" %t20Fifties2)


#ODI Analysis
print (' ')
print ('ODI Analysis:')
print (' ')
p1=0
p2=0
odi_matches=int(odi_matches)
odi_matches2=int(odi_matches2)
if(odi_matches>odi_matches2):
    diff=odi_matches-odi_matches2
    print ("->%s has played %d matches, %d more matches than %s" %(Name,odi_matches,diff,Name2))
    p1=p1+1
else:
    diff=odi_matches2-odi_matches
    print ("->%s has played %d matches, %d more matches than %s" %(Name2,odi_matches2,diff,Name))
    p2=P2+1
    
odiRuns=int(odiRuns)
odiRuns2=int(odiRuns2)
if(odiRuns>odiRuns2):
    diff=odiRuns-odiRuns2
    print ("->%s has scored %d runs, %d more runs than %s" %(Name,odiRuns,diff,Name2))
    p1=p1+2
else:
    diff=odiRuns2-odiRuns
    print ("->%s has scored %d runs, %d more runs than %s" %(Name2,odiRuns2,diff,Name))
    p2=P2+2
    

OAvg=float(OAvg)
OAvg2=float(OAvg2)
if(OAvg>OAvg2):
    print ("->%s has an ODI Average of %f of overall career, which is more than %f of %s" %(Name,OAvg,OAvg2,Name2))
    p1=p1+2
else:
    print ("->%s has an ODI Average of %f of overall career, which is more than %f of %s" %(Name2,OAvg2,OAvg,Name))
    p2=p2+2
    

OSR=float(OSR)
OSR2=float(OSR2)
if(OSR>OSR2):
    print ("->%s has strike rate of %f better than %s " %(Name,OSR,Name2))
    p1=p1+1
else:
    print ("->%s has strike rate of %f better than %s " %(Name2,OSR2,Name))
    p2=p2+1


OHundreds=int(OHundreds)
OHundreds2=int(OHundreds2)
if(OHundreds>OHundreds2):
    diff=OHundreds-OHundreds2
    print ("->%s has scored %d Hundreds, %d more than %s who has scored %d " %(Name,OHundreds,diff,Name2,OHundreds2))
    p1=p1+2
else:
    diff=OHundreds2-OHundreds
    print ("->%s has scored %d Hundreds, %d more than %s who has scored %d " %(Name2,OHundreds2,diff,Name,OHundreds))
    p2=p2+2
    

OFifties=int(OFifties)
OFifties2=int(OFifties2)
if(OFifties>OFifties2):
    diff=OFifties-OFifties2
    print ("->%s has scored %d Fifties, %d more than %s who has scored %d " %(Name,OFifties,diff,Name2,OFifties2))
    p1=p1+1
else:
    diff=OFifties2-OFifties
    print ("->%s has scored %d Fifties, %d more than %s who has scored %d " %(Name2,OFifties2,diff,Name,OFifties))
    p2=P2+1
print (' ')   
if(p1>p2):
    print ("-->%s is better ODI batsman than %s"%(Name,Name2))
else:
    print ("-->%s is better ODI batsman than %s"%(Name2,Name))
    



#Test Analysis
print (' ')
print ('Test Analysis:')
print (' ')
p1=0
p2=0
test_matches=int(test_matches)
test_matches2=int(test_matches2)
if(test_matches>test_matches2):
    diff=test_matches-test_matches2
    print ("->%s has played %d matches, %d more matches than %s" %(Name,test_matches,diff,Name2))
    p1=p1+1
else:
    diff=test_matches2-test_matches
    print ("->%s has played %d matches, %d more matches than %s" %(Name2,test_matches2,diff,Name))
    p2=P2+1
    
TestRuns=int(TestRuns)
TestRuns2=int(TestRuns2)
if(TestRuns>TestRuns2):
    diff=TestRuns-TestRuns2
    print ("->%s has scored %d runs, %d more runs than %s" %(Name,TestRuns,diff,Name2))
    p1=p1+2
else:
    diff=TestRuns2-TestRuns
    print ("->%s has scored %d runs, %d more runs than %s" %(Name2,TestRuns2,diff,Name))
    p2=P2+2
    

TAvg=float(TAvg)
TAvg2=float(TAvg2)
if(TAvg>TAvg2):
    print ("->%s has an Test Average of %f of overall career, which is more than %f of %s" %(Name,TAvg,TAvg2,Name2))
    p1=p1+2
else:
    print ("->%s has an Test Average of %f of overall career, which is more than %f of %s" %(Name2,TAvg2,TAvg,Name))
    p2=p2+2
    

tSR=float(tSR)
tSR2=float(tSR2)
if(tSR>tSR2):
    print ("->%s has strike rate of %f better than %s " %(Name,tSR,Name2))
    p1=p1+1
else:
    print ("->%s has strike rate of %f better than %s " %(Name2,tSR2,Name))
    p2=p2+1


THundreds=int(THundreds)
THundreds2=int(THundreds2)
if(THundreds>THundreds2):
    diff=THundreds-THundreds2
    print ("->%s has scored %d Hundreds, %d more than %s who has scored %d " %(Name,THundreds,diff,Name2,THundreds2))
    p1=p1+2
else:
    diff=THundreds2-THundreds
    print ("->%s has scored %d Hundreds, %d more than %s who has scored %d " %(Name2,THundreds2,diff,Name,THundreds))
    p2=p2+2
    

TFifties=int(TFifties)
TFifties2=int(TFifties2)
if(TFifties>TFifties2):
    diff=TFifties-TFifties2
    print ("->%s has scored %d Fifties, %d more than %s who has scored %d " %(Name,TFifties,diff,Name2,TFifties2))
    p1=p1+1
else:
    diff=TFifties2-TFifties
    print ("->%s has scored %d Fifties, %d more than %s who has scored %d " %(Name2,TFifties2,diff,Name,TFifties))
    p2=P2+1
print (' ')   
if(p1>p2):
    print ("-->%s is better Test batsman than %s"%(Name,Name2))
else:
    print ("-->%s is better Test batsman than %s"%(Name2,Name))


#t20 Analysis
print (' ')
print ('t20 Analysis:')
print (' ')
p1=0
p2=0
t20_matches=int(t20_matches)
t20_matches2=int(t20_matches2)
if(t20_matches>t20_matches2):
    diff=t20_matches-t20_matches2
    print ("->%s has played %d matches, %d more matches than %s" %(Name,t20_matches,diff,Name2))
    p1=p1+1
else:
    diff=t20_matches2-t20_matches
    print ("->%s has played %d matches, %d more matches than %s" %(Name2,t20_matches2,diff,Name))
    p2=P2+1
    
t20Runs=int(t20Runs)
t20Runs2=int(t20Runs2)
if(t20Runs>t20Runs2):
    diff=t20Runs-t20Runs2
    print ("->%s has scored %d runs, %d more runs than %s" %(Name,t20Runs,diff,Name2))
    p1=p1+2
else:
    diff=t20Runs2-t20Runs
    print ("->%s has scored %d runs, %d more runs than %s" %(Name2,t20Runs2,diff,Name))
    p2=p2+2
    

t20Avg=float(t20Avg)
t20Avg2=float(t20Avg2)
if(t20Avg>t20Avg2):
    print ("->%s has an t20 Average of %f of overall career, which is more than %f of %s" %(Name,t20Avg,t20Avg2,Name2))
    p1=p1+2
else:
    print ("->%s has an t20 Average of %f of overall career, which is more than %f of %s" %(Name2,t20Avg2,t20Avg,Name))
    p2=p2+2
    

t20SR=float(t20SR)
t20SR2=float(t20SR2)
if(t20SR>t20SR2):
    print ("->%s has strike rate of %f better than %s " %(Name,t20SR,Name2))
    p1=p1+1
else:
    print ("->%s has strike rate of %f better than %s " %(Name2,t20SR2,Name))
    p2=p2+1


t20Hundreds=int(t20Hundreds)
t20Hundreds2=int(t20Hundreds2)
if(t20Hundreds>t20Hundreds2):
    diff=t20Hundreds-t20Hundreds2
    print ("->%s has scored %d Hundreds, %d more than %s who has scored %d " %(Name,t20Hundreds,diff,Name2,t20Hundreds2))
    p1=p1+2
else:
    diff=t20Hundreds2-t20Hundreds
    print ("->%s has scored %d Hundreds, %d more than %s who has scored %d " %(Name2,t20Hundreds2,diff,Name,t20Hundreds))
    p2=p2+2
    

t20Fifties=int(t20Fifties)
t20Fifties2=int(t20Fifties2)
if(t20Fifties>t20Fifties2):
    diff=t20Fifties-t20Fifties2
    print ("->%s has scored %d Fifties, %d more than %s who has scored %d " %(Name,t20Fifties,diff,Name2,t20Fifties2))
    p1=p1+1
else:
    diff=t20Fifties2-t20Fifties
    print ("->%s has scored %d Fifties, %d more than %s who has scored %d " %(Name2,t20Fifties2,diff,Name,t20Fifties))
    p2=p2+1
print (' '   )
if(p1>p2):
    print ("-->%s is better t20 batsman than %s"%(Name,Name2))
else:
    print ("-->%s is better t20 batsman than %s"%(Name2,Name))