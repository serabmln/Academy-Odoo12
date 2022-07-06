from odoo import api, fields, models

class CreateAppointmentWizard(models.TransientModel):
    _name= 'create.appointment.wizard'
    _description= 'Create Appointment Wizard'

    date_appointment = fields.Date(String='Date Appointment')
    patient_id = fields.Many2one('hospital.patient', string='Patient')

    def action_create_appointment(self):
        # print("TEST BUTTON")
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment   
        }
        apppointmen_rec = self.env['hospital.appointments'].create(vals)
        # print("appointment", apppointmen_rec)
        return {
            'name': ('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointments',
            'res_id': apppointmen_rec.id 
        }
    
    def action_view_appointment(self):
        action = self.env.ref('train_hospital.appointments_action').read()[0]
        action['domain']=[('patient_id', '=', self.patient_id.id)]
        return action