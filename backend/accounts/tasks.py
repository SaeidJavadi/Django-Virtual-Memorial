"""
This is a **public-ready SMS sending stub** for the Virtual Memorial project.

IMPORTANT:
- The `DEFAULT_PHONE` field must be replaced by users with their real phone numbers
  or connected to their own SMS sending service (like Ghasedak, Kavenegar, Twilio, etc.)
- The send_sms function currently **prints the code** instead of sending it via SMS.
- Users must implement their own SMS sending logic to actually send messages and get tokens.
"""


def send_sms(phone, code=None):
    """
    Stub function to simulate sending an SMS with a verification code.
    
    Parameters:
    - phone (str): The recipient phone number.
    - code (str | int): The verification code to send.
    
    Returns:
    - str: The code that would have been sent.
    """
    if code is None:
        code = "1234"  # Default code if not provided

    # Demo output: prints the code instead of sending an SMS
    print("+" * 10, "New Code", "+" * 10)
    print(f"Phone: {phone}")
    print(f"Code: {code}")
    print("Note: This is a stub. Implement your own SMS sending logic here.")
    print("+" * 10, "New Code", "+" * 10)

    # Return the code for confirmation/testing purposes
    return code
