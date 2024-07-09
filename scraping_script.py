import asyncio
import aiohttp
import ssl
from tabulate import tabulate


class ScrapiScript:

    def __init__(self, country="ukraine") -> None:
        self.country = country.lower()
        self.__url = f"https://restcountries.com/v3.1/name/{self.country}?fields=name,capital,flags"
        self.__ssl_context = ssl.create_default_context()
        self.__ssl_context.check_hostname = False
        self.__ssl_context.verify_mode = ssl.CERT_NONE

    async def __get_date(self) -> list:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.__url, ssl=self.__ssl_context) as resp:
                if resp.status != 200:
                    raise ConnectionError("Sorry, check parameters")
                return await resp.json()

    async def print_info_about_country(self) -> None:
        data = await self.__get_date()
        headers = ["Name", "Capital", "Flag(png)"]
        name_country = data[0]["name"]["common"]
        capital = data[0]["capital"][0]
        flag = data[0]["flags"]["png"]
        table = [[name_country, capital, flag]]
        print(tabulate(table, headers, tablefmt="grid"))
