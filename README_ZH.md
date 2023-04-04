# notion-inbox-telegram-plugin
这是一个简单的插件，可以从 Telegram bot 获取新的消息并将其同步到Notion页面块。

[中文](https://github.com/cooolr/notion-inbox-telegram-plugin/blob/main/README_ZH.md) | [English](https://github.com/cooolr/notion-inbox-telegram-plugin/blob/main/README.md)

## 准备工作

1. 创建一个 [集成](https://www.notion.com/my-integrations) 并找到 token。
2. 定位到您的 Notion 数据库并复制其 database_id。
3. 从您的Notion数据库添加连接绑定到第一步创建的integration名字。
4. 设置您的Notion数据库页面模板，必须添加一个Multi-select类型的property命名为Tags，和config.py NOTION_TAG_NAME参数对应。
5. 创建一个Telegram bot并获取token。
6. 在 `config.py` 中配置设置。

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

## 安装依赖

``` bash
pip install -r requirements.txt
```

## 快速开始

``` bash
python3 main.py
```

将 Telegram 机器人添加到聊天中，然后开始发送消息。

## 功能

1. 将来自 Telegram 的文本、图片、文档、视频笔记和语音消息记录到 Notion 数据库。
2. 自动将语音消息转换为文本（可选，需要百度语音 API）。
3. 管理消息中的链接并将它们添加到 Notion 数据库。

## 注意事项

1. 确保您拥有 Telegram 和 Notion 所需的 API 密钥和令牌。
2. 百度语音 API 是可选的，需要额外配置，并且安装ffmpeg。

## 效果图

![demo](https://github.com/cooolr/notion-inbox-telegram-plugin/raw/main/demo.png)
