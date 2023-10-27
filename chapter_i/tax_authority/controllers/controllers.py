# -*- coding: utf-8 -*-
# from odoo import http


# class TaxAuthority(http.Controller):
#     @http.route('/tax_authority/tax_authority', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tax_authority/tax_authority/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tax_authority.listing', {
#             'root': '/tax_authority/tax_authority',
#             'objects': http.request.env['tax_authority.tax_authority'].search([]),
#         })

#     @http.route('/tax_authority/tax_authority/objects/<model("tax_authority.tax_authority"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tax_authority.object', {
#             'object': obj
#         })

