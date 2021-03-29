from odoo import api, fields, models
from openerp.exceptions import ValidationError


class Session(models.Model):
    _name = 'ridwan.session'
    _description = 'Data Course Session..'

    name = fields.Char(string='Name')
    course_id = fields.Many2one(comodel_name='ridwan.course', string='Course')
    instructor_id = fields.Many2one(comodel_name='res.partner',
                                    string='Instructor',
                                    domain="[('is_instructor','=', True)]",
                                    )
    session_date = fields.Datetime(string='Session Date',
                                   default=fields.Datetime.now()
                                   )
    min_attendee = fields.Integer(string='Minimum Attendee')
    attendee_ids = fields.One2many(
        comodel_name='ridwan.attendee', inverse_name='session_id', string='Attendee')
    taken_seats = fields.Float(
        compute='_compute_taken_seats', string='Taken Seats', store=True,)

    @api.depends('min_attendee', 'attendee_ids')
    def _compute_taken_seats(self):
        for record in self:
            if not record.min_attendee:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * \
                    len(record.attendee_ids) / record.min_attendee

    @api.onchange('min_attendee', 'attendee_ids')
    def _onchange_attendee(self):
        if self.min_attendee < 0:
            return {
                'warning': {
                    'title': "Salah Data!",
                    'message': "Minimal Attendee tidak boleh dari 0",
                },
            }
        if self.min_attendee < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "To Many attendee!",
                    'message': "Incrase min attendee or remove axcess attendee",
                },
            }

    _sql_constraints = [
        ('name_unique',
         'UNIQUE (name)',
         "Nama Session Tidak Boleh Sama!"
         ),
    ]

    @api.constrains('instructor_id', 'attendee_ids')
    def _chek_instructor_not_in_attendees(self):
        for r in self:
            students = [record.student_id.id for record in r.attendee_ids]
            print("students")
            if r.instructor_id and r.instructor_id.id in students:
                raise ValidationError("Salah!")


class Attendee(models.Model):
    _name = 'ridwan.attendee'
    _description = 'attendee of course session..'

    name = fields.Char(string='No Pendaftaran')
    student_id = fields.Many2one(comodel_name='res.partner',
                                 string='Student',
                                 domain="[('is_student','=', True)]",
                                 )
    reg_date = fields.Datetime(string='Reg Date',
                               default=fields.Datetime.now(),
                               )
    session_id = fields.Many2one(
        comodel_name='ridwan.session', string='Session')
    remarks = fields.Char(string='Remarks')
