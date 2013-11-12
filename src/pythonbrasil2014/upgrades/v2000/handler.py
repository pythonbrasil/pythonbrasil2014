# -*- coding:utf-8 -*-
from plone.app.upgrade.utils import loadMigrationProfile
from pythonbrasil2014.config import PROJECTNAME

import logging


def apply_profile(context):
    ''' Apply upgrade profile '''
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-pythonbrasil2014.upgrades.v2000:default'
    loadMigrationProfile(context, profile)
    logger.info('Loaded upgrade profile to version 2000')
