import time
import asyncio
from aiohttp import ClientSession

tasks = []
url = "http://ibaby.ipadown.com/api/zuowen/zw.detail.php"
async def getDeatilDatasWithID(url,id,semaphore):
    async with semaphore:
        async with ClientSession() as session:
            async with session.get(url, params={'id':id}) as response:
                # response = await response.read()
                # print(response)
                print('Hello World:%s' % time.time())
                return await response.text(encoding='utf-8')

def runGetDeatil(id_list):
    semaphore = asyncio.Semaphore(5)  # 限制并发量为500
    for id in id_list:
        task = asyncio.ensure_future(runGetDeatil(url.format(id),semaphore))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))
    print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(run())
    runGetDeatil()
    loop.close()