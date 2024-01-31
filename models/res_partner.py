# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import random

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    pokemon_id = fields.Many2one(
        'pokemon',
        string='Pokemon',
        help='The Pokémon catched by Company',
        readonly=True
    )
    
    pokemon_name = fields.Char(
        related='pokemon_id.pokemon_name',
        string = 'Pokemon Name',
        help=' Pokémon catched by Company'
    )
    
    def get_all_pokemon_id(self):
        url = 'https://pokeapi.co/api/v2/pokemon?limit=10000'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            all_pokemon_id = []

            for pokemon in data['results']:
                pokemon_url = pokemon['url']
                pokemon_id = pokemon_url.split('/')[-2]
                all_pokemon_id.append(int(pokemon_id))

            return all_pokemon_id
        
    def get_random_pokemon(self):
        all_pokemon_id = self.get_all_pokemon_id()
        random_pokemon_id = int(random.choice(all_pokemon_id))
        self.pokemon_id = random_pokemon_id
        