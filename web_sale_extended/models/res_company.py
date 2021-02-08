# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = 'res.company'
    
    logo_website_pdf  = fields.Binary(string="Logo Website PDF", readonly=False)
    logo_supervigilado  = fields.Binary(string="Logo Supervigilado", readonly=False)

    mail_tusdatos = fields.Char("E-mail TusDatos")
    password_tusdatos = fields.Char("Password TusDatos")
