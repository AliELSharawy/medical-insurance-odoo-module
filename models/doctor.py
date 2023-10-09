from odoo import models, fields, api

class doctor(models.Model):
    _name = 'doctor'
    _description = 'this is doctor model'
    _inherits = {'res.partner' : 'partner_id'}
    partner_id = fields.Many2one('res.partner')

    # name = fields.Char()
    visit_id = fields.One2many('visit', 'doctor_id')
    claim_id = fields.One2many('claim', 'doctor_id')

