from odoo import http

from ..article_registry import article_registry


class DashboardController(http.Controller):
    @http.route('/odoo-tutorials', type="json", auth="user")
    def get_articles(self):
        return article_registry