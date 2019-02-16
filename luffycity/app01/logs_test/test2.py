import json

v = {
    1:'db',
    2:'sb',
}

s = json.dumps(v)
print(json.loads(s))

import redis
import json

conn = redis.Redis(host='140.143.227.206',port=6379,password='1234')

# for key in conn.scan_iter("luffy_payment_1_*"):
#     conn.delete(key)

# key_list = conn.keys("luffy_payment_1_*")
# conn.delete(*key_list)

print(conn.keys())