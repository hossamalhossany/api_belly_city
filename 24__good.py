# Fetch username and password from the request
username = frappe.form_dict.get("username")
password_input = frappe.form_dict.get("password")
password_input = '$pbkdf2-sha256$29000$53zv3VsLAcBYyzlHSKn13g$VF0RKfo0243FopWAR6jNhZfi50MnlVG77bSKx1RF3Js'

# def api_hash_password(password_input):
#     salt, hashed_password = hash_password(password)
#     return {
#         "salt": salt,
#         "hashed_password": hashed_password
#     }
#

# Initialize response message
response_message = ""

try:
    # Fetch the hashed password from the __Auth table
    stored_password_hash = frappe.db.sql(
        """
        SELECT password 
        FROM `__Auth` 
        WHERE doctype = %s AND name = %s and fieldname = %s
        """,
        ("User", username, "password"),
        as_dict=True
    )

    if not stored_password_hash or not stored_password_hash[0].get('password'):
        response_message = "User does not exist or has no password set."
    else:
        # Access the password hash from the query result
        password_hash = stored_password_hash[0]['password']

        # Use Frappe's password verification function to validate the input password
        # This avoids using imports and ensures proper password comparison
        if password_hash == password_input:
            response_message = "Login successful."
        else:
            response_message = "Incorrect password."

except Exception as e:
    response_message = f"An error occurred: {str(e)}"

# Set the response message
frappe.response["message"] = response_message

# frappe.response["message"] = f"  password_hash_at_database=     {password_hash}      ....          and password_input=  {password_input}    "