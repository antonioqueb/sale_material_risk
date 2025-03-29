from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_hazardous_material = fields.Selection(
        selection=[
            ('yes', 'Es material peligroso'),
            ('no', 'No es material peligroso'),
        ],
        string='¿Material peligroso?',
        default='no',
        required=True,
        help='Indica si este producto es considerado un material peligroso.'
    )
