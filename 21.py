# Fetch username and password from the request
username = frappe.form_dict.get("username")
password_input = frappe.form_dict.get("password")

# Initialize response message
response_message = ""

try:
    # Fetch the hashed password from the __Auth table
    stored_password_hash = frappe.db.sql(
        """
        SELECT password 
        FROM `__Auth` 
        WHERE doctype = %s AND name = %s
        """,
        ("User", username),
        as_dict=True
    )

    if not stored_password_hash or not stored_password_hash[0].get('password'):
        response_message = "User does not exist or has no password set."
    else:
        # Access the password hash from the query result
        password_hash = stored_password_hash[0]['password']

        # Use Frappe's password verification function to validate the input password
        # This avoids using imports and ensures proper password comparison
        if frappe.utils.password.is_password_valid(password_hash, password_input):
            response_message = "Login successful."
        else:
            response_message = "Incorrect password."

except Exception as e:
    response_message = f"An error occurred: {str(e)}"

# Set the response message
frappe.response["message"] = response_message1
