import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class Player:
    def __init__(self, name, health, attack_power, defense_ratio):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_ratio = defense_ratio
        self.is_defeated = False

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        damage_after_defense = damage * (1 - target.defense_ratio)
        target.take_damage(damage_after_defense)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_defeated = True

class BattleSystem:
    def __init__(self):
        self.players = []
        self.current_turn = 0

    def add_player(self, player):
        self.players.append(player)

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def attack(self, attacker, target):
        damage = max(0, attacker.attack_power - target.defense_ratio)
        target.take_damage(damage)

    def commence(self):
        battle_log = []

        battle_log.append("The battle begins!")

        while len([p for p in self.players if not p.is_defeated]) > 1:
            attacker = self.players[self.current_turn]
            defenders = [p for p in self.players if p != attacker and not p.is_defeated]

            if defenders:
                defender = random.choice(defenders)

                battle_log.append(f"{attacker.name} attacks {defender.name}!")

                self.attack(attacker, defender)

                if defender.is_defeated:
                    battle_log.append(f"{defender.name} is defeated and leaves the battle.")
            else:
                battle_log.append(f"{attacker.name} has no valid targets and skips their turn.")

            self.next_turn()

        winner = next(p for p in self.players if not p.is_defeated)
        battle_log.append(f"{winner.name} emerges victorious!")

        return battle_log

    def summon_player(self, name, health, attack_power, defense_ratio):
        player = Player(name, health, attack_power, defense_ratio)
        self.players.append(player)
        return f"{name} has been summoned with {health} health, {attack_power} attack power, and a defense ratio of {defense_ratio:.2f}!"

battle_system = BattleSystem()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def summon_player(ctx, name, health, attack_power, defense_ratio):
    message = battle_system.summon_player(name, int(health), int(attack_power), float(defense_ratio))
    await ctx.send(message)

@bot.command()
async def commence(ctx):
    battle_log = battle_system.commence()
    for line in battle_log:
        await ctx.send(line)

@bot.command()
async def ping_and_start_battle(ctx):
    await ctx.send(f"{ctx.author.mention}, ping received! Starting B.A.L.R.O.G B.A.T.T.L.E S.Y.S.T.E.M.")
    battle_log = battle_system.commence()
    for line in battle_log:
        await ctx.send(line)

# Run the bot
bot.run('MTE1MzAxNDY4NzI2MTI4MjM5NA.GGT1dR.9Gax1k6czm4CZJLfObQmEGWJzTQ4BMTq8TJ7Y8')
