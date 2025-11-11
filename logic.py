import aiohttp
import random

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.power = random.randint(50, 100)

        # Eğer oyuncunun Pokémon'u yoksa oluştur, varsa yükle
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            existing = Pokemon.pokemons[pokemon_trainer]
            self.pokemon_number = existing.pokemon_number
            self.name = existing.name
            self.power = existing.power

    async def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['forms'][0]['name']
                return "Pikachu"

    async def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['sprites']['front_default']
                return None

    async def info(self):
        if not self.name:
            self.name = await self.get_name()
        return f"🎮 Pokémon'unuzun ismi: **{self.name.capitalize()}**\n⚡ Güç: {self.power}"

    async def show_img(self):
        return await self.get_img()

    async def attack(self, enemy):
        if not self.name:
            self.name = await self.get_name()
        if not enemy.name:
            enemy.name = await enemy.get_name()

        attack_value = random.randint(10, 50)
        enemy.power -= attack_value

        if enemy.power <= 0:
            enemy.power = 0
            return f"💥 {self.name.capitalize()} {enemy.name.capitalize()}’yi yendi!"
        else:
            return f"⚔️ {self.name.capitalize()} {enemy.name.capitalize()}’ye {attack_value} hasar verdi! ({enemy.power} güç kaldı.)"


class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.magic_power = random.randint(20, 40)
        self.power += self.magic_power

    async def attack(self, enemy):
        if not self.name:
            self.name = await self.get_name()
        if not enemy.name:
            enemy.name = await enemy.get_name()

        spell_damage = random.randint(30, 70)
        enemy.power -= spell_damage

        if enemy.power <= 0:
            enemy.power = 0
            return f"🧙‍♂️ {self.name.capitalize()} büyüyle {enemy.name.capitalize()}’yi yendi!"
        else:
            return f"✨ {self.name.capitalize()} {enemy.name.capitalize()}’ye {spell_damage} büyü hasarı verdi! ({enemy.power} güç kaldı.)"


class Fighter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.strength = random.randint(20, 50)
        self.power += self.strength

    async def attack(self, enemy):
        if not self.name:
            self.name = await self.get_name()
        if not enemy.name:
            enemy.name = await enemy.get_name()

        hit = random.randint(20, 60)
        enemy.power -= hit

        if enemy.power <= 0:
            enemy.power = 0
            return f"🥊 {self.name.capitalize()} {enemy.name.capitalize()}’yi nakavt etti!"
        else:
            return f"💪 {self.name.capitalize()} {enemy.name.capitalize()}’ye {hit} hasar verdi! ({enemy.power} güç kaldı.)"
