# Fetch username and password from the request
username = frappe.form_dict.get("username")
password_input = frappe.form_dict.get("password")

# Initialize response message
response_message = ""

try:
    # Fetch the hashed password from __Auth table
    stored_password_hash = frappe.db.get_value("__Auth", {"doctype": "User", "name": username}, "password")

    if not stored_password_hash:
        response_message = "User does not exist or has no password set."
    else:
        # Validate the provided password against the stored hash
        from frappe.utils.password import check_password

        if check_password(password_input, stored_password_hash):
            response_message = "Login successful."
        else:
            response_message = "Incorrect password."

except Exception as e:
    # Log error for debugging
    frappe.msgprint(f"Error: {str(e)}")
    response_message = f"An error occurred: {str(e)}"

# Set the response message
frappe.response["message"] = response_message
