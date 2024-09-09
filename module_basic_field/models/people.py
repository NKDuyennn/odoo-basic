from odoo import models, fields

class People(models.Model):
    _name = 'people'
    _description = 'People'
    
    # size là số ký tự, trim là cắt đầu cắt đuôi khoảng trắng, translate bật tính năng tự động dịch
    name = fields.Char(string='Name', size=8, trim=True, translate=True)
    available = fields.Boolean(string='Available')
    height = fields.Float(string='Height', digits='test')
    age = fields.Integer(string='Age')