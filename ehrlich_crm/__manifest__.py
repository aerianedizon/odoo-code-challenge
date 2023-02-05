# -*- coding: utf-8 -*-
{
    'name': "Ehrlich CRM",

    'summary': """
        Custom CRM for Erhlich 24h Code Challenge
        """,

    'description': """
        Custom CRM for Erhlich 24h Code Challenge
    """,

    'author': "A. Dizon",

    'license': 'LGPL-3',

    'category': 'Sales/CRM',

    'version': '13.0.1.0.0',

    'depends': ['crm'],

    'data': [
        'data/crm_stage_data.xml',
        'views/crm_lead_view.xml',
        'views/crm_team_view.xml',
        'views/res_partner_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'installable': True,
    'application': False,
    'auto_install': False

}
