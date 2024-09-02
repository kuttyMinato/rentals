# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
    def before_save(self):
        pass
    def set_title(self):
        self.title=f"{self.make} {self.model}, {self.year}"
            
