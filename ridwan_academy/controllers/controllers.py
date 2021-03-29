# -*- coding: utf-8 -*-
from odoo import http

# class RidwanAcademy(http.Controller):
#     @http.route('/ridwan_academy/ridwan_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ridwan_academy/ridwan_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ridwan_academy.listing', {
#             'root': '/ridwan_academy/ridwan_academy',
#             'objects': http.request.env['ridwan_academy.ridwan_academy'].search([]),
#         })

#     @http.route('/ridwan_academy/ridwan_academy/objects/<model("ridwan_academy.ridwan_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ridwan_academy.object', {
#             'object': obj
#         })