from odoo import models, fields, api

class demo_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    claim_state = fields.Selection([
        ("insurance company only","insurance company only"), 
        ("insurance company  and patient","insurance company and patient")
    ], string="claim_state", config_parameter="demo.claim_state")