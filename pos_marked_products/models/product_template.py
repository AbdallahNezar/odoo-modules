from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_marked = fields.Boolean(
        string='Marked in POS',
        help='If checked, this product will be highlighted in POS'
    )
