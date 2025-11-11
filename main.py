import discord
from discord.ext import commands
import random
from config import token
from logic import Pokemon, Wizard, Fighter

# Bot için gerekli izinleri (intents) ayarla
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

# Komut öneki ve izinlerle botu oluştur
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot çalıştığında tetiklenen olay
@bot.event
async def on_ready():
    print(f'✅ Giriş yapıldı: {bot.user.name}')

# ------------------ !go KOMUTU ------------------
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Komutu yazan kullanıcının adını al
    if author not in Pokemon.pokemons:
        chance = random.randint(1, 5)  # Süper güç şansını azalt (1–5)
        if chance == 1:
            pokemon = Wizard(author)
            await ctx.send("🧙‍♂️ Sihirbaz Pokémon elde ettin!")
        elif chance == 2:
            pokemon = Fighter(author)
            await ctx.send("🥊 Dövüşçü Pokémon elde ettin!")
        else:
            pokemon = Pokemon(author)
            await ctx.send("🐾 Normal Pokémon elde ettin!")

        await ctx.send(await pokemon.info())

        image_url = await pokemon.show_img()
        if image_url:
            embed = discord.Embed()
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("⚠️ Pokémon görüntüsü yüklenemedi.")
    else:
        await ctx.send("Zaten bir Pokémon oluşturmuşsun!")

# ------------------ !attack KOMUTU ------------------
@bot.command()
async def attack(ctx):
    target = ctx.message.mentions[0] if ctx.message.mentions else None  # Etiketlenen kullanıcıyı al
    if not target:
        await ctx.send("⚔️ Saldırmak istediğin kullanıcıyı etiketle: örnek `!attack @Kullanıcı`")
        return

    if target.name not in Pokemon.pokemons or ctx.author.name not in Pokemon.pokemons:
        await ctx.send("👀 Her iki tarafın da Pokémon sahibi olması gerekiyor!")
        return

    attacker = Pokemon.pokemons[ctx.author.name]
    enemy = Pokemon.pokemons[target.name]

    result = await attacker.attack(enemy)
    await ctx.send(result)

# ------------------ !heal KOMUTU ------------------
@bot.command()
async def heal(ctx):
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[author]
        pokemon.power = random.randint(50, 100)
        await ctx.send(f"💖 Pokémon'unuz yeniden güçlendi! Yeni güç: {pokemon.power}")
    else:
        await ctx.send("🩹 Önce bir Pokémon oluşturmalısınız! `!go` komutunu kullanın.")

# ------------------ BOTU ÇALIŞTIR ------------------
bot.run(token)
