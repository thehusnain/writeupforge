import requests
import os

class LinkedInHelper:
    def __init__(self, access_token=None):
        self.access_token = access_token or os.getenv("LINKEDIN_ACCESS_TOKEN")
        self.member_id = os.getenv("LINKEDIN_MEMBER_ID")
        
    def share_post(self, title, summary, link=""):
        if not self.access_token or not self.member_id:
            return False, "LinkedIn Credentials not configured."
        
        url = "https://api.linkedin.com/v2/ugcPosts"
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "X-Restli-Protocol-Version": "2.0.0",
        }
        
        post_data = {
            "author": f"urn:li:person:{self.member_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": f"Just finished a new cybersecurity writeup: {title}\n\n{summary}\n\n{link}"
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        
        res = requests.post(url, headers=headers, json=post_data)
        
        if res.status_code == 201:
            return True, "Successfully shared on LinkedIn!"
        else:
            return False, f"LinkedIn Error: {res.json().get('message', 'Unknown error')}"
