from discord.ext import tasks
import discord
import datetime
from scraper import get_current_price

CHANNEL_ID = 000000000000000000
TOKEN = '<Insert your token here>'
URL = "https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=JSW"
SEND_HOUR, SEND_MINUTE = 12, 00

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_background_task.start()

    async def on_ready(self):
        print(self.user.name)
        print(self.user.id)

    @tasks.loop(seconds=60)
    async def my_background_task(self):
        now = datetime.datetime.now()
        hour, minute = now.hour, now.minute
        if hour == SEND_HOUR and minute == SEND_MINUTE:
            channel = self.get_channel(CHANNEL_ID)
            price = get_current_price(URL)
            if price is not None:
                message = f"Today's JSW price: {price}"
                await channel.send(message)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()


bot = MyClient()
bot.run(TOKEN)
