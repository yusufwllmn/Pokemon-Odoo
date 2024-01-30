# -*- coding: utf-8 -*-
# from odoo import http


# class CustomInherit(http.Controller):
#     @http.route('/custom_inherit/custom_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_inherit/custom_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_inherit.listing', {
#             'root': '/custom_inherit/custom_inherit',
#             'objects': http.request.env['custom_inherit.custom_inherit'].search([]),
#         })

#     @http.route('/custom_inherit/custom_inherit/objects/<model("custom_inherit.custom_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_inherit.object', {
#             'object': obj
#         })

