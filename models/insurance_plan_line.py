from odoo import models, fields, api

class insurance_plan_line(models.Model):
    _name = 'insurance_plan_line'
    _description = 'this is insurance_plan_line model'

    name = fields.Char()
    price = fields.Float()
    percentage = fields.Float()

    product_id = fields.Many2one('product.product')
    insurance_plan_id = fields.Many2one('insurance_plan')

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id and self.price == 0:
            self.price = self.product_id.lst_price