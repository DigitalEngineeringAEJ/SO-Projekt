from odoo import _, api, models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    # ------------------------------------------------------------
    # Fields
    # ------------------------------------------------------------
    register_court_name = fields.Char(string="Register Court Name")
    company_registry = fields.Char(string="Company registry")
    customer_group_id = fields.Many2one('res.partner.category', string='Customer Group', compute='_compute_customer_group', store=1)

    # ------------------------------------------------------------
    # ORM
    # ------------------------------------------------------------
    @api.model
    def create(self, vals):
        """Add sequence to partner."""
        partner = super(ResPartner, self).create(vals)
        code = self.env["ir.sequence"].next_by_code(
                "res.partner.seq"
            )
        partner.ref = code
        return partner

    # ------------------------------------------------------------
    # Compute Methodes
    # ------------------------------------------------------------
    @api.depends('category_id')
    def _compute_customer_group(self):
        for partner in self:
            partner.customer_group_id = False
            if partner.category_id:
                partner.customer_group_id = partner.category_id[0].id