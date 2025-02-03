{
    'name': 'Purchase Custom Sequence',
    'version': '16.0.1.0.0',
    'category': 'Purchase',
    'summary': 'Add custom sequence selection for purchase orders',
    'description': """
        This module allows users to choose between different sequences when creating purchase orders.
    """,
    'depends': ['purchase'],
    'data': [
        'data/sequence_data.xml',
        'views/purchase_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
