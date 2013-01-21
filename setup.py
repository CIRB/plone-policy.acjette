from setuptools import setup, find_packages
import os

version = '1.1.5.dev0'

long_description = (
        open('README.txt').read()
        + '\n' +
        'Contributors\n'
        '============\n'
        + '\n' +
        open('CONTRIBUTORS.txt').read()
        + '\n' +
        open('CHANGES.txt').read()
        + '\n')

setup(name='policy.acjette',
        version=version,
        description="'policy of acjette site'",
        long_description=long_description,
        # Get more strings from
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            "Programming Language :: Python",
            ],
        keywords='',
        author='',
        author_email='',
        url='http://svn.plone.org/svn/collective/',
        license='gpl',
        packages=find_packages('src'),
        package_dir = {'': 'src'},
        namespace_packages=['policy', ],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'setuptools',
            'collective.ckeditor',
            'collective.plonefinder',
            'webcouturier.dropdownmenu',
            'Products.LinguaPlone',
            'collective.js.jqueryui',
            'collective.quickupload',
            'Products.PloneFormGen',
            'Solgema.ContextualContentMenu',
            'Solgema.fullcalendar',
            'collective.js.colorpicker',
            'collective.js.fullcalendar',
            'plone.app.jquerytools',
            'plone.app.theming',
            'plonetheme.acjette',
            'collective.easyslider',
            ],
        extras_require={'test': ['plone.app.testing']},
        entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
