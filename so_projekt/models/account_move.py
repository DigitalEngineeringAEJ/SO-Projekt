from odoo import _, api, models
from datetime import datetime
import csv
from tempfile import TemporaryFile
import base64
import calendar

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def sent_email_invoice_customers(self):
        today = datetime.today()
        year = today.year
        month = today.month
        first_day_month = (
            datetime(year, month, 1)
        ).date()
        last_day_month = (
            datetime(year, month, calendar.mdays[month])
        ).date()
        moves = self.env["account.move"].search(
            [('move_type', '=', 'out_invoice'), ('state', '=', 'posted'), ('invoice_date', '>=', first_day_month), ('invoice_date', '<=', last_day_month)])
        date_sent_mail = (
            datetime(year, month, int(self.env.user.company_id.day))
        ).date()
        fileobj = TemporaryFile("w+")
        fileobj.seek(0)

        with open('invoices_customer.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            writer.writerow(['Invoice amount gross incl. 7% VAT', 'S for debit entry', 'Customer number', '4300', 'Invoice date', 'Invoice number', 'Customer name'])
            for move in moves:
                writer.writerow([move.amount_total if move.amount_total else "", 'S', move.partner_id.ref if move.partner_id.ref else "", '4300', move.invoice_date if move.invoice_date else "", move.name if move.name else "", move.partner_id.name if move.partner_id.name else ""])

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
