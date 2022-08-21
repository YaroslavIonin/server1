from flask import Flask, request

app = Flask(__name__)
ListOfMessages = []


@app.route('/')
def hello_world():
    return 'Server is running!' \
           '<br><a href="/status">Check status</a>'


@app.route('/status')
def status():
    return {
        'message_count': len(ListOfMessages)
    }


@app.route('/api/messanger', methods=['POST'])
def send_message():
    msg = request.json
    print(msg)
    ListOfMessages.append(msg)
    msg_text = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Всего сообщений: {len(ListOfMessages)} Посланное сообщение: {msg_text}")
    return f"Сообщение отослано успешно. Всего сообщений: {len(ListOfMessages)}", 200


@app.route("/api/messanger/<int:id>")
def get_message(id):
    if 0 <= id < len(ListOfMessages):
        return ListOfMessages[id], 200
    else:
        return "Not found", 400


if __name__ == '__main__':
    app.run()
