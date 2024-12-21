# Fetch username and password from the request
username = frappe.form_dict.get("username")
password_input = frappe.form_dict.get("password")

# Initialize response message
response_message = ""

try:
    # Retrieve the user list
    user_list = frappe.get_all("User", filters={"name": username}, limit_page_length=1)

    if not user_list:
        response_message = "User not found."
    else:
        # Retrieve the user document
        user = frappe.get_doc("User", user_list[0].name)

        if user:
            # Compare the input password with the stored password
            if user.check_password(password_input):
                response_message = "Login successful."
            else:
                response_message = "Incorrect password."
        else:
            response_message = "User document retrieval failed."
except Exception as e:
    response_message = f"An error occurred: {str(e)}"

# Set the response message
frappe.response["message"] = response_message