from pony.orm import db_session, Required
from components.db import init_db
from components.db import db
from components.env import init_env
import uuid
import datetime
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
# 生成一个随机的 UUID
random_uuid = str(uuid.uuid4())
print('random_uuid====>', random_uuid)
init_env()
init_db();

class Audio(db.Entity):
  title = Required(str)
  url = Required(str)
  uuid = Required(str)
  created_at = Required(str)
  update_at = Required(str)
  description = Required(str)
  
db.generate_mapping(create_tables=True)

# 增加数据
@db_session
def insert_audio(title, description, url, uuid=random_uuid, created_at=current_time, update_at=current_time):
    new_audio = Audio(title=title, description=description, url=url, uuid=uuid, created_at=created_at, update_at=update_at)
    return;
  
# insert_audio('动物', 'https://demo1', random_uuid, current_time, current_time);


# 删除数据
@db_session
def delete_audio_by_uuid(uuid: [str]):
    db.execute("DELETE from audio WHERE uuid=$uuid")

    return

# delete_audio_by_uuid('2fc939ed-d6df-4dc5-a83c-387e5d2791e1');

# 更新数据
@db_session
def update_audio_by_uuid(uuid: [str], title: str):
    db.execute("UPDATE audio SET title=$title WHERE uuid=$uuid")

    return
  
# update_audio_by_uuid('6165b085-873d-4fb5-983e-69fae3e0c000', '动物');

# 查询数据
@db_session
def get_audio_list():
    rows = db.select(
        "SELECT * FROM audio"
    )
    
    print("rows=====>", rows)
  
# get_audio_list();
