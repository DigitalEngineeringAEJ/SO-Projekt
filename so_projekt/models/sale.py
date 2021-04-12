from odoo import fields, api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # ------------------------------------------------------------
    # Fields
    # ------------------------------------------------------------
    comment = fields.Text(string="Comment")

    # ------------------------------------------------------------
    # Methodes
    # ------------------------------------------------------------
    def _create_invoices(self, grouped=False, final=False, date=None):
        moves = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final, date=date)
        for order in self:
            if order.comment:
                for move in moves:
                    move.sudo().message_post(body=order.comment, author_id=move.partner_id.id, message_type='comment', )
        return moves