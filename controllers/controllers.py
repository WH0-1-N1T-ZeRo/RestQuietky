# -*- coding: utf-8 -*-
# from odoo import http


# class RestQuietky(http.Controller):
#     @http.route('/rest_quietky/rest_quietky', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rest_quietky/rest_quietky/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rest_quietky.listing', {
#             'root': '/rest_quietky/rest_quietky',
#             'objects': http.request.env['rest_quietky.rest_quietky'].search([]),
#         })

#     @http.route('/rest_quietky/rest_quietky/objects/<model("rest_quietky.rest_quietky"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rest_quietky.object', {
#             'object': obj
#         })

