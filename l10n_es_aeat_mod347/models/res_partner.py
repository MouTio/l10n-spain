# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    not_in_mod347 = fields.Boolean(
        "Not included in 347 report",
        help="If you mark this field, this partner will not be included in "
             "any AEAT 347 model report, independently from the total "
             "amount of its operations.", default=False,
    )

    @api.model
    def _commercial_fields(self):
        res = super(ResPartner, self)._commercial_fields()
        res += ['not_in_mod347']
        return res
