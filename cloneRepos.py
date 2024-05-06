import os
import requests


username = '#enter username here'
token = '#enter token here'

# Function to clone repositories and set up personal remote
def clone_repos(organization_name, repo_names):
    for repo_name in repo_names:
        # Constructing the clone URL using SSH
        clone_url = f'git@github.com:{organization_name}/{repo_name}.git'
        
        # Create the repository on GitHub
        url = f'https://api.github.com/user/repos'
        headers = {'Authorization': f'token {token}'}
        data = {'name': repo_name, 'private' : True}
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            print(f'Repository {repo_name} created successfully!')
            # Clone the repository
            os.system(f'git clone {clone_url}')
            # Change directory to the cloned repository
            os.chdir(repo_name)
            # Add a personal remote
            os.system(f'git remote add personal git@github.com:{username}/{repo_name}.git')
            os.system(f'git push personal')
            
        else:
            print(f'Failed to create repository {repo_name}: {response.status_code}')
            return False
    return True
        
def main():
    organization_name = 'Boise-State-University-CS-121'
    repo_list_file = 'fileName.txt'
    
    with open(repo_list_file, 'r') as file:
        repo_names = [line.strip() for line in file.readlines() if line.strip()]
    
        if repo_names:
            clone_repos(organization_name, repo_names)
            print("Repositories cloned successfully!")
        else:
            print("No repositories found in the list file.")

if __name__ == "__main__":
     main()

