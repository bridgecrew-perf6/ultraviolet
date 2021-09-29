# -*- coding: utf-8 -*-
#
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 NYU.
#
# ultraviolet is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
# conftest.py
"""Pytest configuration."""


import invenio_app.factory as factory
from invenio_base.wsgi import wsgi_proxyfix
from invenio_config import create_config_loader
import pytest
import os


@pytest.fixture(scope="module")
def create_ultraviolet_app_ui(ultraviolet_instance_path):
    create_ultraviolet_app_ui = factory.create_app_factory(
        "ultraviolet",
        config_loader=create_config_loader(config=None, env_prefix="Invenio"),
        blueprint_entry_points=["invenio_base.blueprints"],
        extension_entry_points=["invenio_base.apps"],
        converter_entry_points=["invenio_base.converters"],
        wsgi_factory=wsgi_proxyfix(),
        instance_path=ultraviolet_instance_path,
        static_folder=os.path.join(ultraviolet_instance_path, "static"),
        root_path=ultraviolet_instance_path,
        app_class=factory.app_class(),
    )

    return create_ultraviolet_app_ui


@pytest.fixture(scope="module")
def create_app(create_ultraviolet_app_ui):
    """Flask app fixture."""
    return create_ultraviolet_app_ui
