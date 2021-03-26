odoo.define("so_projekt.payment", function (require) {
    "use strict";

    var ajax = require("web.ajax");

    $(document).ready(function () {
        $("button#o_payment_form_pay").bind("click", function (ev) {
            var comment = $("#comment").val();
            ajax.jsonRpc("/shop/payment/customer_comment/", "call", {
                comment: comment,
            });
        });
    });
});