# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import random

class pokemon(models.Model):
    _name = 'pokemon'
    _description = 'Pokemon Records from API'
    
    pokemon_id = fields.Integer(
        string='Pokemon ID',
        help='ID of the Pokémon associated with the company'
    )
    
    name = fields.Char(
        string='pokemon Name',
        help='Name of the Pokémon associated with the company'
    )
    
    abilities = fields.Char(
        string='Pokemon Abilities',
        help='Abilities of the Pokémon associated with the company'
    )
    
    abilities_desc = fields.Char(
        string='Pokemon Abilities',
        help='Abilities of the Pokémon associated with the company'
    )
    
    def get_pokemon(self):
        url = 'https://pokeapi.co/api/v2/pokemon'
        headers = {
                'Content-type': 'application/json'
            }
        response = requests.get(url, headers=headers)
        data = response.json()
        
        pokemon_count = int(data.get('count'))
        random_pokemon_id = random.randint(1, pokemon_count)
        
        for result in data.get('results', []):
            name = result.get('name')
            pokemon_id = int(result.get('url').split('/')[-2])
            
            detail_url = result.get('url')
            detail_response = requests.get(detail_url, headers=headers)
            detail_data = detail_response.json()
            
            ability_data = detail_data.get('abilities', [{}])[0].get('ability', {})
            ability_name = ability_data.get('name')
            
            ability_url = ability_data.get('url')
            ability_response = requests.get(ability_url, headers=headers)
            ability_detail = ability_response.json()
            ability_desc = ability_detail.get('effect_entries', [{}])[0].get('effect')
            
            self.create({
                'name': name,
                'pokemon_id': pokemon_id,
                'abilities': ability_name,
                'abilities_desc': ability_desc
            })