# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class TaskInherit(models.Model):
    _inherit = 'budget.capex.cear'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------
    # state already exist in the parent model
    # category already exist in the parent model
    # authorized_amount already exist in the parent model

    # RELATIONSHIPS
    # ----------------------------------------------------------
    # company_currency_id already exist in the parent model

    po_ids = fields.Many2many('budget.purchase.order',
                              'budget_cear_po_rel',
                              'cear_id',
                              'po_id',
                              string='Purchase Orders')
    # RELATED FIELDS
    # ----------------------------------------------------------

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # BUTTONS
    # ----------------------------------------------------------
