import requests
import base64
import os

class GitHubHelper:
    def __init__(self, token=None, repo=None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.repo = repo or os.getenv("GITHUB_REPO") # format: "username/repo"
        
    def upload_file(self, file_path, branch="main"):
        if not self.token or not self.repo:
            return False, "GitHub Token or Repo not configured."
        
        file_name = os.path.basename(file_path)
        url = f"https://api.github.com/repos/{self.repo}/contents/writeups/{file_name}"
        
        with open(file_path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf-8")
            
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        data = {
            "message": f"Upload writeup: {file_name}",
            "content": content,
            "branch": branch
        }
        
        # Check if file exists to get SHA (for update)
        get_res = requests.get(url, headers=headers)
        if get_res.status_code == 200:
            data["sha"] = get_res.json()["sha"]
            
        res = requests.put(url, headers=headers, json=data)
        
        if res.status_code in [200, 201]:
            return True, f"Successfully uploaded to GitHub: {self.repo}"
        else:
            return False, f"GitHub Error: {res.json().get('message', 'Unknown error')}"
