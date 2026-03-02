import requests
from datetime import datetime

def submit_google_form():
    # The URL ends in /formResponse to submit the data directly
    url = "https://docs.google.com/forms/d/e/1FAIpQLSdIPMAsgCqNNP_5BliHIhde01LXw2lfSalCDegQu3tmMiihlw/formResponse"
    
    # Replace the values on the right with your actual answers
    form_data = {
        "entry.1339829787": "Ankon", 
        "entry.2052905156": "Manager",
        "entry.432399424": "1)Take backup of Database
        2)Assign Products 
        3)Active products
        4)Fix Products Issue from Messenger group
        "
    }
    
    try:
        print("Sending data to Google Forms...")
        # requests.post sends the data instantly without opening a browser
        response = requests.post(url, data=form_data)
        
        # Google returns status code 200 if it was successful
        if response.status_code == 200:
            print(f"SUCCESS: Form submitted at {datetime.now()}!")
        else:
            print(f"FAILED: Google returned status code {response.status_code}")
            
    except Exception as e:
        print(f"ERROR: Something went wrong: {e}")

if __name__ == "__main__":
    submit_google_form()