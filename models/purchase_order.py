# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class PurchaseOrder(models.Model):
    _name = 'budget.purchase.order'
    _rec_name = 'no'
    _description = 'Purchase Order'
    _order = 'no'

    # CHOICES
    # ----------------------------------------------------------
    STATES = choices_tuple(['draft', 'active', 'closed', 'cancelled'], is_sorted=False)
    TYPES = choices_tuple(['standard', 'blanket', 'planned'], is_sorted=False)

    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(STATES, default='draft')

    is_parent = fields.Boolean(default=True)
    type = fields.Selection(TYPES, default='standard')
    no = fields.Char(string='Purchase Order')
    date = fields.Date(string='Date')
    amount = fields.Monetary(string='Amount', currency_field='currency_id')
    remark = fields.Text(string='Remark')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=lambda self: self.env.user.company_id.currency_id)

    contractor_id = fields.Many2one('budget.contractor.contractor', string='Contractor')

    po_line_ids = fields.One2many('budget.purchase.order.line',
                                  'po_id',
                                  string="Lines")

    # parent is the main PO
    parent_id = fields.Many2one('budget.purchase.order',
                                domain=[('is_parent', '=', True)],
                                string='Parent Purchase Order')

    # TODO WORK AND RESEARCH NEEDS ON THIS, MUST VERIFY IF ALLCATION OR JUST VIEWING
    cear_ids = fields.Many2many('budget.capex.cear',
                                'budget_cear_po_rel',
                                'po_id',
                                'cear_id',
                                string='CEARs')

    # TODO WORK AND RESEARCH NEEDS ON THIS, MUST VERIFY IF ALLCATION OR JUST VIEWING
    oear_ids = fields.Many2many('budget.opex.oear',
                                'budget_oear_po_rel',
                                'po_id',
                                'oear_id',
                                string='OEARs')

    # ONCHANGE FIELDS
    # ----------------------------------------------------------
    @api.onchange('parent_id')
    def _onchange_is_parent(self):
        self.is_parent = not self.parent_id

    # BUTTONS/TRANSITIONS
    # ----------------------------------------------------------
    @api.one
    def set2draft(self):
        self.state = 'draft'

    @api.one
    def set2active(self):
        self.state = 'active'

    @api.one
    def set2closed(self):
        self.state = 'closed'

    @api.one
    def set2cancelled(self):
        self.state = 'cancelled'
