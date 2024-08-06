# pip install requests
import requests
import os

# Replace with your actual webhook URL
webhook_url = 'YOUR_WEBHOOK_URL_HERE' 

# Replace with the directory containing your .txt files
directory = 'path/to/your/directory'

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith(".txt"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Open the file in read mode
        with open(file_path, 'r') as file:
            file_contents = file.read()

        # Create the payload for the webhook request
        payload = {'content': file_contents}

        # Send the request to the webhook URL
        response = requests.post(webhook_url, json=payload)

        # Check if the request was successful
        if response.status_code == 204:
            print(f'File "{filename}" sent successfully!')
        else:
            print(f'Error sending file "{filename}".')
