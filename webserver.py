from flask import Flask, request
import requests
import json

app = Flask(__name__)

# 定义 Webhook 的 Secret Token
SECRET_TOKEN = "define_your_tocken_here"

# 定义目标 Webhook URL
TARGET_WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=your_robot_key"

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # 验证 Secret Token
    token = request.headers.get('X-Gitlab-Token')
    print(token)
    if token != SECRET_TOKEN:
        return 'Unauthorized', 401

    # 解析 JSON 数据

    payload = request.get_json()


    user_name=payload["user_name"]
    commit=payload["commits"][0]["url"]
    commit=commit.replace("yourgitlab.domain.com","192.xxx.xxx.xxx") //内网情况下，可能需要换成真实ip
    message=payload["commits"][0]["message"]
    wechatRobotMessage ={
        "msgtype": "text",
        "text": {
            "content": "Ding! 有人提代码了\n" + "姓名：" + user_name + "\n" + "Commit：" + commit + "\n" + "Message：" + message
        }
    }

    # 转发至目标 Webhook URL
    response = requests.post(TARGET_WEBHOOK_URL, json=wechatRobotMessage)
    
    if response.status_code == 200:
        return 'Webhook forwarded successfully'
    else:
        return 'Failed to forward webhook', response.status_code

if __name__ == '__main__':
    app.run(host='xxx.xxx.xxx.xxx', port=5000) //xxx替换成程序运行的ip
