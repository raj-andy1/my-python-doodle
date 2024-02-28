import aiohttp
import asyncio
import csv


async def by_aiohttp_concurrency(file):
    # use aiohttp

    async with aiohttp.ClientSession() as session:
        tasks = []
        url = 'https://hello.atlassian.net/rest/api/3/issue/'
        with open('Sheet 3-Table 1.csv',
                  'r', encoding='utf-8') as csvfile:
            lines = csv.reader(csvfile)
            headers = next(lines)
            # lines = csvfile.readlines()
            for line in lines:
                httpurl = url + line[6]
                if not line[1]:
                    print(line[4] + ' Not in Rev5')

        for  in range(total):
            tasks.append(asyncio.create_task(fetch(url, session)))

        original_result = await asyncio.gather(*tasks)
        for res in original_result:
            print(res)


if __name__ == "__main__":
    total = 100

    start_time = time.time()
    asyncio.run(by_aiohttp_concurrency(total))
    print("--- It took %s seconds ---" % (time.time() - start_time))
