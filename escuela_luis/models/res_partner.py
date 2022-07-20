import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api
from odoo.exceptions import UserError

class ResPartner(models.Model):
	_inherit = 'res.partner'

	is_attendant = fields.Boolean(string = "Está inscrito a un curso", readonly = True)