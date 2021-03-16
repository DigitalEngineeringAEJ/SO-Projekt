from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    recipient_id = fields.Many2one('res.partner', string='Recipient')
    day = fields.Integer(string="Day", default=28)
    subject = fields.Char(string="Subject")
    description = fields.Html(string="Description")
    invoice_date_from = fields.Date(string='Date From')
    invoice_date_to = fields.Date(string='Date To')
