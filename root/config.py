
import os 

class Config(object):
  APP_ID = int(os.environ.get("APP_ID", "1976680"))
  API_HASH = os.environ.get("API_HASH", "9073255ce64a6072a59099803493f97d")
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
  AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1940030638").split())
  DOWNLOAD_LOCATION = "./bot/DOWNLOADS"
  DB_URI = os.environ.get("DATABASE_URL", "")
  # owner is for log cmd only owner can use (this can be multiple users)
  OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "1940030638").split(" ")]
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "dcbotsa")
  CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION",False)
