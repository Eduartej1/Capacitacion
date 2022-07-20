from odoo import fields, models


class WizardAssingCourses(models.TransientModel):
    _name = 'wizard.assing.courses'
    _description = 'Asignación de cursos a escuelas'

    courses_id = fields.Many2one('qualsys.courses', string="Curso a asociar")

    def asignador(self):
        print('Entramos al Wizard')
        for record in self:
            print(record.courses_id)
            print(record.courses_id.name)
            escuela_id = int(self.env.context.get('active_id', False))
            print(escuela_id)
            record.courses_id.school_id = escuela_id