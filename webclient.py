import requests
import json

def send_webhook(message):
    # 定义 Web 服务的 URL
    webhook_url = "http://192.xxx.xxx.xxx:5000/webhook"

    # 定义请求头部，包含 Secret Token
    headers = {
        "X-Secret-Token": "your_tocken",
        "Content-Type": "application/json"
    }

    # 构建要发送的 JSON 数据
    payload = {
        "message": message
    }

    # 发送 POST 请求
    response = requests.post(webhook_url, headers=headers, json=payload)
    
    # 检查响应状态码
    if response.status_code == 200:
        print("Webhook sent successfully")
    else:
        print("Failed to send webhook:", response.status_code)

# 发送一条包含 "hello" 的 Webhook
send_webhook("hello")
