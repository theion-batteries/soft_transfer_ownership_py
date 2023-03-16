import requests
from github import Github

# Set up authentication with a personal access token
access_token = 'XXXXXXXX'
g = Github(access_token)

# Define the source and destination owners
source_owner = 'theionSami'
dest_org = 'theion-batteries'

# Get a list of repositories owned by the source owner
repos = g.get_user(source_owner).get_repos()

# Loop over the repositories and transfer ownership to the destination organization
for repo in repos:
    try:
        # Construct the API endpoint URL
        url = f'https://api.github.com/repos/{source_owner}/{repo.name}/transfer'

        # Set the request headers and body
        headers = {'Authorization': f'token {access_token}'}
        body = {'new_owner': dest_org}

        # Send the API request
        response = requests.post(url, headers=headers, json=body)

        # Check the response status code
        if response.status_code == 202:
            print(f'Successfully transferred {repo.name} to {dest_org}.')
        else:
            print(f'Failed to transfer {repo.name}: {response.content}')
    except Exception as e:
        print(f'Error transferring {repo.name}: {str(e)}')
