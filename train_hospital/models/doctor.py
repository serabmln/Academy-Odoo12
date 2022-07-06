from odoo import api, fields, models

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description='Hospital Doctor'
    _rec_name = 'doctor_name' 
    
    doctor_name = fields.Char(String='Doktor Name', required=True)
    age = fields.Integer(String= 'Age')
    gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
    ], required=True, default='male')
    note = fields.Text(String='Description', copy=False)
    image = fields.Binary(String='Image')
    
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('doctor_name'):
            default['doctor_name'] = ("%s (copy)") % (self.doctor_name)
        return super(Doctor, self).copy(default)
        