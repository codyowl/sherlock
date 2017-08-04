import urllib2
from BeautifulSoup import BeautifulSoup
from selenium import webdriver

class Sherlock(object):
	
	def predict(self, url):
		self.url = url
		self.link_getter = self.index_link_and_button_getter(self.url)
		return self.link_getter

	@staticmethod	
	def index_link_and_button_getter(url):
		html_file = urllib2.urlopen(url).read()
		soup = BeautifulSoup(html_file)
		all_links = soup.findAll("a")
		if all_links:
			link_name = [link.string for link in all_links]
		return all_links
	

	