# -*- coding: utf-8 -*-
{
    'name': "Custom Inherit",

    'summary': "Custom Inherit Modules",

    'description': """
    Custom Module for Inherit
    """,

    'author': "Yusuf Willman",
    'website': "https://www.odoo.yusufwllmn.my.id",
    'category': 'Uncategorized',
    'version': '0.1',
    
    'depends': ['base','contacts'],

    'data': [
        'security/ir.model.access.csv',
        
        'views/res_partner.xml',
        'views/pokemon.xml',
        'views/menu.xml',
    ],
    
    'installable': True, 
    'application': True,
    
    'demo': [
        'demo/demo.xml',
    ],
}
    # def write(self, vals):
    #     if 'is_company' in vals and not vals['is_company']:
    #         vals['pokemon_id'] = None
    #         vals['pokemon_name'] = None
    #         vals['ability'] = None
    #         vals['ability_info'] = None
    #     return super(ResPartner, self).write(vals)
