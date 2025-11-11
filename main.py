import discord
from discord.ext import commands
import random
from config import token
from logic import Pokemon, Wizard, Fighter

# ------------------ BOT AYARLARI ------------------
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)


# ------------------ BOT BAŞLANGICI ------------------
@bot.event
async def on_ready():
    print(f'✅ Giriş yapıldı: {bot.user.name}')


# ------------------ !go KOMUTU ------------------
@bot.command()
async def go(ctx, tür: str = None):
    """Yeni bir Pokémon oluşturur (wizard, fighter veya normal)."""
    author = ctx.author.name

    if author in Pokemon.pokemons:
        await ctx.send("⚠️ Zaten bir Pokémon oluşturmuşsun!")
        return

    # Tür seçimi
    if tür == "wizard":
        pokemon = Wizard(author)
        await ctx.send("🧙‍♂️ Sihirbaz Pokémon elde ettin!")
    elif tür == "fighter":
        pokemon = Fighter(author)
        await ctx.send("🥊 Dövüşçü Pokémon elde ettin!")
    else:
        pokemon = Pokemon(author)
        await ctx.send("🐾 Normal Pokémon elde ettin!")

    info_text = await pokemon.info()
    await ctx.send(info_text)

    image_url = await pokemon.show_img()
    if image_url:
        embed = discord.Embed(title=pokemon.name.capitalize())
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("⚠️ Pokémon görüntüsü yüklenemedi.")


# ------------------ !attack KOMUTU ------------------
@bot.command()
async def attack(ctx):
    """Etiketlenen kullanıcıya saldırı başlatır."""
    target = ctx.message.mentions[0] if ctx.message.mentions else None

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
    """Pokémon'un gücünü yeniler."""
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[author]
        heal_amount = random.randint(20, 50)
        pokemon.power += heal_amount
        await ctx.send(f"💖 Pokémon'unuz iyileşti! Yeni güç: {pokemon.power}")
    else:
        await ctx.send("🩹 Önce bir Pokémon oluşturmalısınız! `!go` komutunu kullanın.")


# ------------------ !info KOMUTU ------------------
@bot.command()
async def info(ctx):
    """Kullanıcının Pokémon'u hakkında bilgi verir."""
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pok = Pokemon.pokemons[author]
        info_text = await pok.info()
        await ctx.send(f"ℹ️ @{author} Pokémon bilgileri:\n{info_text}")
    else:
        await ctx.send("⚠️ Önce bir Pokémon oluşturmalısınız! `!go` komutunu kullanın.")


# ------------------ BOTU ÇALIŞTIR ------------------
bot.run(token)
