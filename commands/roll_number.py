from commands.base_command import BaseCommand

class Roll(BaseCommand):
    def __init__(self):
        description = "Generates a random number between two given numbers"
        params = ["lower", "upper"]
        super().__init__(description, params)

    async def handle(self,params,message,client):
        lower_bound = int(params[0])
        upper_bound = int(params[1])
        rolled = randint(lower_bound, upper_bound)

        msg = f"{message.author.mention}, you rolled a {rolled}!" #f string literal
        await client.send_message(message.channel, msg)
