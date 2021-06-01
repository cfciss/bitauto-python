import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2118605697669-2147019350688-aFNGeJTnRk8QtUbrytBKHKL6"
 
post_message(myToken,"#stock","jocoding")
