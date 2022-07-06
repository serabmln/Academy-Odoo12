from odoo import models, fields, api

class NamaModel(models.Model):
    _inherit = 'sale.order'

    sale_description = fields.Char(string="Sale Description")

