#!/usr/bin/python

import os,sys
import re


path = sys.argv[1]
sourcesList = []

def fileReader(file):
	f = open(file,"rb").read()
	return f

def Lister(path):
	for fpath, dirs,files in os.walk(path):
	  	for file in files:
        		if ".smali" in file:
            			sourcesList.append(os.path.join(fpath, file))

Lister(path)

print "[+] Sources list successfully generated !"

class Extractor:
	def __init__(self,file):
		self.file = file

	def emailEX(self):
		emails = open(sys.argv[1]+"/EX_EMAILS.txt","a")
		data = fileReader(self.file)
		ex_emails= list(set(re.findall(r'[\w\.-]+@[\w\.-]+', data)))

		for email in ex_emails:
                        if len(email) < 2:
                                pass
                        else:
                                emails.write(email.strip()+"\n")

	def urlsEX(self):
		urls = open(sys.argv[1]+"/EX_URLS.txt","a")
		data = fileReader(self.file)
                ex_urls = list(set(re.findall(r'(?:https?|ftp):\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+', data)))

		for url in ex_urls:
			if len(url) < 2:
				pass
			else:
				urls.write(url.strip()+"\n")

	def ipsEX(self):
		ips = open(sys.argv[1]+"/EX_IPS.txt","a")
		data = fileReader(self.file)
                ex_ips = list(set(re.findall(r'[0-9]+(?:\.[0-9]+){3}', data)))

		for ip in ex_ips:
			ips.write(ip.strip()+"\n")

	def interes_files(self):
		words = ['base_url',"ftp_","db_","password","pass","user_pass","user_name","username","smtp_","passwd","mysql://","ftp://"]
		data = fileReader(self.file)
		for word in words:
			if word.upper() in data or word.lower() in data:
				print "[!] {} has {}".format(self.file,word)
			elif "UserName" or "Username" in data:
				print "[!] {} has a username ".format(self.file)
			elif "PassWord" or "Password" in data:
				print "[!] {} has a password ".format(self.file)


if __name__ == '__main__':
	for sl in sourcesList:
		EX = Extractor(sl)
		EX.urlsEX()
		EX.emailEX()
		EX.ipsEX()
