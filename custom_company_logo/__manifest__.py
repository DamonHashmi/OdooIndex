{
    'name': 'Custom Company Logo',
    'version': 'For All',
    'summary': '',
    'description': '',
    'category': 'Extra Tools',
    'author': 'Junaid Shah',
    'website': 'www.odooindex.com',
    'depends': ['base', 'web', 'account'],
    'data': [
        'views/external_layout.xml',
        'views/res_company_view.xml',
        'views/invoice_inherit.xml',
    ],
    'installable': True,
    'auto_install': False,
}
