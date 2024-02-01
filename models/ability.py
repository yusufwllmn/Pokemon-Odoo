# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import random

class ability(models.Model):
    _name = 'ability'
    _description = 'ability Records from API'
    
    name = fields.Char(
        string='Ability ID',
        help='ID of the Ability'
    )
    
    ability = fields.Char(
        string='Ability',
        help='Name of the Ability'
    )
    
    ability_info = fields.Char(
        string = 'Ability Description',
        help='Description of Ability'
    )
    
    def get_ability_id(self):
        all_pokemon = self.env['pokemon'].search([])
        all_ability_id = list(set([pokemon.ability_id for pokemon in all_pokemon]))
        return all_ability_id
    
    def get_ability(self):
        all_ability_id = self.get_ability_id()
    
        for ability_ids in all_ability_id:
            url = f'https://pokeapi.co/api/v2/ability/{ability_ids}/'
            response = requests.get(url)
    
            if response.status_code == 200:
                data = response.json()
                ability_id = data['id']
                ability_name = data['name']
                ability_info = ''
    
                for entry in data['effect_entries']:
                    if entry['language']['name'] == 'en':
                        ability_info = entry['effect']
                        break
                    
                self.create({
                    'name' : ability_id,
                    'ability' :  ability_name,
                    'ability_info' : ability_info,
                })