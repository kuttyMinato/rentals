import frappe

def execute():
    drivers=frappe.db.get_all("Driver",pluck="name")
    for d in drivers:
        print(d)
        driver=frappe.get_doc("Driver",d)
        driver.set_name()
        driver.save()
    frappe.db.commit()