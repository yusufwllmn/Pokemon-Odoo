# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import random
import base64
from io import BytesIO

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    pokemon_id = fields.Many2one(
        'pokemon', 
        string = 'Pokemon ID',
        help = 'Pokémon associated with Partner',
        readonly = True,
        ondelete = 'cascade'
    )
    
    pokemon = fields.Char(
        related = 'pokemon_id.name',
        string = 'ID Pokemon',
        help = 'ID of the Pokémon associated with the company'
    ) 
    
    pokemon_name = fields.Char(
        related = 'pokemon_id.pokemon_name',
        string = 'Pokemon',
        help = 'Name of the Pokémon associated with the company'
    )
    
    ability = fields.Char(
        related = 'pokemon_id.ability',
        string = 'Ability',
        help = 'Name of the Pokémon ability'
    )
    
    ability_info = fields.Char(
        related = 'pokemon_id.ability_info',
        string = 'Ability Description',
        help = 'Description of the Pokémon ability'
    )
    
    image = fields.Binary(
        related = 'pokemon_id.image',
        string = 'Avatar',
        help = 'Avatar of The Pokémon'
    )
    
    def write(self, vals):
        if 'is_company' in vals and not vals['is_company']:
            if self.pokemon_id:
                old_pokemon = self.pokemon_id
                self.pokemon_id = None
                old_pokemon.unlink()
        return super(ResPartner, self).write(vals)
    
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
        url = f'https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}/'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            pokemon_id = data['id']
            pokemon_name = data['name']
            image_url = data['sprites']['front_default']
            response = requests.get(image_url)
            image = base64.b64encode(BytesIO(response.content).read())
            ability_url = data['abilities'][0].get('ability',{}).get('url')
            response = requests.get(ability_url)
            
            if response.status_code == 200:
                data = response.json()
                ability = data['name']
                ability_info = 'Ability has no description'
                
                for entry in data['effect_entries']:
                    if entry['language']['name'] == 'en':
                        ability_info = entry['effect']
                        break
                
                if self.pokemon_id:
                    old_pokemon = self.pokemon_id
                    self.pokemon_id = None
                    old_pokemon.unlink()
                    
                pokemon = self.env['pokemon'].create({
                    'name' : pokemon_id,
                    'pokemon_name' : pokemon_name,
                    'ability' : ability,
                    'ability_info' : ability_info,
                    'image' : image
                })

                self.pokemon_id = pokemon.id