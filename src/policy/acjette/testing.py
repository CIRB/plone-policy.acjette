from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PolicyAcjette(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import policy.acjette
        xmlconfig.file('configure.zcml',
                       policy.acjette,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy.acjette:default')

POLICY_ACJETTE_FIXTURE = PolicyAcjette()
POLICY_ACJETTE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(POLICY_ACJETTE_FIXTURE, ),
                       name="PolicyAcjette:Integration")