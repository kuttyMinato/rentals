# your_app/your_app/www/custom_route.py
import frappe

def get_context(context):
    print("*****************&&&&&&&&&&&&&&&&&&^^^^^^^^^^^^^^^^^^^^^^Custom route called")
    context.message = "Hello, this is the response from the custom function in api.py!"
    frappe.redirect("/desk")
    return context

