from odoo import models, fields

class House(models.Model):
    _name = 'house'
    _discription = 'House'
    
    name = fields.Char(string='Name')
    
    # Many2one field
    people_id = fields.Many2one('people', string='Owner', domain=[('name','=','People 1')])
    
    # Many2many field
    people_ids = fields.Many2many('people', string="People")