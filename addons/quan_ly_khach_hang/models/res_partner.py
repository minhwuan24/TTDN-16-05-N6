from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    van_ban_di_ids = fields.One2many(
        'qlvn.van_ban_di',
        'customer_id',
        string='Văn bản của khách hàng'
    )
