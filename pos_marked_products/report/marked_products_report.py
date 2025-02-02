from odoo import api, fields, models, tools

class MarkedProductsReport(models.Model):
    _name = 'report.marked.products'
    _description = 'Marked Products Sales Report'
    _auto = False
    _order = 'date desc'

    product_id = fields.Many2one('product.product', string='Product', readonly=True)
    quantity = fields.Float(string='Quantity', readonly=True)
    date = fields.Date(string='Date', readonly=True)
    session_id = fields.Many2one('pos.session', string='Session', readonly=True)
    config_id = fields.Many2one('pos.config', string='POS Branch', readonly=True)
    amount_total = fields.Float(string='Total Amount', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT
                    row_number() OVER () AS id,
                    l.product_id AS product_id,
                    s.config_id AS config_id,
                    sum(l.qty) AS quantity,
                    sum(l.price_subtotal_incl) as amount_total,
                    date_trunc('day', o.date_order)::date AS date,
                    o.session_id AS session_id
                FROM pos_order_line l
                JOIN pos_order o ON (l.order_id=o.id)
                JOIN pos_session s ON (o.session_id=s.id)
                JOIN product_product p ON (l.product_id=p.id)
                JOIN product_template t ON (p.product_tmpl_id=t.id)
                WHERE t.is_marked = true
                GROUP BY 
                    l.product_id,
                    s.config_id,
                    date_trunc('day', o.date_order)::date,
                    o.session_id
                ORDER BY date_trunc('day', o.date_order)::date DESC
            )
        """ % self._table)