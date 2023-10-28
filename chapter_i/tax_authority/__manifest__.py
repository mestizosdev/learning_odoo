# -*- coding: utf-8 -*-
{
    'name': "Tax Authority",

    'summary': """Tax Authority resources""",

    'description': """Manage tax authority resources""",

    'author': "Jorge Luis",
    'website': "https://mestizos.dev",

    'category': 'Accounting/Accounting',
    'version': '0.1',
    'license': 'LGPL-3',

    'depends': ['base', 'account', 'l10n_ec'],

    'data': [
        'security/ir.model.access.csv',
        'views/dashboard.xml',
        'views/payment_method.xml',
        'views/sign_certificate.xml',
        'views/tax_authority_menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
