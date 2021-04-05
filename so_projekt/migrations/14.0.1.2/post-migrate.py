from odoo.api import Environment


def migrate(cr, version):
    """Update Invoices and Partners."""
    env = Environment(cr, 1, context={})
    partners = env["res.partner"].sudo().search([])
    moves = env['account.move'].sudo().search([])
    print("Start add group customer to partner")
    for partner in partners:
        if partner.category_id:
           partner.customer_group_id = partner.category_id[0]
    print("Finish add group customer to partner")
    print("Start add group customer to move")
    for move in moves:
        if partner.customer_group_id:
            move.customer_group_id = partner.customer_group_id
    print("Finish add group customer to move")
