{
	'name':"qualsys_school",

	'description':" Escuela de cursos Odoo ",

	'author':"Daniel Rodríguez",

	'depends':[
		'base'
	],

	'data':[
		'wizard/wizard_assing_courses_views.xml',
		'views/qualsys_school_views.xml',
		'views/qualsys_courses_views.xml',
		'views/qualsys_attendees_views.xml',
		'views/qualsys_res_partner_views.xml',
		'security/ir.model.access.csv',
	]

}