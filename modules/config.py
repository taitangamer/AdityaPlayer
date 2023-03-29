import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID","27241643"))
API_HASH = getenv("API_HASH","a2882ef0d9c47bc7b885a54e4c6f10cc")
BOT_TOKEN = getenv("BOT_TOKEN","6101414253:AAFloqp7iMcIwjeGrQrzo3mRgPB37r_fL3Y")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION","1BVtsOLEBu7dIFZCjmE4m__F38NlQnii9STRifqs-CoAB-9CKooQRIZ4QfVDERBD7_11G8D-3q0ybDxVRicR-ExJ733MQV0Ps4EkWM5gwQL4mTW8MpZLCVIHKJuPH5etISG-suupH2H20aN82Zxf3GFRtC2fz9Igk2W6MiZ_GDnZ3uExMu6hT_q-1YBICae9JojDaONkvCRv5x0LpFCNY9NCSS9k-zcolVwZ2GuwfK3VduB9aq0vbUkew3taXWz1x3JU0B8LYVuzNoHIbsKMrBXyNC8eC-yiF4A0OqLAGUpMazG1k3pAueMZBd3M-W0k_2b9J_ai8pta75lpoQhWNYnyflkWwYwA=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
aiohttpsession = aiohttp.ClientSession()
