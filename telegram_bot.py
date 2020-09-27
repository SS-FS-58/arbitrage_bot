#!/usr/bin/env python
# coding: utf-8

import requests
import json

class telegram():
    tg_url_bot_general = "https://api.telegram.org/bot"

    def http_get(self, url):
        res = requests.get(url, proxies=self.proxies)
        answer = res.text
        # answer_json = json.loads(answer.decode('utf8'))
        answer_json = json.loads(answer)
        return answer_json

    def __init__(self, key, chat_id):
        self.debug = False
        self.key = key
        self.to  = chat_id
        self.proxies = {}
        self.type = "private"  # 'private' for private chats or 'group' for group chats
        self.markdown = False
        self.html = False
        self.disable_web_page_preview = False
        self.disable_notification = False
        self.reply_to_message_id = 0
        self.tmp_uids = None

    def get_me(self):
        url = self.tg_url_bot_general + self.key + "/getMe"
        me = self.http_get(url)
        return me

    def get_updates(self):
        url = self.tg_url_bot_general + self.key + "/getUpdates"
        if self.debug:
            print(url)
        updates = self.http_get(url)
        if self.debug:
            print("Content of /getUpdates:")
            print(updates)
        if not updates["ok"]:
            print(updates)
            return updates
        else:
            return updates

    def message(self, message):
        url = self.tg_url_bot_general + self.key + "/sendMessage"
        # message = "\n".join(message)
        params = {"chat_id": self.to, "text": message, "disable_web_page_preview": self.disable_web_page_preview,
                  "disable_notification": self.disable_notification}
        if self.reply_to_message_id:
            params["reply_to_message_id"] = self.reply_to_message_id
        if self.markdown or self.html:
            parse_mode = "HTML"
            if self.markdown:
                parse_mode = "Markdown"
            params["parse_mode"] = parse_mode
        if self.debug:
            print("Trying to /sendMessage:")
            print(url)
            print("post params: " + str(params))
        res = requests.post(url, params=params, proxies=self.proxies)
        answer = res.text
        # answer_json = json.loads(answer.decode('utf8'))
        answer_json = json.loads(answer)
        if not answer_json["ok"]:
            print(answer_json)
            return answer_json
        else:
            return answer_json

if __name__ == "__main__":
    chat_id    = 'your id'
    chat_token = 'your token'

    tg = telegram(chat_token, chat_id)
    result = tg.message("hello my friend!!!")
