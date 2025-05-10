from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

notion = Client(auth=NOTION_TOKEN)

def get_items():
    response = notion.databases.query(database_id=NOTION_DATABASE_ID)
    items = []
    for r in response['results']:
        props = r['properties']
        title = props['Название']['title'][0]['text']['content']
        content = props['Содержание']['rich_text'][0]['text']['content']
        command = props['Команда']['rich_text'][0]['text']['content']
        access = props['Тип']['select']['name'] if props['Тип']['select'] else 'бесплатно'
        items.append({"title": title, "content": content, "command": command, "access": access})
    return items

def get_item_by_command(cmd):
    for item in get_items():
        if item['command'] == cmd:
            return item
    return None
