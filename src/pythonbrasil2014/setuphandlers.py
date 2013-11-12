# -*- coding:utf-8 -*-
from pythonbrasil2014.config import PROJECTNAME

import logging

logger = logging.getLogger(PROJECTNAME)

REMOVE = [
    'events',
    'front-page',
    'Members',
    'news',
]


def remove_default_content(p):
    ''' Remove default content
    '''
    oIds = p.objectIds()
    to_remove = [oId for oId in REMOVE if oId in oIds]
    p.manage_delObjects(to_remove)
    logger.info('Default content removed')


def setup_portal(context):
    ''' Setup portal content
    '''
    if context.readDataFile('initcontent.txt') is None:
        return
    site = context.getSite()
    # Remove default content
    remove_default_content(site)
