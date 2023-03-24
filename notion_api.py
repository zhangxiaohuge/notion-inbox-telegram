import os
import time
import requests
from notion_client import Client
import datetime
from typing import Dict, Any, List

from config import NOTION_AUTH, NOTION_DATABASE_ID, NOTION_TAG_NAME, NOTION_TAG_VALUE

# Initialize Notion client
notion = Client(auth=NOTION_AUTH)
# Define database ID
database_id = NOTION_DATABASE_ID

WEEKDAYS_DICT: Dict[str, str] = {
    "Monday": "周一",
    "Tuesday": "周二",
    "Wednesday": "周三",
    "Thursday": "周四",
    "Friday": "周五",
    "Saturday": "周六",
    "Sunday": "周日",
}


def get_page(page_title: str) -> Dict[str, Any]:
    existing_page = notion.databases.query(
        **{
            "database_id": database_id,
            "filter": {
                "property": "title",
                "title": {
                    "equals": page_title
                }
            }
        }
    )
    return existing_page


def create_page(page_title: str, tag_value: str, tag_name: str = NOTION_TAG_NAME) -> None:
    new_page = {
        "title": {
            "title": [{"text": {"content": page_title}}]
        },
        tag_name: {"multi_select": [{"name": tag_value}]},
    }
    new_page_content = [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": page_title,
                        }
                    }
                ]
            }
        }
    ]
    notion.pages.create(parent={"database_id": database_id}, properties=new_page, children=new_page_content)


def get_page_content(page_id: str) -> Dict[str, Any]:
    content = notion.blocks.children.list(page_id)
    return content


def append_page(block_id: str, text: str, file_type: str, file_url: str, link_list: List[Tuple[int, int, str, str]]) -> None:
    new_block = [
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text,
                        }
                    }
                ]
            }
        }]
    
    if link_list:
        last_end = 0
        new_block[0]["bulleted_list_item"]["rich_text"] = [{"type": "text","text": {"content":text.split(' - ')[0] + " - "}}]
        text = ' - '.join(text.split(' - ')[1:])
        for start, end, content, url in link_list:
            new_block[0]["bulleted_list_item"]["rich_text"].append({"type": "text","text": {"content": text[last_end:start]}})
            new_block[0]["bulleted_list_item"]["rich_text"].append({"type": "text","text": {"content": content,"link":{"url":url}}})
            last_end = end
        new_block[0]["bulleted_list_item"]["rich_text"].append({"type": "text","text": {"content": text[last_end:]}})
    
    if file_url:
        if "image" in file_type:
            new_block.append({
                "object": "block",
                "type": "image",
                "image": {
                    "type": "external",
                    "external": {
                        "url": file_url
                    }
                }
            })
        elif "video" in file_type:
            new_block.append({
                "object": "block",
                "type": "video",
                "video": {
                    "type": "external",
                    "external": {
                        "url": file_url
                    }
                }
            })
        elif "audio" in file_type:
            new_block.append({
                "object": "block",
                "type": "audio",
                "audio": {
                    "type": "external",
                    "external": {
                        "url": file_url
                    }
                }
            })
        else:
            new_block.append({
                "object": "block",
                "type": "file",
                "file": {
                    "type": "external",
                    "external": {
                        "url": file_url
                    }
                }
            })

    notion.blocks.children.append(block_id, children=new_block)


def insert(text: str, file_type: str = "", file_url: str = "", link_list: List[Tuple[int, int, str, str]] = []) -> None:
    date = datetime.datetime.now()
    weekday = date.strftime("%A")
    page_title = f"{date.strftime('%Y-%m-%d')} {WEEKDAYS_DICT[weekday]}"
    existing_page = get_page(page_title)
    
    if not existing_page["results"]:
        create_page(page_title, NOTION_TAG_VALUE)
        time.sleep(2)  # Wait for the new page to be available
        existing_page = get_page(page_title)
    
    page_id = existing_page["results"][0]["id"]
    content = get_page_content(page_id)
    block_id = content["results"][-1]["id"]
    append_page(block_id, text, file_type, file_url, link_list)

