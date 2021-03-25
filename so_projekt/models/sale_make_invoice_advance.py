from odoo import api, fields, models, _


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        invoice = super(SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        if order.comment:
            invoice.sudo().message_post(body=order.comment, author_id=invoice.partner_id.id, message_type='comment',)
        return invoice