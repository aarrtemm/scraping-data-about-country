import asyncio

from scraping_script import ScrapiScript


if __name__ == '__main__':
    ukraine = ScrapiScript("usa")
    asyncio.run(ukraine.print_info_about_country())
