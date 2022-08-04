# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase, tagged
import logging

_log = logging.getLogger(__name__)


@tagged("sdl", "post_install", "-at_install")
class TestAutoUpdate(TransactionCase):
    def setUp(self):
        super().setUp()
