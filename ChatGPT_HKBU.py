import os
import requests

class HKBU_ChatGPT:
    def __init__(self):
        # 从环境变量中获取配置
        self.basic_url = os.environ['BASICURL']
        self.model_name = os.environ['MODELNAME']
        self.api_version = os.environ['APIVERSION']
        self.access_token = os.environ['CHATGPT_ACCESS_TOKEN']

    def submit(self, message):
        conversation = [{"role": "user", "content": message}]
        # 构造请求的完整 URL
        url = (
            f"{self.basic_url}/deployments/{self.model_name}"
            f"/chat/completions/?api-version={self.api_version}"
        )
        # 构造请求头
        headers = {
            'Content-Type': 'application/json',
            'api-key': self.access_token
        }
        # 请求体
        payload = {'messages': conversation}
        
        # 发送请求
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            # 返回错误信息，方便调试
            return f"Error: {response.status_code}", response.text

if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()
    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)
