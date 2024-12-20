# Fetch username and password from the request
username = frappe.form_dict.get("username")
password = frappe.form_dict.get("password")

try:
    # Check if the user exists
    user = frappe.get_doc("User", username)

    if not user:
        frappe.response["message"] = "Login failed. User does not exist."
    else:
        # Verify the password using Frappe's password utility
        if user.useFrappeAuth(password):
            frappe.response["message"] = "Login successful!"
        else:
            frappe.response["message"] = "Login failed. Incorrect password."
except Exception as e:
    # frappe.response["message"] = str(e)
    frappe.response["message"] = str(e)

