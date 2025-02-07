from selenium import webdriver

class SeleniumClient:
	@staticmethod
	def get_driver(self):
		return webdriver.Chrome()