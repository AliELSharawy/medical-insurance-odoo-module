from odoo import models, fields, api

class claim_line(models.Model):
    _name = 'claim_line'
    _description = 'this is claim_line model'

    price = fields.Float()
    name = fields.Char()

    product_id = fields.Many2one('product.product')
    claim_id = fields.Many2one('claim')
