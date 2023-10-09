from odoo import models, fields, api

class visit_line(models.Model):
    _name = 'visit_line'
    _description = 'this is visit_line model'

    name = fields.Char()

    currency_id = fields.Many2one('res.currency')
    patient_share = fields.Monetary('Retail Price')
    insurance_company_share = fields.Monetary('Retail Price')
    
    product_id = fields.Many2one('product.product')
    visit_id = fields.Many2one('visit')
