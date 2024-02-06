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
        readonly=True,
        ondelete='set null'
    )
    
    pokemon_name = fields.Char(
        related='pokemon_id.pokemon_name',
        string = 'Pokemon',
        help='Name of the Pokémon catched with the company'
    )
    
    ability_id = fields.Many2one(
        'ability',
        string='Ability ID',
        help='ID of the Pokémon ability catched with the company',
        readonly=True,
        ondelete='set null'
    )
    
    pokemon_ability = fields.Char(
        related='ability_id.ability',
        string = 'Ability',
        help='Name of the Pokémon ability'
    )
    
    ability_desc = fields.Char(
        related='ability_id.ability_info',
        string = 'Ability Description',
        help='Description of the Pokémon ability'
    )
    
    def write(self, vals):
        if 'is_company' in vals and not vals['is_company']:
            vals['pokemon_id'] = None
            vals['ability_id'] = None
        return super(ResPartner, self).write(vals)
    
    def get_all_pokemon_id(self):
        all_pokemon = self.env['pokemon'].search([])
        all_pokemon_id = list([pokemon.name for pokemon in all_pokemon])
        return all_pokemon_id
        
    def get_random_pokemon(self):
        all_pokemon_id = self.get_all_pokemon_id()
        random_pokemon_id = int(random.choice(all_pokemon_id))
        pokemon = self.env['pokemon'].search([('id', '=', random_pokemon_id)], limit=1)
        if pokemon:
            self.pokemon_id = pokemon.id
            ability = self.env['ability'].search([('id', '=', int(pokemon.ability_id))], limit=1)
            if ability:
                self.ability_id = ability
        