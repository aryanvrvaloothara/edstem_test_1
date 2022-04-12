import asyncio
import webbrowser

common_urls = [
    'https://www.edstem.com/',
    'https://www.edstem.com/contact-us/',
    'https://www.edstem.com/approach',
    # 'https://www.edstem.com/blogs',
    # 'https://www.edstem.com/',
]

services_urls = [
    'https://www.edstem.com/services/cloud-native',
    'https://www.edstem.com/services/custom-software',
    'https://www.edstem.com/services/mobile-apps'
]


async def open_tab():
    for url in common_urls:
        print("Common page")
        webbrowser.open(url)
        await asyncio.sleep(5)


async def services_open_tab():
    for services_url in services_urls:
        print("Service page")
        webbrowser.open(services_url)
        await asyncio.sleep(5)


async def main():
    await asyncio.gather(open_tab(), services_open_tab())

asyncio.run(main())