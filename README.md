# notion-inbox-telegram-plugin
This is simple plugin that get new messages from Telegram bot and paste its to page block.

[中文](https://github.com/cooolr/notion-inbox-telegram-plugin/blob/main/README_ZH.md) | [English](https://github.com/cooolr/notion-inbox-telegram-plugin/blob/main/README.md)

## Prepare

1. Create an [integration](https://www.notion.com/my-integrations) and find the token.
2. Locate your Notion database and copy its database_id.
3. Add connections from your notion database.
4. To set your Notion database page template, must add a Multi-select type property named Tags, which corresponds to the NOTION_TAG_NAME parameter in config.py.
5. Create a telegram bot and get token.
6. Configure the settings in `config.py`.

``` python
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
```

## Install dependencies

``` bash
pip install -r requirements.txt
```

## Quick start

``` bash
python3 main.py
```

Add the Telegram bot to a chat and start sending messages.

## Features

1. Log text, images, documents, video notes, and voice messages from Telegram to a Notion database.
2. Automatically convert voice messages to text (optional, requires Baidu Speech API).
3. Manage links in messages and add them to the Notion database.

## Note

1. Make sure you have the required API keys and tokens for Telegram and Notion.
2. The Baidu Speech API is optional and requires additional configuration, and install ffmpeg.

## Screenshots
![property](https://github.com/cooolr/notion-inbox-telegram-plugin/raw/main/property.png)
![demo](https://github.com/cooolr/notion-inbox-telegram-plugin/raw/main/demo.png)
