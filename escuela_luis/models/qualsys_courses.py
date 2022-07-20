import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api
from odoo.exceptions import UserError

class QualsysCourses(models.Model):
	_name = 'qualsys.courses'
	_description = 'Cursos'

	@api.depends("attendees_ids")
	def get_course_attendees(self):
		_logger.info("##### Este es el self: %s" % self)
		for data in self:
			_logger.info("##### Este es el data dentro del self: %s" % data)
			data.attendees_number = len(data.attendees_ids)

	name = fields.Char(string = "Nombre", required = True)
	duration = fields.Integer(string = "Duración en horas", required = True)
	start_date = fields.Date(string = "Fecha de inicio", required = True)
	end_date = fields.Date(string = "Fecha de termino", required = True)
	code = fields.Char(string = "Codigo", required = True)
	teacher_id = fields.Many2one('res.users', string = "Instructor")
	attendees_number = fields.Integer(compute = get_course_attendees, string = "No. Asistentes")
	
	school_id= fields.Many2one('qualsys.school', string = "Escuela")
	attendees_ids = fields.One2many('qualsys.attendees', 'courses_id', string = "Asistentes")