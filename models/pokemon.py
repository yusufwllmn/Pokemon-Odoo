# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pokemon(models.Model):
    _name = 'pokemon'
    _description = 'Pokemon Records Associated with partner'
    
    name = fields.Char(
        string = 'Pokemon ID',
        help = 'ID of the Pokémon associated with the company'
    )
    
    pokemon_name = fields.Char(
        string = 'Pokemon',
        help = 'Name of the Pokémon catched with the company'
    )
    
    ability = fields.Char(
        string = 'Ability',
        help = 'Name of the Pokémon ability'
    )
    
    ability_info = fields.Char(
        string = 'Ability Description',
        help = 'Description of the Pokémon ability'
    )
    
    image = fields.Binary(
        string = 'Avatar',
        help = 'Avatar of The Pokémon',
    )
    
    partner_id = fields.One2many(
        'res.partner',
        'pokemon_id',
        string = 'Partner ID',
        help = 'Partner associated with Pokémon'
    )
    
    partner_name = fields.Char(
        related = 'partner_id.name',
        string = 'Partner',
        help = 'Name of the Partner associated with the Pokémon'
    )