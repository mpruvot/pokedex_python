import requests
import json
import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Pokemon:
    def __init__(self, id, name, base_experience, height, is_default, order, weight, stats, sprites):
        self.id = id
        self.name = name
        self.base_experience = base_experience
        self.height = height
        self. is_default = is_default
        self.order = order
        self.weight = weight
        self.stats = stats
        self.sprites = sprites
        
    def get_stats(self) -> dict:
        pass

    
    def get_sprites(self):
        try:
            with open(f"sprites/{self.name}.png", 'xb') as f:
                response = requests.get(self.sprites['front_default'])
                response.raise_for_status()
                f.write(response.content)
                logging.info(f'Success: {self.name} sprites Added !')
        except FileExistsError:
            logging.exception(f"Le fichier sprites/{self.name}.png existe déjà.")
        except requests.exceptions.HTTPError as err:
            logging.exception(err)
            raise
            
class Pokefinder:
    def __init__(self) -> None:
        pass

    def get_pokemon_by_name(self, name: str) -> Pokemon:
        try:
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}/')
            response.raise_for_status()
            r = response.json()
            logging.info(f'class Pokemon: {name} succefully created !')
            return Pokemon(r['id'], r['name'], r['base_experience'], r['height'], r['is_default'], r['order'], r['weight'], r['stats'], r['sprites'])
        except requests.exceptions.HTTPError as err:
            logging.exception(f'NAME: {name} not found !')
            raise        
            
            
    def get_pokemon_by_id(self, id: str) -> Pokemon:
        try:
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
            response.raise_for_status()
            r = response.json()
            logging.info(f'class Pokemon: {id} succefully created !')
            return Pokemon(r['id'], r['name'], r['base_experience'], r['height'], r['is_default'], r['order'], r['weight'], r['stats'], r['sprites'])
        except requests.exceptions.HTTPError as err:
            logging.exception(f'ID: {id} not found !')
            raise
        
new_poke = Pokefinder()

test = new_poke.get_pokemon_by_id(139)


test.get_sprites()