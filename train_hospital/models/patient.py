# from unittest import result
from turtle import colormode
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name= 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description= 'Hospital Patient'

    reference = fields.Char(string='Reference', copy=False, required=True, readonly=True, 
                            default=lambda self: ('New'))
    name = fields.Char(String='Name', required=True)
    age = fields.Integer(String='Age', required=True, tracking=True)
    gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
    ], required=True, default='male')
    note = fields.Text(String='Description')
    state = fields.Selection(selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancel')
        ], string='Status', default='draft', tracking=True)
    responsible_id = fields.Many2one(comodel_name='res.partner', String='Responsible')
    appointment_count = fields.Integer(String='Appointment Count', compute='_compute_appointment_count')
    image = fields.Binary(string='patient_image')
    doctor_id = fields.Many2one(comodel_name='hospital.doctor', String="Doctor")
    doctor_specialis = fields.Char(String="Doctor Specialis")
    appointments_ids = fields.One2many('hospital.appointments', 'patient_id', string='Appointments')
    
    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointments'].search_count([('patient_id','=',rec.id)])
            rec.appointment_count = appointment_count
    
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference', ('New')) == ("New"):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or ('New')
        res = super(HospitalPatient, self).create(vals)
        return res
    
    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        # print("TEST GET DEFAUTL", fields)
        # print("TEST GET DEFAULT", res)
        res['gender'] = 'other'
        res['age'] = 50
        res['note'] = 'Test Method Get Default'
        return res
    
    @api.onchange('doctor_id')
    def get_doctor_specialis(self):
        if self.doctor_id:
            if self.doctor_id.note:
                self.doctor_specialis = self.doctor_id.note
        else:
            self.doctor_specialis = ''