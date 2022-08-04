# -*- coding: utf-8 -*-

import logging

import odoo


from odoo import api, models

_logger = logging.getLogger(__name__)


class AutoUpdate(models.AbstractModel):
    _name = "auto.update"
    _description = "Auto Update Service"

    @api.model
    def do_auto_update(self):
        messages = []
        self.env["ir.module.module"].update_list()
        installed_modules = self.env["ir.module.module"].search(
            [("state", "=", "installed")]
        )
        for module in installed_modules:
            src_version = odoo.modules.load_information_from_description_file(
                module.name
            )["version"]
            if module.latest_version != src_version:
                msg = f"Auto upgrade module[{module.name}] v{module.latest_version} => v{src_version}"
                _logger.info(msg)
                messages.append(msg)
                module.button_immediate_upgrade()
        return messages

    @api.model
    def _regenerate_assets_bundles(self):
        domain = [
            "&",
            ("res_model", "=", "ir.ui.view"),
            "|",
            ("name", "=like", "%.assets_%.css"),
            ("name", "=like", "%.assets_%.js"),
        ]

        ids = self.env["ir.attachment"].sudo().search(domain)
        ids.unlink()
