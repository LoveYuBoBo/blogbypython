import orm
from models import User,Blog,Comment
import asyncio


async def test(loop):
	await orm.creat_pool(loop,user='root',password='141592',database='ds')
	u=User(name='Test',email='test@qq.com',passwd='12345',image='about:blank')
	await u.save()
loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()
