from odoo import _, api, models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    register_court_name = fields.Char(string="Register Court Name")
    company_registry = fields.Char(string="Company registry")

    @api.model
    def create(self, vals):
        """Add sequence to partner."""
        partner = super(ResPartner, self).create(vals)
        code = self.env["ir.sequence"].next_by_code(
                "res.partner.seq"
            )
        partner.ref = code
        return partner