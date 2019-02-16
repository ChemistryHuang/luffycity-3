import redis
import json

conn = redis.Redis(host='140.143.227.206',port=6379,password='1234')
"""
-----> 第一版
{
    luffy_shopping_car:{
        6:{
            11:{
                'title':'21天入门到放弃',
                'src':'xxx.png'
            },
            12:{
                'title':'21天入门到放弃',
                'src':'xxx.png'
            }
        }
    }
}
-----> 第二版
{
    luffy_shopping_car_6_11:{
        'title':'21天入门到放弃',
         'src':'xxx.png'
    },
    luffy_shopping_car_6_12:{
        'title':'21天入门到放弃',
         'src':'xxx.png'
    },
    luffy_shopping_car_6_14:{
        'title':'21天入门到放弃',
         'src':'xxx.png'
    }
}
"""
# conn.flushall()

# 添加课程
# redis_key = "luffy_shopping_car_%s_%s" %(7,12,)
# conn.hmset(redis_key,{'title':'21天入门到放弃','src':'xxx.png'})

# 删除课程
# conn.delete('luffy_shopping_car_6_12')
# print(conn.keys())

# 修改课程
# conn.hset('luffy_shopping_car_6_11','src','x1.png')
# print(conn.hget('luffy_shopping_car_6_11','src'))

# 查看所有课程
# print(conn.keys("luffy_shopping_car_6_*"))
# for item in conn.scan_iter('luffy_shopping_car_6_*',count=10):
#     course = conn.hgetall(item)
#     print(course)

# conn.set('k1',123)
# print(conn.type('luffy_shopping_car_6_11'))
# print(conn.type('k1'))

from django.core.cache import cache






# print(conn.keys())
#
# for key in conn.scan_iter("luffy_shopping_car_1*"):
#
#     title = conn.hget(key,'title')
#     img = conn.hget(key, 'img')
#     policy = conn.hget(key, 'policy')
#     default_policy = conn.hget(key, 'default_policy')
#
#
#     print(str(title,encoding='utf-8'))
#     print(str(img,encoding='utf-8'))
#     print(json.loads(str(policy,encoding='utf-8')))
#     print(str(default_policy,encoding='utf-8'))




print(conn.keys())
conn.scan_iter()

print(conn.exists('luffy_sg_car_1_1'))



