from datetime import datetime
from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)

#Save messages in file
DB_FILE = 'data/db.json'

def load_messages():
    json_file = open(DB_FILE, 'r')
    data = json.load(json_file)
    return data['messages']


all_messages = load_messages()

def save_messages():
    data = {
        'messages': all_messages
    }
    json_file = open(DB_FILE, "w")
    json.dump(data, json_file)
    return


all_messages = []

def print_message(msg):
  print(f"[{msg['sender']}]: {msg['text']} / {msg['time']}")


def add_message(sender, text):

  new_message = {
    "sender": sender,
    "text": text,
    "time": datetime.now().strftime('%H:%M:%S'),
  }
# Добавил проверку, система выводит сообщение если ошибка.
  if (len(sender) < 3 or len(sender) >100):
      return redirect(url_for('error'), code=302)
  if (len(text) < 1 or len(text) >3000):
      return redirect(url_for('error'), code=302)
  all_messages.append(new_message)
  save_messages()


@app.route("/get_messages")
def get_messages():
    return {'messages': all_messages}

@app.route('/')
def main_page():
    return 'Hello mazafucka!'

@app.route('/send_message')
def send_message():
    sender = request.args['name']
    text = request.args['text']
    add_message(sender, text)
    return 'OK'

@app.route('/chat')
def display_chat():
    return  render_template('form.html')

@app.route('/error')
def error():
    return 'ERROR'

app.run(host='0.0.0.0', port=80)

test_git = "test1"
