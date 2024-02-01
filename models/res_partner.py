# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import random

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    pokemon_id = fields.Many2one(
        'pokemon',
        string='Pokemon ID',
        help='ID of the Pokémon catched with the company',
        readonly=True
    )
    
    pokemon_name = fields.Char(
        related='pokemon_id.pokemon_name',
        string = 'Pokemon',
        help='Name of the Pokémon catched with the company'
    )
    
    pokemon_ability = fields.Char(
        related='pokemon_id.ability_id',
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

            return all_pokemon_id
        
    def get_random_pokemon(self):
        all_pokemon_id = self.get_all_pokemon_id()
        random_pokemon_id = int(random.choice(all_pokemon_id))
        self.pokemon_id = random_pokemon_id
        