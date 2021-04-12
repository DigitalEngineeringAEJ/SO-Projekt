from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # ------------------------------------------------------------
    # Fields
    # ------------------------------------------------------------
    recipient_id = fields.Many2one('res.partner', string='Recipient')
    day = fields.Integer(string="Day", default=28)
    subject = fields.Char(string="Subject")
    description = fields.Html(string="Description")
    invoice_date_from = fields.Date(string='Date From')
    invoice_date_to = fields.Date(string='Date To')
    register_court_name = fields.Char(related='partner_id.register_court_name', string="Register Court Name", readonly=False)
    company_registry = fields.Char(related='partner_id.company_registry', readonly=False)
