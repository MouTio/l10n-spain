# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


def _fill_aeat_dates_model(env, model):
    env.cr.execute(
        """SELECT r.id, af.date_start
        FROM account_fiscalyear af
        JOIN %s r ON r.fiscalyear_id = af.id""" % model._table
    )
    for row in env.cr.fetchall():
        record = model.browse(row[0])
        record.year = int(row[1][:4])
        record.onchange_period_type()


def fill_aeat_dates(env):
    """Fill year and start/end dates of all AEAT reports, detected by
    the existence of `_aeat_number` variable."""
    AEAT_BASE_MODELS = [
        u'l10n.es.aeat.report',
        u'l10n.es.aeat.report.tax.mapping',
    ]
    for model in env['ir.model'].search([]):
        try:
            m = env[model.model]
        except KeyError:
            continue
        if not hasattr(m, '_aeat_number') or m._name in AEAT_BASE_MODELS:
            continue
        _fill_aeat_dates_model(env, m)


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    fill_aeat_dates(env)
