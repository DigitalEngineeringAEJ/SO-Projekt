from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    # ------------------------------------------------------------
    # Fields
    # ------------------------------------------------------------
    customer_group_id = fields.Many2one('res.partner.category', string='Customer Group')

    # ------------------------------------------------------------
    # Methodes
    # ------------------------------------------------------------
    def _select(self):
        return super(AccountInvoiceReport, self)._select() + ", move.customer_group_id as customer_group_id"