from odoo import models, fields, api

class RelaxationActivity(models.Model):
    _name = 'relaxation.activity'
    _description = 'Relaxation Activities'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # InheritChatter

    name = fields.Char(string='Activity Name', required=True)
    duration = fields.Integer(string='Duration (minutes)', required=True)
    description = fields.Text(string='Description')
    recommended_for = fields.Selection([
        ('stress', 'Stress Relief'),
        ('focus', 'Focus Improvement'),
        ('relaxation', 'General Relaxation')
    ], string='Recommended For')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
