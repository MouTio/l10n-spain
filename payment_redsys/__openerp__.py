# -*- coding: utf-8 -*-

{
    'name': 'Redsys Payment Acquirer',
    'category': 'Hidden',
    'summary': 'Payment Acquirer: Redsys Implementation',
    'version': '9.0.1.0.0',
    'author': "Tecnativa,"
              "Odoo Community Association (OCA)",
    'depends': ['payment', 'website_sale'],
    "external_dependencies": {
        "python": [
            "Crypto.Cipher.DES3",
        ],
        "bin": [],
    },
    'data': [
        'views/redsys.xml',
        'views/payment_acquirer.xml',
        'data/payment_redsys.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
}
