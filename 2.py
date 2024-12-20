# Fetch username and password from the request
username = frappe.form_dict.get("username")


try:
    # Check if the user exists
    user = frappe.get_all("User", filters={"name": username}, limit_page_length=1)

    if not user:
        frappe.response["message"] = "Login failed. User does not exist."
    else:
        frappe.response["message"] = "hi hossam you enter username:: ",user
except Exception as e:
    # frappe.response["message"] = str(e)
    frappe.response["message"] = str(e)