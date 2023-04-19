import os
import json

# Telegram configuration
TELEGRAM_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Notion configuration
# create an [integration](https://www.notion.com/my-integrations) and find the token.
NOTION_AUTH = "secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# https://www.notion.so/<username>/<database_id>?v=<view_id>
NOTION_DATABASE_ID = "xxxxxxxxxxxxxxxxxxxxxxxxx"

# 标签名称
NOTION_TAG_NAME = "Tags"

# 标签属性
NOTION_TAG_VALUE = "Daily"

# Speech configuration
# 使用百度短语音普通话转文字标准版api，按调用量后付费0.0034元/次，https://cloud.baidu.com/product/speech/asr
# 默认关闭，如要开启，申请相应参数填入并设置SPEECH_TO_TEXT=True
SPEECH_TO_TEXT = False
SPEECH_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxx"
SPEECH_SECRET_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 代理
PROXY_URL = ""

# 从环境变量获取
env = os.environ
if env.get("TELEGRAM_TOKEN"):
    TELEGRAM_TOKEN = env.get("TELEGRAM_TOKEN")
if env.get("NOTION_AUTH"):
    NOTION_AUTH = env.get("NOTION_AUTH")
if env.get("NOTION_DATABASE_ID"):
    NOTION_DATABASE_ID = env.get("NOTION_DATABASE_ID")
if env.get("NOTION_TAG_NAME"):
    NOTION_TAG_NAME = env.get("NOTION_TAG_NAME")
if env.get("NOTION_TAG_VALUE"):
    NOTION_TAG_VALUE = env.get("NOTION_TAG_VALUE")
if env.get("SPEECH_TO_TEXT"):
    SPEECH_TO_TEXT = json.loads(env.get("SPEECH_TO_TEXT"))
if env.get("SPEECH_API_KEY"):
    SPEECH_API_KEY = env.get("SPEECH_API_KEY")
if env.get("SPEECH_SECRET_KEY"):
    SPEECH_SECRET_KEY = env.get("SPEECH_SECRET_KEY")
if env.get("PROXY_URL"):
    PROXY_URL = env.get("PROXY_URL")

proxies = {"http": PROXY_URL, "https": PROXY_URL}
