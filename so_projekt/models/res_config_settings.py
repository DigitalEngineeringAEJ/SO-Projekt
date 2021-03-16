from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    recipient_id = fields.Many2one('res.partner', related="company_id.recipient_id", readonly=0)
    day = fields.Integer(string="Day", related="company_id.day", readonly=0)
    subject = fields.Char(string="Subject", related="company_id.subject", readonly=0)
    description = fields.Html(string="Description", related="company_id.description", readonly=0)
    invoice_date_from = fields.Date(string='Date From', related="company_id.invoice_date_from", readonly=0)
    invoice_date_to = fields.Date(string='Date To', related="company_id.invoice_date_to", readonly=0)
