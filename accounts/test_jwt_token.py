import requests
from base64 import b64decode, b64encode

JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjEyMDEwMjM3LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjEyMDA5OTM3fQ.HFzyAAp9DutBadD5ABSfMDNN5Zf3b-7tr6vrb47Kk88'

headers = {
    # 'Authorization': f'Token {TOKEN}',   # Token 인중
    'Authorization': f'JWT {JWT_TOKEN}', # JWT Token 인증
}

res = requests.get("http://localhost:8000/post/", headers=headers)
print(res.json())