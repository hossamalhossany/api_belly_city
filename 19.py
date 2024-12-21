# Fetch username and password from the request
username = frappe.form_dict.get("username")
password_input = frappe.form_dict.get("password")

# Initialize response message
response_message = ""

try:
    # Fetch the User document using frappe.get_doc
    user_doc = frappe.get_doc("User", username)

    # Check if the user exists and has a password set
    if not user_doc or not user_doc.password:
        response_message = "User does not exist or has no password set."
    else:
        # Access the password hash from the user document
        password_hash = user_doc.password

        # Use Frappe's password hashing utility to hash the input password
        from frappe.utils.password import get_password_hash

        # Hash the input password
        hashed_input_password = get_password_hash(password_input)

        # Validate the hashed input password against the stored password hash
        if hashed_input_password == password_hash:
            response_message = "Login successful."
        else:
            response_message = "Incorrect password."

except Exception as e:
    response_message = f"An error occurred: {str(e)}"

# Set the response message
frappe.response["message"] = response_message
