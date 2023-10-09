from odoo import models, fields, api

class visit(models.Model):
    _name = 'visit'
    _description = 'this is visit model'
    _rec_name = 'id'

    price = fields.Float(string='Visit Price', required = True)
    state = fields.Selection([
        ("new","new"), ("progress","progress"), ("done","done")
    ],default= "new")

    doctor_id = fields.Many2one('doctor')
    patient_id = fields.Many2one('patient')
    insurance_company_id = fields.Many2one('insurance_company')
    insurance_plan_id = fields.Many2one('insurance_plan')
    visit_line_id = fields.One2many('visit_line', 'visit_id')

    @api.onchange('insurance_plan_id')
    def onchange_insurance_plan_id(self):
        plan_lines = self.insurance_plan_id.insurance_plan_line_id
        print(plan_lines)
        for visit_line in self.visit_line_id:
            for plan_line in plan_lines:
                if visit_line.product_id.id == plan_line.product_id.id:
                    visit_line.insurance_company_share = plan_line.price * plan_line.percentage
                    visit_line.patient_share = plan_line.price - visit_line.insurance_company_share


    def progress_visit(self):
        self.state = "progress"

    def finish_visit(self):
        self.state = "done"
        claim_state = self.env['ir.config_parameter'].get_param('demo.claim_state')
        print(claim_state)

        if claim_state == "insurance company only":
            print("creatinggggggggggg Olny")
            self.create_invoice(True)
        elif claim_state == "insurance company  and patient":
            print("creatinggggggggggg both")
            self.create_invoice(True)
            self.create_invoice(False)
        
        # # obj id
        # print(self.insurance_company_id.partner_id.id)
        # # whole obj(id,name,.....)
        # print(self.insurance_company_id.partner_id)


    def create_invoice(self, is_company):
        invoice_lines = []
        for line in self.visit_line_id:
            if is_company:
                price = line.insurance_company_share
            else:
                price = line.patient_share
            invoice_lines.append((0, 0, {
                'product_id': line.product_id.id,
                'name': line.product_id.name,
                'price_unit': price,

                # 'quantity': line.quantity,
                # 'tax_ids': [(6, 0, line.tax_ids.ids)],
            }))

        if is_company:
            partner_id = self.insurance_company_id.partner_id.id
        else:
            partner_id = self.patient_id.partner_id.id
        print(self.env['account.move'].create({
            # 'partner_id':self.insurance_company_id.partner_id.id,
            'partner_id':partner_id,
            'move_type':'out_invoice',
            'invoice_line_ids':invoice_lines
        }))



            
        

