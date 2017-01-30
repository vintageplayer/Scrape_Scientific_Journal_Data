import glob
from bs4 import BeautifulSoup
import json
import urllib.request

import signal
from contextlib import contextmanager

class TimeoutException(Exception): pass


@contextmanager
def time_limit(seconds):
	def signal_handler(signum, frame):
		raise TimeoutException
	signal.signal(signal.SIGALRM, signal_handler)
	signal.alarm(seconds)
	try:
		yield
	finally:
		signal.alarm(0)


# The prefix of updated link to get JSON object inserted in the website using AngularJS
JSON_Data_link 			= "http://ieeexplore.ieee.org/rest/document/"


def get_response(aurl):
	hdr					= {'User-Agent':'Mozilla/5.0'}
	req					= urllib.request.Request(aurl,headers=hdr)
	# response			= urllib.request.urlopen(req)

	while True:
		try: 
			# Waiting 60 seconds to recieve a responser object
			with time_limit(30):
				response			= urllib.request.urlopen(req)
			break
		except Exception:
			print("Error opening url!!")
			continue


	return response

# Getting the authors' details
def get_authors(arnumber):
	authors 	= {}

	authors_link		= JSON_Data_link + arnumber + "/authors"

	try:
		response 			= get_response(authors_link)
		content				= response.read().decode()
		authors 			= json.loads(content)
	except Exception:
		pass

	return authors

def get_journals_list():

	return glob.glob("../output/Journal Data/*")


def get_volumes_list(adir):

	return glob.glob(adir+"/Volumes/*")


def get_contents_list(adir):

	return glob.glob(adir+"/*")

def update_journal(adir):
	print(adir)
	volumes = get_volumes_list(adir)
	for volume in volumes:
		issues = get_contents_list(volume)

		for issue in issues:
			articles = get_contents_list(issue)

			for article in articles:
				with open(article+"/ArticleData.json",'r') as infile:
					article_data = json.load(infile)

				article_data["authors"]			= get_authors(article_data["arnumber"])

				print("Updating article : " + article_data["arnumber"])

				with open(article+"/ArticleData.json","w") as outfile:
					json.dump(article_data,outfile)

if __name__ == "__main__":
	journals = get_journals_list()
	for journal in journals:
		update_journal(journal)