# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _name = 'budget.purchase.order.line'
    _description = 'Purchase Order Line'
    _rec_name = 'sequence'
    _order = 'sequence asc'

    sequence = fields.Integer(string='SR', default=1)
    description = fields.Text(string='Description')
    quantity = fields.Float(default=0.00)
    unit_price = fields.Monetary(string='Price', currency_field='currency_id')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    currency_id = fields.Many2one('res.currency', readonly=True,
                                  default=lambda self: self.env.user.company_id.currency_id)
    po_id = fields.Many2one('budget.purchase.order', string='Purchase Order')

    # COMPUTE FIELDS
    # ----------------------------------------------------------
    revised_unit_price = fields.Monetary(string='Revised Price',
                                         compute='_compute_revised_unit_price',
                                         inverse='_inverse_revised_unit_price',
                                         currency_field='currency_id')

    total_amount = fields.Monetary(currency_field='currency_id',
                                   store=True,
                                   compute="_compute_total_amount",
                                   string='Amount')

    @api.one
    @api.depends('unit_price', 'quantity')
    def _compute_total_amount(self):
        self.total_amount = self.revised_unit_price * self.quantity

    @api.one
    @api.depends('unit_price')
    def _compute_revised_unit_price(self):
        if self.revised_unit_price in [0, 0.0, False]:
            self.revised_unit_price = self.unit_price
        return

    @api.one
    def _inverse_revised_unit_price(self):
        pass

    # POLYMORPH FUNCTIONS
    # ----------------------------------------------------------
    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}: {}".format(record.po_id.no,
                                                      record.sequence)
                           )
                          )
        return result
