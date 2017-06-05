# -*- coding: utf-8 -*-
# pylint: disable=logging-format-interpolation
"""
Configuration loading.
"""

from __future__ import unicode_literals, absolute_import

import os
import logging
import yaml


# pylint: disable=invalid-name
logger = logging.getLogger(__name__)


def get_config(config_file=None):
    """Loads config file and returns its content."""
    default_conf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dump2polarion.yaml')
    user_conf = config_file or '~/.config/dump2polarion.yaml'

    try:
        with open(os.path.expanduser(user_conf)):
            pass
    except EnvironmentError:
        user_conf = None
        if config_file:
            raise EnvironmentError("cannot open config file '{}'".format(config_file))

    with open(default_conf) as input_file:
        config_settings = yaml.load(input_file)
    logger.debug("Default config loaded from '{}'".format(default_conf))

    if user_conf:
        with open(user_conf) as input_file:
            config_settings_user = yaml.load(input_file)
        logger.info("Config loaded from '{}'".format(user_conf))

        # merge default and user configuration
        config_settings.update(config_settings_user)

    return config_settings
