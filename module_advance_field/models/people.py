from odoo import models, fields

class People(models.Model):
    _name = 'people'
    _description = 'People'
    
    name = fields.Char(string='Name')
    
    # Binary Field
    cv1 = fields.Binary(string='CV 1')
    cv2 = fields.Binary(string='CV 2', attachment=False)
    
    # HTML Field
    description = fields.Html(string='Description')
    
    # Image Field
    avatar = fields.Image(string='Avatar', max_width=1920, max_height=1920)
    
    # Selaction Field
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    
    # Text Field
    information = fields.Text(string='Information')
    
    