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
    ],
    
    'application': True,
    
    'demo': [
        'demo/demo.xml',
    ],
}
