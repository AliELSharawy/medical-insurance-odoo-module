from odoo import models, fields, api

class insurance_company(models.Model):
    _name = 'insurance_company'
    _description = 'this is insurance_company model'
    _inherits = {'res.partner' : 'partner_id'}
    partner_id = fields.Many2one('res.partner')

    # name = fields.Char()
    insurance_plan_id = fields.One2many('insurance_plan', 'insurance_company_id')
    claim_id = fields.One2many('claim', 'insurance_company_id')
    patient_id = fields.One2many('patient','insurance_company_id')
    visit_id = fields.One2many('visit','insurance_company_id')

