from setuptools import setup, find_packages
import os

version = '1.0'

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
          'CKeditor for Plone',
 	  'Collective Plone Finder',
          'Dropdown menu',
	  'LinguaPlone',
	  'Plone JQuery Integration',
          'Plone JQuery Tools Integration',
          'Plone Quick Upload',
	  'PloneFormGen',
	  'Solgema ContextualContentMenu',
	  'Solgema Fullcalendar',
	  'jQuery Color Picker',
	  'jQuery FullCalendar plugin',
	  'jQuery UI',
	  'Diazo theme support'
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
