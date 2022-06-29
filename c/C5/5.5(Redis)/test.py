import redis
import json

red = redis.Redis(
    host='redis-13602.c300.eu-central-1-1.ec2.cloud.redislabs.com',
    port=13602,
    password='MTnIqelhXe9f71UnfCQEor7txRliJV6R'
)

dict1 = {'key1' : 'value1', 'key2' : 'value2'}
red.set('dict1', json.dumps(dict1))
converted_dict = json.loads(red.get('dict1'))
print(type(converted_dict))
print(converted_dict)
red.delete('dict1')
print(red.get('dict1'))
