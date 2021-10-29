import motor.motor_asyncio
from decouple import config

MONGO_URL = config("MONGO_URL")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.bugme

# Collections
user_collection = db.get_collection("users")
brand_collection = db.get_collection("brands")
apps_collection = db.get_collection("apps")
bug_collection = db.get_collection("bugs")
slack_collection = db.get_collection("slack")
clickup_collection = db.get_collection("clickup")
jira_collection = db.get_collection("jira")
