import asyncio

from scraping_script import ScrapiScript


def main() -> None:
    country = str(input("Enter country: "))
    if country.isdigit():
        raise ValueError("Please, enter a country name correctly")
    scr = ScrapiScript(country=country)
    asyncio.run(scr.print_info_about_country())


if __name__ == '__main__':
    main()
