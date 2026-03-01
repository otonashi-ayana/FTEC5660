import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY", "test"), base_url="https://api.deepseek.com")
print(client.base_url)
