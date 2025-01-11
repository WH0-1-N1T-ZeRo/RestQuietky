from odoo import models, fields, api
from datetime import datetime, timedelta  # Time Setting

class RestSchedule(models.Model):
    _name = 'rest.schedule'
    _description = 'Rest Schedule'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # InheritChatter

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    start_time = fields.Datetime(string='Start Time', required=True, default=fields.Datetime.now)
    end_time = fields.Datetime(string='End Time', required=True, default=lambda self: fields.Datetime.now() + timedelta(hours=1))
    category = fields.Selection([
        ('sleep', 'Sleep'),
        ('work_break', 'Work Break'),
        ('meditation', 'Meditation')
    ], string='Category', required=True)
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
    status = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('completed', 'Completed'),
        ('missed', 'Missed')
    ], string='Status', compute='_compute_status', store=True)

    @api.depends('start_time', 'end_time')
    def _compute_status(self):
        current_time = fields.Datetime.now()
        for record in self:
            if record.end_time < current_time:
                record.status = 'completed'
            elif record.start_time > current_time:
                record.status = 'upcoming'
            else:
                record.status = 'missed'
