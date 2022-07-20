import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api
from odoo.exceptions import UserError

class QualsysSchool(models.Model):
	_name = 'qualsys.school'
	_description = 'Escuelas'

	@api.depends('courses_ids')
	def get_courses_number(self):
		_logger.info("##### Este es el self: %s" % self)
		for data in self:
			_logger.info("##### Este es el data dentro del self: %s" % data)
			data.courses_number = len(data.courses_ids)

	name = fields.Char(string = "Nombre", required = True)
	street = fields.Char(string = "Calle")
	street_number = fields.Char(string = "No. Ext.")
	city = fields.Char(string = "Ciudad", required = True)
	state = fields.Many2one('res.country.state', string = "Estado", required = True)
	country = fields.Many2one('res.country', string = "País", required = True)
	phone_one = fields.Char(string = "Teléfono Uno", required = True)
	phone_two = fields.Char(string = "Teléfono Dos")
	email = fields.Char(string = 'Correo', required = True)
	courses_number = fields.Integer(compute = get_courses_number, string = "No. Cursos")
	
	courses_ids = fields.One2many('qualsys.courses', 'school_id', string="Curso", required = True)