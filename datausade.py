#!usr/bin/python
#
#			***JioFi_Manager***
#	Written By : prajyot gurav (prajyotgurav@gmail.com)
#
#

from urllib.request import Request
from urllib.request import urlopen
from xml.etree import ElementTree as etree
from xml.etree.ElementTree import parse
import time

def getbat():
	url = "http://jiofi.local.html/st_dev.w.xml"
	request = Request(url)
	u = urlopen(request)
	xml = u.read()
	batt_per = etree.XML(xml).findtext("batt_per")
	batt_status = int(etree.XML(xml).findtext("batt_st"))>>8
	if(batt_status < 4):
		status = "Discharging"	
	elif(batt_status == 4):
		status = "Charging"
	elif(batt_status == 5):
		status = "fully_charged"
	batt_val = batt_per + "("+status+")"
	print(batt_val)

def speed():
	url = "http://jiofi.local.html/st_per.w.xml"
	request = Request(url)
	u = urlopen(request)
	xml = u.read()
	maxuspeed = etree.XML(xml).findtext("max_tx")
	uspeed = etree.XML(xml).findtext("curr_tx")
	maxdspeed = etree.XML(xml).findtext("max_rx")
	dspeed = etree.XML(xml).findtext("curr_rx")
	print("Data Rate\nDownload:\nMax Download Rate \t:"+maxdspeed + "\nCurrent Download Rate\t:" + dspeed)
	print("Upload:\nMax Upload Rate\t\t:"+maxuspeed+"\nCurrent Upload Rate\t:"+uspeed)

def datausage():
	url = "http://jiofi.local.html/st_wan.w.xml"
	request = Request(url)
	u = urlopen(request)
	xml = u.read()
	ul = etree.XML(xml).findtext("t_tx")
	dl = etree.XML(xml).findtext("t_rx")
	print("Data Usage :\nDownload \t:"+dl+"\nUpload\t\t:"+ul)

def users():
	url = "http://jiofi.local.html/st_lan.w.xml"
	req = Request(url)
	resp = urlopen(req)
	xml = parse(resp)
	i = 0
	for userlist in xml.findall("user_list"):
		for user in userlist.findall("user"):
			i=i+1
			print("User #"+str(i))
			print("Name\t:"+user.findtext("name"))
			print("IP\t:"+user.findtext("ip"))

ch = 0
while ch!= 5:
	ch = int(input("\n1.Battery Info\n2.Data Usage\n3.Current Speed\n4.Connected Users\n5.Exit\nEnter Choice :"))
	if(ch == 1):
		getbat()
	elif(ch == 2):
		datausage()
	elif(ch == 3):
		speed()
	elif(ch == 4):
		users()
	elif(ch == 5):
		exit()
	else:
		print("Enter Correct Option")


#system = "http;//jiofi.local.html/st_per.w.xml"
#device = "http;//jiofi.local.html/st_dev.w.xml"
#lan = "http;//jiofi.local.html/st_lan.w.xml"
#wan = "http;//jiofi.local.html/st_wan.w.xml"

