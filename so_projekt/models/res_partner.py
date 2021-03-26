from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    register_court_name = fields.Char(string="Register Court Name")
    company_registry = fields.Char(string="Company registry")
