import requests
from enum import Enum

class SendWebhook:
    class Level(Enum):
        # 10進数のカラーコード
        none = 0000000 # 黒
        info = 8568360 # 緑
        error = 16711731 # 赤

    HEADERS = {'Content-Type': 'application/json',}

    def __init__(self, webhook_url: str) -> None:
        self.webhook_url: str = webhook_url
        self.username: str = None
        self.avatar_url: str = None
        self.level_color: self.Level = self.Level.none
        self.footer_text: str = None
        self.footer_icon_url: str = None
        self.thumbnail_icon_url: str = None
        self.author_name: str = None
        self.author_url: str = None
        self.author_icon_url: str = None

    def send_message(self, message: str) -> None:
        # Webhookに送信するデータの構築
        main_content = {"content": message}

        # POST
        requests.post(self.webhook_url, main_content)

    def send_embed_message(self,
                           description: str,
                           username: str = None,
                           avatar_url: str = None,
                           level_color: Level = None,
                           footer_text: str = None,
                           footer_icon_url: str = None,
                           thumbnail_icon_url: str = None,
                           author_name: str = None,
                           author_url: str = None,
                           author_icon_url: str = None,
                           ) -> None:

        # 指定なし変数のデフォルト値代入
        if username is None: username = self.username
        if avatar_url is None: avatar_url = self.avatar_url
        if level_color is None: level_color = self.level_color
        if footer_text is None: footer_text = self.footer_text
        if footer_icon_url is None: footer_icon_url = self.footer_icon_url
        if thumbnail_icon_url is None: thumbnail_icon_url = self.thumbnail_icon_url
        if author_name is None: author_name = self.author_name
        if author_url is None: author_url = self.author_url
        if author_icon_url is None: author_icon_url = self.author_icon_url

        # Webhookに送信するデータの構築
        data = {
            "username": username,
            "avatar_url": avatar_url,
            "embeds": [{
                "description": description,
                "color": level_color.value,
                "footer": {
                    "text": footer_text,
                    "icon_url": footer_icon_url
                },
                "thumbnail": {
                    "url": thumbnail_icon_url
                },
                "author": {
                    "name": author_name,
                    "url": author_url,
                    "icon_url": author_icon_url
                }
            }]
        }

        # POST
        requests.post(self.webhook_url, headers=self.HEADERS, json=data)
