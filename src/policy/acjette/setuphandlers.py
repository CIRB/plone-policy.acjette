from zope import component
from zope.interface import alsoProvides
#from z3c.saconfig.interfaces import IEngineFactory
#from z3c.saconfig import Session
import transaction
from Products.CMFCore.utils import getToolByName
from Products.LinguaPlone.browser.setup import SetupView

def setupLinguaFolders(site, logger):
    sw = SetupView(site, site.REQUEST)

    sw.folders = {}
    pl = getToolByName(site, "portal_languages")
    sw.languages = pl.getSupportedLanguages()
    if len(sw.languages) == 1:
        logger.error('Only one supported language configured.')
    sw.defaultLanguage = pl.getDefaultLanguage()
    available = pl.getAvailableLanguages()
    for language in sw.languages:
        info = available[language]
        sw.setUpLanguage(language, info.get('native', info.get('name')))
    
    sw.linkTranslations()
    sw.removePortalDefaultPage()
    #if sw.previousDefaultPageId:
    #    sw.resetDefaultPage()
    sw.setupLanguageSwitcher()

def setupACJette(context):
    logger = context.getLogger("setupACJette")
    logger.info('start setup ACJette')
    if context.readDataFile('policy.acjette.txt') is None:
        return
    site = context.getSite()
    portal_workflow = site.portal_workflow
    setupLinguaFolders(site, logger)
    
    fr = site.fr

    fr.invokeFactory(type_name='Folder',
        id='commun',
        title='Commun',
        description='',
        language='fr')
    commun = fr.commun
    portal_workflow.doActionFor(commun, 'publish')
    commun.setExcludeFromNav(True)
    commun.reindexObject()

    fr.commun.invokeFactory(type_name='Document',
        id='topnav',
        title='Topnav',
        description='',
        language='fr')
    topnav = fr.commun.topnav
    portal_workflow.doActionFor(topnav, 'publish')
    topnav.setExcludeFromNav(True)
    topnav.reindexObject()

    fr.commun.invokeFactory(type_name='Document',
        id='slider',
        title='Slider',
        description='',
        language='fr')
    slider = fr.commun.slider
    portal_workflow.doActionFor(slider, 'publish')
    slider.setExcludeFromNav(True)
    slider.reindexObject()

    fr.commun.invokeFactory(type_name='Document',
        id='footer',
        title='Footer',
        description='',
        language='fr')
    footer = fr.commun.footer
    portal_workflow.doActionFor(footer, 'publish')
    footer.setExcludeFromNav(True)
    footer.reindexObject()

    fr.commun.invokeFactory(type_name='Document',
        id='tagline',
        title='Tagline',
        description='',
        language='fr')
    tagline = fr.commun.tagline
    portal_workflow.doActionFor(tagline, 'publish')
    tagline.setExcludeFromNav(True)
    tagline.reindexObject()

    nl = site.nl

    nl.invokeFactory(type_name='Folder',
        id='common',
        title='Common',
        description='',
        language='nl')
    common = nl.common
    portal_workflow.doActionFor(common, 'publish')
    common.addTranslationReference(commun)
    common.setExcludeFromNav(True)
    common.reindexObject()

    nl.common.invokeFactory(type_name='Document',
        id='topnav',
        title='Topnav',
        description='',
        language='nl')
    topnavnl = nl.common.topnav
    portal_workflow.doActionFor(topnavnl, 'publish')
    topnavnl.addTranslationReference(topnav)
    topnavnl.setExcludeFromNav(True)
    topnavnl.reindexObject()

    nl.common.invokeFactory(type_name='Document',
        id='slider',
        title='Slider',
        description='',
        language='nl')
    slidernl = nl.common.slider
    portal_workflow.doActionFor(slidernl, 'publish')
    slidernl.addTranslationReference(slider)
    slidernl.setExcludeFromNav(True)
    slidernl.reindexObject()

    nl.common.invokeFactory(type_name='Document',
        id='footer',
        title='Footer',
        description='',
        language='nl')
    footernl = nl.common.footer
    portal_workflow.doActionFor(footernl, 'publish')
    footernl.addTranslationReference(footer)
    footernl.setExcludeFromNav(True)
    footernl.reindexObject()

    nl.common.invokeFactory(type_name='Document',
        id='tagline',
        title='Tagline',
        description='',
        language='nl')
    taglinenl = nl.common.tagline
    portal_workflow.doActionFor(taglinenl, 'publish')
    taglinenl.addTranslationReference(tagline)
    taglinenl.setExcludeFromNav(True)
    taglinenl.reindexObject()

    logger.info('end setup ACJette')
