from odoo import models, fields, api

class patient(models.Model):
    _name = 'patient'
    _description = 'this is patient model'
    _inherits = {'res.partner' : 'partner_id'}
    partner_id = fields.Many2one('res.partner')

    # name = fields.Char()
    # doctor_id = fields.Many2one('doctor')
    visit_id = fields.One2many('visit', 'patient_id')
    claim_id = fields.One2many('claim', 'patient_id')
    insurance_company_id = fields.Many2one('insurance_company')