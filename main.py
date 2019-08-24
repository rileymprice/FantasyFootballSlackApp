import os
import re
import logging
import slack

BOT_OAUTH_TOKEN = os.environ["SLACK_BOT_OAUTH_ACCESS_TOKEN"]
BOT_NAME = "fantasybot"
BOT_MENTION_REGEX = "^<@UM95JLU5T>"
# BOT_MENTION_REGEX = f"<@{BOT_NAME}>"
ALAN_MENTION_REGEX = "[^a-zA-Z](alan)[^a-zA-Z]|^(alan)[^a-zA-Z]"

logger = logging.getLogger("Fantasybot")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    "C:\\Users\\Riley Price\\Documents\\GitHub\\FantasyFootballSlackApp\\fantasybot.log"
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

rtm_client = slack.RTMClient(token=BOT_OAUTH_TOKEN)


@slack.RTMClient.run_on(event="message")
def message_handler(**payload):
    data = payload["data"]
    sub_type = data["subtype"] if "subtype" in data else None
    if sub_type == "bot_message":
        logger.debug(f"Response:  {payload}")
    else:
        logger.debug(f"Request: {payload}")
        user = data["user"]
        # print(payload)
        thread_ts = data["ts"]
        web_client = payload["web_client"]
        text = data["text"]
        channel_id = data["channel"]
        # print(data["text"])
        bot_mentioned = re.search(BOT_MENTION_REGEX, text, re.IGNORECASE)
        print("bot", bot_mentioned)
        alan_mentioned = re.search(ALAN_MENTION_REGEX, text, re.IGNORECASE)
        print("alan", alan_mentioned)

        if bot_mentioned:
            response_text = "Working on it"
        elif alan_mentioned:
            response_text = "Fuck you Alan!"
        else:
            response_text = f"Hi <@{user}>"
            # TODO Insert commands for Bot to do with Alan
        web_client.chat_postMessage(channel=channel_id, text=response_text)


rtm_client.start()
