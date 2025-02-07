from selenium.webdriver.common.by import By
from selenium_client import SeleniumClient

class Abstractsyntaxtree:
	def __init__(self, component_type, url):
		self.component_type = component_type
		self.driver = SeleniumClient.get_driver()
		self.url = url

	# for extracting forms of a web page
	def extract_forms_for_a_webpage(self):
		self.driver.get(self.url)

		forms = self.driver.find_elements(By.TAG_NAME, "form")
    	self.all_forms = []

    	for form in forms:
        	inputs = form.find_elements(By.TAG_NAME, "input")
        	fields = [{"name": i.get_attribute("name"), "type": i.get_attribute("type")} for i in inputs]
        	self.all_forms.append({"url": url, "fields": fields})

    	return self.all_forms

    # for closing the driver 
    def close_driver(self):
    	return self.driver.close()	