# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_core.models.utilities import choices_tuple


class PurchaseOrder(models.Model):
    _name = 'budget.purchase.order'
    _rec_name = 'no'
    _description = 'Purchase Order'
    _order = 'no'

    # CHOICES
    # ----------------------------------------------------------
    STATES = choices_tuple(['draft', 'active', 'closed'], is_sorted=False)

    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(STATES, default='draft')
    no = fields.Char(string='Purchase Order')
    date = fields.Date(string='Date')
    amount = fields.Monetary(string='Amount', currency_field='company_currency_id')
    status = fields.Char(string='Status')
    type = fields.Char(string='Type')
    remark = fields.Text(string='Remark')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    company_currency_id = fields.Many2one('res.currency', readonly=True,
                                          default=lambda self: self.env.user.company_id.currency_id)
    contractor_id = fields.Many2one('res.partner',
                                    domain=[('is_budget_contractor', '=', True)],
                                    string='Invoice')

    cear_ids = fields.Many2many('budget.capex.cear',
                                'budget_cear_po_rel',
                                'po_id',
                                'cear_id',
                                string='CEARs')

    # TODO MOVE TO INVOICE MODULE
    # invoice_ids = fields.One2many('budget.invoice.invoice',
    #                               'po_id',
    #                               string="Invoices")
