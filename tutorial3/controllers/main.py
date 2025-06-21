from odoo import http
from odoo.http import request


class Controller(http.Controller):
    @http.route('/demo-page', auth='public',
                        website=True, methods=['GET'])
    def demo_page_endpoint(self, **kw):
        return request.render("tutorial3.demo_page", {
            "title": "Title of the page", 
            "body_classname": "demo-page",
            "var1": "value1"})