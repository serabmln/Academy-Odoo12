from odoo import fields, models

class Course(models.Model):
    _name = 'ridwan.course.category'
    _description = 'Data Course Category'

    name = fields.Char(
        string='Course Name Category',
        required= True,
        help="Fill course category name.."
    )
    
    description  = fields.Text(
        string='Description',
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    course_ids = fields.One2many(
        comodel_name='ridwan.course', 
        inverse_name='category_id', 
        string='Course')
    
    
    


