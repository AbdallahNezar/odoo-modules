{
    'name': 'POS Marked Products',
    'version': '16.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Mark special products in POS',
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'report/marked_products_report_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_marked_products/static/src/css/pos.css',
            'pos_marked_products/static/src/js/models.js',
            'pos_marked_products/static/src/js/ProductItem.js',
            'pos_marked_products/static/src/xml/product_item.xml',
        ],
    },
    'pos_fields': {
        'product.product': ['is_marked'],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}