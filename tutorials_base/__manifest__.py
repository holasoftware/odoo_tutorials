# -*- coding: utf-8 -*-
{
    'name': "Tutorials base",
    'author': "Miguel Martinez Lopez",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'tutorials_base/static/src/tutorials_dashboard.js',
            'tutorials_base/static/src/tutorials_dashboard.xml'
        ]
    },
    "installable": True,
    'application': False,
    "license": "AGPL-3"
}

