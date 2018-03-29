import time
import os
from sqlalchemy import true, false

port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)

from HandlerBot import HandlerBot

TOKEN = "512426147:AAGBYAM9R-kL7X8Q5R9sZgG58pVt5rR2EsI"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

bot=HandlerBot(TOKEN, URL)
bot.train("chatterbot.corpus.english")
def main():
    last_update_id = None
    #last_textchat = (None, None)
    while True:
        updates = bot.get_updates(last_update_id)
        #text, chat = bot.get_last_chat_id_and_text(bot.get_updates())

        if len(updates["result"]) > 0:
            last_update_id = bot.get_last_update_id(updates) + 1
            bot.echo_all(updates)

            #last_textchat = (whatToSend, chat)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
