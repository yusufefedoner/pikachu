import discord
from discord.ext import commands
import random
from config import token
from logic import Pokemon, Wizard, Fighter

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Giriş yapıldı: {bot.user.name}')

# ---------------- !go ----------------
@bot.command()
async def go(ctx, tür: str = None):
    author = ctx.author.name
    if author in Pokemon.pokemons and len(Pokemon.pokemons[author]) >= 3:
        await ctx.send("⚠️ Maksimum 3 Pokémon alabilirsin!")
        return

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

# ---------------- !attack ----------------
@bot.command()
async def attack(ctx):
    target = ctx.message.mentions[0] if ctx.message.mentions else None
    if not target:
        await ctx.send("⚔️ Saldırmak istediğin kullanıcıyı etiketle: örnek `!attack @Kullanıcı`")
        return
    if target.name not in Pokemon.pokemons or ctx.author.name not in Pokemon.pokemons:
        await ctx.send("👀 Her iki tarafın da Pokémon sahibi olması gerekiyor!")
        return

    # En güçlü Pokémon'u seç
    attacker = max(Pokemon.pokemons[ctx.author.name], key=lambda x: x.power)
    enemy = max(Pokemon.pokemons[target.name], key=lambda x: x.power)

    result = await attacker.attack(enemy)
    await ctx.send(result)

# ---------------- !heal ----------------
@bot.command()
async def heal(ctx):
    author = ctx.author.name
    if author in Pokemon.pokemons:
        for pok in Pokemon.pokemons[author]:
            heal_amount = random.randint(20, 50)
            pok.power += heal_amount
        await ctx.send(f"💖 Pokémon'larınız iyileşti!")
    else:
        await ctx.send("🩹 Önce bir Pokémon oluşturmalısınız! `!go` komutunu kullanın.")

# ---------------- !info ----------------
@bot.command()
async def info(ctx):
    author = ctx.author.name
    if author not in Pokemon.pokemons:
        await ctx.send("⚠️ Önce bir Pokémon oluşturmalısınız! `!go` komutunu kullanın.")
        return

    info_text = ""
    for pok in Pokemon.pokemons[author]:
        info_text += await pok.info() + "\n\n"
    await ctx.send(f"ℹ️ @{author} Pokémon bilgileri:\n{info_text}")

# ---------------- !history ----------------
@bot.command()
async def history(ctx):
    author = ctx.author.name
    history_list = Pokemon.get_history(author)
    if not history_list:
        await ctx.send("📭 Henüz hiç savaş geçmişin yok!")
        return
    formatted = "\n".join([f"{i+1}. {item}" for i, item in enumerate(history_list[-10:])])
    await ctx.send(f"📜 **Son savaşların:**\n{formatted}")

# ---------------- !leaderboard ----------------
@bot.command()
async def leaderboard(ctx):
    if not Pokemon.pokemons:
        await ctx.send("📭 Henüz kimsenin Pokémon'u yok!")
        return

    # Tüm Pokémon'ları tek listede sırala
    all_pokemons = []
    for trainer, pok_list in Pokemon.pokemons.items():
        for pok in pok_list:
            all_pokemons.append((trainer, pok))

    sorted_pokemons = sorted(all_pokemons, key=lambda x: x[1].power, reverse=True)

    leaderboard_text = ""
    for i, (trainer, pok) in enumerate(sorted_pokemons[:10], start=1):
        name = pok.name.capitalize() if pok.name else "Bilinmiyor"
        leaderboard_text += f"{i}. 🏅 {trainer} - {name} ⚡ {pok.power} güç\n"

    embed = discord.Embed(
        title="🏆 Pokémon Liderlik Tablosu",
        description=leaderboard_text,
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed)

# ---------------- BOTU ÇALIŞTIR ----------------
bot.run(token)
