from odoo import fields, models

class Course(models.Model):
    _name = 'ridwan.course'
    _description = 'Data Course'

    name = fields.Char(
        string='Course Name',
        required= True,
        help="Fill course name.."
    )
    
    description  = fields.Text(
        string='Description',
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    category_id = fields.Many2one(comodel_name='ridwan.course.category', string='Category')
    
    
    
    


