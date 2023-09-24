# pokedex
LIB EXTERNE AUTHORISE: requests

(cf https://requests.readthedocs.io/en/latest/)
Ici, nous allons plus nous interessé à l'utilisation d'API externes.
Pour ce faire, nous allons coder un petit wrapper sur l'api de pokemon.
Mais qu'est ce qu'un wrapper ? Dans l'usage courant c'est essentiellement une librairie qui permet de manipuler une API en faisant abstraction des appels sur l'api.
On oublie pas les codes http, les raise_for_status etc etc etc.

## PokeFinder
PokeFinder est une classe.
Elle prend rien a l'instanciation

Elle implementera:
### get_pokemon_by_name
`def get_pokemon_by_name(name: str) -> Pokemon`
get_pokemon_by_name fera un call a l'endpoint `GET https://pokeapi.co/api/v2/pokemon/{id or name}/`

et retournera une instance de la class Pokemon (cf ci dessous).

### get_pokemon_by_id
La même chose mais avec l'id cette fois.

### get_pokemons_by_ids / get_pokemons_by_names
Qui prendront respectivement une liste d'int et une liste de str, et qui retournera une liste de Pokemon.
A toi de voir comment tu veux gerer les erreurs (si un id existe pas ou une str).

## Pokemon
Pokemon est une class qui représente un pokemon.
Il aura les variables d'instance suivantes:
- id
- name
- base_experience
- height
- is_default
- order
- weight
Tu remarquera une similitude avec la réponse de l'API ........
Pour les methodes suivantes, tu aura peut-être besoin de rajouter des champs (c'est un vrai peut-être, j'ai juste pas verifié)

Elle implementera les methodes suivantes:
### get_stats
`def get_stats(self) -> dict[str, Any]`

Retourne un dictionnaire contenant les stats du personnages.
Je te laisse lire la doc, chercher par toi même.

### download_sprites
`def get_sprites(self)`

Enregistre les sprites dans un dossier /sprites/{pokemon id} si (et uniquement si) elles n'ont pas été encore enregistré.