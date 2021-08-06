from app.database.crud.app import add_new_app, retrive_apps_of_bundles
from app.database.crud.brand import retrieve_brand_from_auth_key


"""
    Client POST bugs from client sdk with auth_key of brand
    get Brand details
    get apps for the bundle ids
    match bundle id
        if the bundle id is new, 
            create a new app.
            
    put brand id into the bug data
"""


async def bundle_id_handler(auth_key: str, bug_data: dict) -> dict:
    # Platform safecheck
    bug_data['platform'] = bug_data['platform'].upper()
    
    brand = await retrieve_brand_from_auth_key(auth_key)
    print(f"brand response: {brand}")
    apps = await retrive_apps_of_bundles(bug_data['bundle_id'], bug_data['platform'])
    print(f"Apps response: {apps}")
    if len(apps) < 1:
        await add_new_app({
            "brand_id": brand['id'],
            "user_id": brand['user_id'],
            "bundle_id": bug_data['bundle_id'],
            "platform": bug_data['platform'],
            "slack_integration": False,
            "clickup_integration": False
        })
        print(f"New app created for bundle:{bug_data['bundle_id']} for {bug_data['platform']}")

    if bug_data or bug_data['brand_id']:
        bug_data['brand_id'] = brand['id']
    else:
        bug_data = {**bug_data, "brand_id": brand['id']}
    return bug_data
