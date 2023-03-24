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
NOTION_TAG_VALUE = "日志"

# Speech configuration
# 使用百度短语音普通话转文字标准版api，按调用量后付费0.0034元/次，https://cloud.baidu.com/product/speech/asr
# 默认关闭，如要开启，申请相应参数填入并设置SPEECH_TO_TEXT=True
SPEECH_TO_TEXT = False
SPEECH_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxx"
SPEECH_SECRET_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
