from odoo import models, fields, api

class insurance_plan(models.Model):
    _name = 'insurance_plan'
    _description = 'this is insurance_plan model'

    name = fields.Char()

    insurance_company_id = fields.Many2one('insurance_company')
    insurance_plan_line_id = fields.One2many('insurance_plan_line', 'insurance_plan_id')