# -*- coding: utf-8 -*-
{
    'name': "Purchase Order",
    'version': '0.1',
    'summary': 'Purchase Order Management',
    'sequence': 6,
    'description': """
Odoo Module
===========
Specifically Designed for Etisalat-TBPC

Purchase Order Management
---------------------
- Purchase Order
    """,
    'author': "Marc Philippe de Villeres",
    'website': "https://github.com/mpdevilleres",
    'category': 'TBPC Budget',
    'depends': ['document',
                'budget_contractor',
                'budget_capex',
                'budget_opex'],
    'data': [
        'security/budget_purchase_order.xml',
        'security/ir.model.access.csv',

        'views/purchase_order.xml',
        # 'views/cear_inherit.xml',
        'views/menu.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
