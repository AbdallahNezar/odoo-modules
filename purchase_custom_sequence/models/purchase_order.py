from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sequence_type = fields.Selection([
        ('default', 'Default Sequence (P)'),
        ('special', 'Special Sequence')
    ], string='Sequence Type', default='default', required=True)

    @api.model
    def create(self, vals):
        if vals.get('sequence_type') == 'special':
            if vals.get('name', '/') == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('special.purchase.sequence')
        return super(PurchaseOrder, self).create(vals)