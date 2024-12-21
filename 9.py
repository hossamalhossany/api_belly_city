# Fetch username and password from the request
username = frappe.form_dict.get("username")
password_input = frappe.form_dict.get("password")


user_list = frappe.get_all("User", filters={"name": username}, limit_page_length=1)

frappe.response["message"] = f"the get_all returned data ::: line 8 {user_list} "


# Retrieve the user document
user = frappe.get_doc("User", user_list[0].name)

frappe.response["message"] = f"the get_doc returned data ::: line 16 {user.password}"

# # Verify the password using Frappe's password utility
# if frappe.utils.password.verify_password(password_input, user.password):
#     frappe.response["message"] = "Login successful!"
# else:
#     frappe.response["message"] = "Login failed. Incorrect password."
#
