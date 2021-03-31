from odoo.api import Environment


def migrate(cr, version):
    """Update Invoices."""
    env = Environment(cr, 1, context={})
    invoices = env["account.move"].sudo().search([('move_type', '=', 'out_invoice'), ('state', '=', 'posted'), ('name', '!=', '/')], order="invoice_date, name")
    invoices_not_migrated = env["account.move"].sudo().search([('move_type', '=', 'out_invoice'), ('state', '=', 'posted'), ('name', 'ilike', '/')])
    print("Start change old invoice number")
    if invoices_not_migrated:
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
    print("Finish change old invoice number")
    print("Start add automatically ref to partner")
    partners = env["res.partner"].sudo().search([('ref', '=', False)], order="create_date")
    partner_seq = env["ir.sequence"].search([('code', "=", "res.partner.seq")], limit=1)
    ref = 10327
    for partner in partners:
        partner.ref = ref
        ref = int(ref) + 1
    partner_seq.number_next_actual = ref
    print("Finish change old invoice number")

