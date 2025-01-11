from odoo import models, fields, api

class RestLog(models.Model):
    _name = 'rest.log'
    _description = 'Rest Logs'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # InheritChatter

    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    sleep_duration = fields.Float(string='Sleep Duration (hours)', required=True)
    stress_level = fields.Integer(string='Stress Level (1-10)')
    notes = fields.Text(string='Notes')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
