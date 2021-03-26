from odoo.api import Environment


def migrate(cr, version):
    """Update Invoices."""
    env = Environment(cr, 1, context={})
    invoices = env["account.move"].sudo().search([('move_type', '=', 'out_invoice'), ('name', '!=', '/')], order="invoice_date, name")
    print("Start")
    first_invoice = invoices[0]
    code_first_invoice = invoices[0].name.split('/', 4)
    invoices[0].name = "RG_10_%s" % str(code_first_invoice[3])
    invoices[0].payment_reference = invoices[0].name
    for invoice in invoices:
        if invoice != first_invoice:
            code = invoice.name.split('/', 4)
            new_code = int(code[3]) + 1
            invoice.name = "RG_10_%04d" % new_code
            invoice.payment_reference = invoice.name

    print("Finish")

