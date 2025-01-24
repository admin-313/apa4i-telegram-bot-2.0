import logging
import asyncio


async def main() -> None:
    logging.basicConfig(
        format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
    )


if __name__ == "__main__":
    asyncio.run(main())
