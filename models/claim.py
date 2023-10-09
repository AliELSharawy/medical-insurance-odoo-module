from odoo import models, fields, api

class claim(models.Model):
    _name = 'claim'
    _description = 'this is claim model'

    name = fields.Char()
    state = fields.Selection([
        ("insurance company only","insurance company only"), 
        ("insurance company  and patient","insurance company and patient")
    ])

    insurance_company_id = fields.Many2one('insurance_company')
    doctor_id = fields.Many2one('doctor')
    patient_id = fields.Many2one('patient')
    claim_line_id = fields.One2many('claim_line', 'claim_id')
