from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalAppointments (models.Model):
    _name='hospital.appointments'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description='Hospital Appointments'
    
    name = fields.Char(string='Order Reference', copy=False, required=True, readonly=True, 
                            default=lambda self: ('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    age = fields.Integer(String='Age', related='patient_id.age', tracking=True)
    state = fields.Selection(selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancel')
        ], string='Status', default='draft', tracking=True)
    gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
    ], required=True)
    note = fields.Text(String='Description')
    date_appointment = fields.Date(String="Date Appointment")
    date_chekup = fields.Datetime('Date Chek Up Time')
    prescrition = fields.Text(String='Doctor Prescription')
    prescription_line_ids = fields.One2many('hospital.appointment.line', 'appointment_id', string='Prescription Line')
    
    
    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'
        
    @api.model
    def create(self,vals):
        if vals.get('name',('New')=="New"):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointments') or ('New')
        res = super(HospitalAppointments, self).create(vals)
        return res
    
    def unlink(self):
        if self.state == 'done':
            raise ValidationError(("Tidak Bisa Hapus %s State Done" % self.name))
        return super(HospitalAppointments,self).unlink()
    
    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.note:
                self.note = self.patient_id.note
        else:
            self.gender = ''
            self.note = ''

class HospitalAppointmentsLine(models.Model):
    _name='hospital.appointment.line'
    _description='Hospital Appointment Line'
    
    name = fields.Char(string="Medicine", required=True)
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointments', string='Appointment')
        
    