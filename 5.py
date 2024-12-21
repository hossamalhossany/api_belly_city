# Fetch username and password from the request
username = frappe.form_dict.get("username")
password_input = frappe.form_dict.get("password")

try:
    # Check if the user exists
    user_list = frappe.get_all("User", filters={"name": username}, limit_page_length=1)

    frappe.response["message"] = f"the get_all retuen data ::: line 9 {user_list} "
    if not user_list:
        frappe.response["message"] = "Login failed. User does not exist."
    else:
        # Retrieve the user document
        user = frappe.get_doc("User", user_list[0].name)

        frappe.response["message"] = f"the get_doc retuen data ::: line 16 {user}"

        hashed_input_password = frappe.utils.password.get_encrypted_password(password_input)


        # Verify the password using Frappe's password utility
        if frappe.utils.password.verify_password(password_input, user.password):
            frappe.response["message"] = "Login successful!"
        else:
            frappe.response["message"] = "Login failed. Incorrect password."
except Exception as e:
    frappe.response["message"] = f"An error occurred:line 24 :::  {str(e)}"