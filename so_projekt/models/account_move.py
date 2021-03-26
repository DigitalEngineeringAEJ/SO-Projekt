from odoo import _, api, models
from datetime import datetime
import csv
from tempfile import TemporaryFile
import base64


class AccountMove(models.Model):
    _inherit = "account.move"

    def _constrains_date_sequence(self):
        # Multiple import methods set the name to things that are not sequences:
        # i.e. Statement from {date1} to {date2}
        # It makes this constraint not applicable, and it is less needed on bank statements as it
        # is only an indication and not some thing legal.
        return

    @api.model
    def sent_email_invoice_customers(self):
        today = datetime.today()
        year = today.year
        month = today.month
        moves = self.env["account.move"].search(
            [('move_type', '=', 'out_invoice'), ('state', '=', 'posted'), ('invoice_date', '>=', self.env.user.company_id.invoice_date_from), ('invoice_date', '<=', self.env.user.company_id.invoice_date_to)], order="invoice_date ASC")
        date_sent_mail = (
            datetime(year, month, int(self.env.user.company_id.day))
        ).date()
        fileobj = TemporaryFile("w+")
        fileobj.seek(0)

        with open('invoices_customer.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_NONE)
            writer.writerow(['Invoice amount gross incl. 7% VAT', 'S for debit entry', 'Customer number', '4300', 'Invoice date', 'Invoice number', 'Customer name'])
            for move in moves:
                writer.writerow([str(move.amount_total).replace(".",",") if move.amount_total else "", 'S', move.partner_id.ref if move.partner_id.ref else "", '4300', move.invoice_date.strftime("%d-%m-%Y") if move.invoice_date else "", move.name if move.name else "", move.partner_id.name if move.partner_id.name else ""])

        files = base64.b64encode(open('invoices_customer.csv', 'rb').read())
        values = {

            'name': 'invoices_customer_%s/%s.csv' %(month,year),
            'datas': files,

        }
        attachment = self.env['ir.attachment'].create(
            values
        )
        if date_sent_mail == today.date():
            mail = self.env["mail.mail"].sudo().create(
                {
                    "body_html": self.env.user.company_id.description,
                    "email_to": self.env.user.company_id.recipient_id.email,
                    "subject": self.env.user.company_id.subject,
                    "attachment_ids": [(4, attachment.id)]
                }
            )
            mail.send()