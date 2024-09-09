import json
from odoo import http
import werkzeug
from odoo.http import request

# class NKDuyenController(http.Controller):
    
    # @http.route('/nkduyen', auth='public', type='http')
    # def nkduyen_check(self):
    #     return "NKDuyen check check check"
    
    # @http.route(['/nkduyen', '/nkduyen1'], auth='public', type='http')
    # def nkduyen_check(self):
    #     return "NKDuyen check check check"


    # Truyền biến qua đường dẫn
    # @http.route('/nkduyen/<int:id>', auth='public', type='http')
    # def nkduyen_check(self, id):
    #     return "NKDuyen check check check %s" %str(id)
    
    # @http.route('/nkduyen', auth='public')
    # def nkduyen_check(self):
    #     return werkzeug.utils.redirect('https://www.google.com')
    
    # Render đến module web.login trong addon của odoo
    # @http.route('/nkduyen', auth='public')
    # def nkduyen_check(self):
    #     return request.render("web.login")
    #
    # # return json
    # @http.route('/nkduyen', auth='public', type='http')
    # def nkduyen_check(self):
    #     return json.dumps({
    #         "check": "check 123"
    #     })
    
    # Xử lý database trong controller
    # @http.route('/nkduyen', auth='public', type='http')
    # def nkduyen_check(self):
    #     partner = request.env['res.partner'].sudo().create({
    #         'name' : 'NKDuyen'
    #     })
    #     return 'Partner has been created'
    #

    