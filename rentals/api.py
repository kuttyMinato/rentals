import frappe

@frappe.whitelist(allow_guest=True)
def get_emoji():
    return "emoji"

@frappe.whitelist(allow_guest=True)
def custom():
    print("This was my custom Routing FUnction.........!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return "Hello, this is a custom route!"