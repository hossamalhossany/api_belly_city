# Fetch username and password from the request
username = frappe.form_dict.get("username")
password_input = frappe.form_dict.get("password")

# Initialize response message
response_message = ""

try:
    # Retrieve the user document
    user_list = frappe.get_all("User", filters={"name": username}, limit_page_length=1)

    # Check if a user was found
    if not user_list:
        response_message = "User does not exist."
    else:
        # Get the user document directly
        user = frappe.get_doc("User", user_list[0].name)

        # Check if the user exists and validate the password
        if user.check_password(password_input):
            response_message = "Login successful."
        else:
            response_message = "Incorrect password."

except Exception as e:
    response_message = f"An error occurred: {str(e)}"

# Set the response message
frappe.response["message"] = user
