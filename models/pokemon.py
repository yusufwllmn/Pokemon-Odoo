# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class pokemon(models.Model):
    _name = 'pokemon'
    _description = 'Pokemon Records from API'
    
    name = fields.Char(
        string='Pokemon ID',
        help='ID of the Pokémon associated with the company'
    )
    
    pokemon_name = fields.Char(
        string='Pokemon Name',
        help='Name of the Pokémon associated with the company'
    )
    
    def get_pokemon(self):
        url = 'https://pokeapi.co/api/v2/pokemon?limit=10000'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
        
            for result in data.get('results', []):
                pokemon_id = int(result.get('url').split('/')[-2])
                name = result.get('name')
                
                self.create({
                    'name': pokemon_id,
                    'pokemon_name': name,
                })