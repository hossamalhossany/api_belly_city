import frappe
from frappe.utils import password

# Fetch username and password from the request
username = frappe.form_dict.get("username")
password_input = frappe.form_dict.get("password")

try:
    # Check if the user exists
    user_list = frappe.get_all("User ", filters={"name": username}, limit_page_length=1)

    if not user_list:
        frappe.response["message"] = "Login failed. User does not exist."
    else:
        # Retrieve the user document
        user = frappe.get_doc("User ", user_list[0].name)

        # Verify the password using Frappe's password utility
        if password.verify_password(password_input, user.password):
            frappe.response["message"] = "Login successful!"
        else:
            frappe.response["message"] = "Login failed. Incorrect password."
except Exception as e:
    frappe.response["message"] = f"An error occurred: {str(e)}"