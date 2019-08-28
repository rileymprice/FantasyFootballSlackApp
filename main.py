import os
import re
import logging
import time
import slack

BOT_OAUTH_TOKEN = os.environ["SLACK_BOT_OAUTH_ACCESS_TOKEN"]
# BOT_OAUTH_TOKEN = "kjsdf"
BOT_NAME = "fantasybot"
BOT_MENTION_REGEX = "^<@UM95JLU5T>"
# BOT_MENTION_REGEX = f"<@{BOT_NAME}>"
ALAN_MENTION_REGEX = "[^a-zA-Z](alan)[^a-zA-Z]|^(alan)[^a-zA-Z]|[^a-zA-Z](alan)"
DIRECTORY = os.getcwd()
logging_file_loc = f"{DIRECTORY}\\fantasybot.log"

logger = logging.getLogger("Fantasybot")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(logging_file_loc)
formatter = logging.Formatter(
    "%(asctime)s ||| %(name)s ||| %(levelname)s ||| %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


rtm_client = slack.RTMClient(token=BOT_OAUTH_TOKEN)


@slack.RTMClient.run_on(event="message")
def message_handler(**payload):
    data = payload["data"]
    sub_type = data["subtype"] if "subtype" in data else None
    if sub_type == "bot_message":
        logger.debug(f"Response:  {payload}")
    elif sub_type in ["group_join", "channel_join"]:
        pass
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

        if alan_mentioned or text.lower() == "alan":
            response_text = "Fuck off Alan!"
            web_client.chat_postMessage(channel=channel_id, text=response_text)
        elif bot_mentioned:
            response_text = "Working on it"
            web_client.chat_postMessage(channel=channel_id, text=response_text)
        else:
            pass
        # TODO Insert commands for Bot to do with Alan


# Bot was invited to a private channel
@slack.RTMClient.run_on(event="group_joined")
def private_channel_added(**payload):
    logger.critical(f"Private: {payload}")
    # logger.info('Private Channel: {}')


# Bot was invited to a channel
@slack.RTMClient.run_on(event="channel_joined")
def channel_added(**payload):
    logger.critical(f"Channel: {payload}")


# Verifies the bot connected successfully
@slack.RTMClient.run_on(event="hello")
def say_hello(**payload):
    # time_now = time.now()
    logger.info(f"Bot connected via HELLO {payload}")


rtm_client.start()
