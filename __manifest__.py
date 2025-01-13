# -*- coding: utf-8 -*-
{
    'name': "RestQuietky",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
            Long description of module's purpose
    """,
    'author': "Suradi",
    'category': 'Schedule',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base','mail'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/Break_Schedule.xml',
        'views/Menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

