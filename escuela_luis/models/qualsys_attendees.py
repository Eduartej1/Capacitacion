import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api
from odoo.exceptions import UserError

class QualsysAttendees(models.Model):
	_name = 'qualsys.attendees'
	_description = 'Asistentes'

	partner_id = fields.Many2one('res.partner', string = "Nombre")
	courses_id = fields.Many2one('qualsys.courses', string = "Curso")
	age = fields.Integer(string = "Edad")

	#@api.depends('res.partner')
	#@api.onchange('partner_id')
	#def _change_contact(self):
		#contact = self.env['res.partner'].search([('id', '=', self.partner_id.id)])
		#if contact in self.env['res.partner'].search(['id', '=', self.partner_id.id]):
			#contact.is_attendant = True
		#else:
			#contact.is_attendant = False