from odoo import api, fields, models

class SearchAppointmentWizard(models.TransientModel):
    _name= 'search.appointment.wizard'
    _description= 'Search Appointment Wizard'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    
    def search_appointment(self):
        action = self.env.ref('train_hospital.appointments_action').read()[0]
        action['domain']=[('patient_id', '=', self.patient_id.id)]
        return action