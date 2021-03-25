from odoo import fields, api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    comment = fields.Text(string="Comment")

    def _create_invoices(self, grouped=False, final=False, date=None):
        move = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final, date=date)
        if self.comment:
            move.sudo().message_post(body=self.comment, author_id=move.partner_id.id, message_type='comment', )
        return move