# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class RideBooking(Document):
    def validate(self):
        if not self.rate:
            frappe.throw("Please Provide a rate")
            self.rate=frappe.db.get_single_value("Rentals Settings" ,"standard_rate")
        else:
            total_distance=0 
            for i in self.item:
                total_distance += i.distance
            self.total_amount= total_distance * self.rate   
