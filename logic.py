import aiohttp
import random

class Pokemon:
    pokemons = {}  # {trainer_name: [Pokemon1, Pokemon2, ...]}
    battle_history = {}  # {trainer_name: [str, ...]}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.power = random.randint(50, 100)
        self.health = random.randint(100, 500)

        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = [self]
        else:
            Pokemon.pokemons[pokemon_trainer].append(self)

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
        return f"🎮 Pokémon'unuzun ismi: **{self.name.capitalize()}**\n⚡ Güç: {self.power}\n❤️ Can: {self.health}"

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
            result_text = f"💥 {self.name.capitalize()} {enemy.name.capitalize()}’yi yendi!"
        else:
            result_text = f"⚔️ {self.name.capitalize()} {enemy.name.capitalize()}’ye {attack_value} hasar verdi! ({enemy.power} güç kaldı.)"

        Pokemon.add_battle_history(self.pokemon_trainer, result_text)
        Pokemon.add_battle_history(enemy.pokemon_trainer, result_text)
        return result_text

    @classmethod
    def add_battle_history(cls, trainer, text):
        if trainer not in cls.battle_history:
            cls.battle_history[trainer] = []
        cls.battle_history[trainer].append(text)

    @classmethod
    def get_history(cls, trainer):
        return cls.battle_history.get(trainer, [])

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
            result_text = f"🧙‍♂️ {self.name.capitalize()} büyüyle {enemy.name.capitalize()}’yi yendi!"
        else:
            result_text = f"✨ {self.name.capitalize()} {enemy.name.capitalize()}’ye {spell_damage} büyü hasarı verdi! ({enemy.power} güç kaldı.)"

        Pokemon.add_battle_history(self.pokemon_trainer, result_text)
        Pokemon.add_battle_history(enemy.pokemon_trainer, result_text)
        return result_text

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
            result_text = f"🥊 {self.name.capitalize()} {enemy.name.capitalize()}’yi nakavt etti!"
        else:
            result_text = f"💪 {self.name.capitalize()} {enemy.name.capitalize()}’ye {hit} hasar verdi! ({enemy.power} güç kaldı.)"

        Pokemon.add_battle_history(self.pokemon_trainer, result_text)
        Pokemon.add_battle_history(enemy.pokemon_trainer, result_text)
        return result_text
