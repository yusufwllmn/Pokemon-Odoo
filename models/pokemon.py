# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import random

class pokemon(models.Model):
    _name = 'pokemon'
    _description = 'Pokemon Records from API'
    
    name = fields.Char(
        string='Pokemon ID',
        help='ID of the Pokémon associated with the company'
    )
    
    pokemon_name = fields.Char(
        string='Pokemon',
        help='Name of the Pokémon associated with the company'
    )
    
    ability_id = fields.Char(
        string = 'Ability',
        help='Name of the Pokémon ability'
    )
    
    
    def get_random_pokemon_id(self):
        url = 'https://pokeapi.co/api/v2/pokemon?limit=10000'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            all_pokemon_id = []

            for pokemon in data['results']:
                pokemon_url = pokemon['url']
                pokemon_id = pokemon_url.split('/')[-2]
                all_pokemon_id.append(int(pokemon_id))

            random_pokemon_id = random.sample(all_pokemon_id, 200)
            return random_pokemon_id
    
    def get_pokemon(self):
        all_pokemon_id = self.get_random_pokemon_id()

        for pokemon_ids in all_pokemon_id:
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_ids}/'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                pokemon_id = data['id']
                pokemon_name = data['name']
                ability_url = data['abilities'][0].get('ability',{}).get('url')
                ability_id = ability_url.split('/')[-2]

                self.create({
                    'name' : pokemon_id,
                    'pokemon_name' :  pokemon_name,
                    'ability_id' : ability_id,
                })