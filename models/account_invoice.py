# -*- coding: utf-8 -*-
##############################################################################
#
# This module is developed by Deddy Setiawan
# Copyright (C) 2017 Deddy Setiawan (<http://dedset.xyz>).
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo.tools import amount_to_text_en
from odoo.exceptions import UserError
from odoo import fields, api, models, _

class AccountInvoice(models.Model):
	_inherit='account.invoice'

	in_words = fields.Char('In Words', compute='_computeInWords')

	@api.depends('amount_total')
	def _computeInWords(self):
		self.in_words = amount_to_text_en.amount_to_text(self.amount_total, currency='Dollars')

	