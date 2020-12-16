import asyncio
import aiohttp
import json


async def request_data(url):
    async with aiohttp.request('GET', url) as resp:
        assert resp.status == 200
        return await resp.text()


async def get_reddit_top(subreddit):
    data = await request_data(f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5')
    print(f'\n/r/{subreddit}:')

    json_data = json.loads(data)
    for j in json_data['data']['children']:
        post_title = j['data']['title']
        score = j['data']['score']
        link = j['data']['url']
        print(f'\t {score}: {post_title} \n {link}')


async def main():
    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    await asyncio.gather(*(get_reddit_top(q) for q in reddits))


asyncio.run(main())
