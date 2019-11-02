import sqlite_utils
import plistlib

appId = 57

db = sqlite_utils.Database("/var/folders/dz/d8cknx8d387816s0632gqz840000gn/0/com.apple.notificationcenter/db2/db")

SQL = """
    SELECT APP_ID, DATA, PRESENTED, DELIVERED_DATE 
    FROM RECORD 
    WHERE APP_ID IN ({appId}) 
    ORDER BY DELIVERED_DATE DESC
""".format(appId=appId)


def parse_row(row):
    if not row:
        return None

    app_id = row.get('app_id')
    delivered_date = row.get('delivered_date') or 0

    data = plistlib.loads(row.get('data'))
    app = data.get('app')
    req = data.get('req')

    title = req.get('titl')
    body = req.get('body')

    return dict(
        title=title,
        body=body,
        delivered_date=delivered_date,
        app_id=app_id,
        app=app
    )


data_list = db.execute_returning_dicts(SQL)
for row in data_list:
    parsed_row = parse_row(row)

    print(parsed_row)
