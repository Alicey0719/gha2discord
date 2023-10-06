import os
import sys

from utils.sendwebhook import SendWebhook
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    webhook_url = os.environ.get("WEBHOOK_URL", None)
    try:
        if webhook_url is None:
            raise Exception(f"WEBHOOK_URL is not found: {webhook_url}")
    except:
        traceback.print_exc()

    sw = SendWebhook(webhook_url)
    sw.username = os.environ.get("MESSAGE_USERNAME", "GitHubActions")
    sw.avatar_url = os.environ.get("MESSAGE_AVATAR_URL", "")
    sw.author_name = os.environ.get("MESSAGE_AUTHORNAME", "GitHubAvtions Notification")
    sw.author_icon_url = os.environ.get("MESSAGE_AUTHORICON_URL", "")
    comment = os.environ.get("MESSAGE_COMMENT", "default message")

    # message = str(" ".join(sys.argv[1:]))
    sw.send_embed_message(comment, level_color=sw.Level.info)
    print(f"send message:\n{comment}")