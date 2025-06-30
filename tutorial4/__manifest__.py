# -*- coding: utf-8 -*-
{
    'name': "Tutorial custom admin page",
    'summary': "Demo of custom admin page",
    'author': "Miguel Martinez Lopez",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'tutorials_base'],
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'tutorial4/static/src/my_component.js',
            'tutorial4/static/src/my_component.xml'
        ]
    },
    "installable": True,
    'application': True,
    "license": "AGPL-3"
}