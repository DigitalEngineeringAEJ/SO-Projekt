from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    recipient_id = fields.Many2one('res.partner', related="company_id.recipient_id", readonly=0)
    day = fields.Integer(string="Day", related="company_id.day", readonly=0)
    subject = fields.Char(string="Subject", related="company_id.subject", readonly=0)
    description = fields.Html(string="Description", related="company_id.description", readonly=0)
