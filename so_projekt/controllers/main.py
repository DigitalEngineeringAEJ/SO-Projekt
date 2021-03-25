from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class WebsiteSale(WebsiteSale):

    @http.route(['/shop/payment/customer_comment'], type="json", auth="public", methods=["POST"], website=True,)
    def payment_customer_comment(self, **post):
        comment = post.get("comment", False)
        order = request.website.sale_get_order()
        order.comment = comment