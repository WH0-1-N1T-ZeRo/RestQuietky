# -*- coding: utf-8 -*-
{
    'name': "RestQuietky",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
            Long description of module's purpose
    """,
    # Creator
    'author': "Suradi",
    'category': 'Schedule',
    'version': '0.1',
    #Add new Depends mail
    'depends': ['base','mail'],
    #Configuration file data
    'data': [
        'security/ir.model.access.csv',
        'views/Break_Schedule.xml',
        'views/Menu.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

