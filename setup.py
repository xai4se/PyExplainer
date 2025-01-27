# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyexplainer']

package_data = \
{'': ['*'],
 'pyexplainer': ['css/*',
                 'default_data/*',
                 'dev_info/*',
                 'js/*',
                 'rf_models/*']}

install_requires = ['python>=3.8',
                    'ipywidgets>=7.6.3,<8.0.0',
                     'scikit-learn>=0.24.2',
                     'numpy>=1.20.1',
                     'pandas>=1.2.5',
                     'scikit-learn>=0.24.2',
                     'scipy>=1.6.1',
                     'statsmodels>=0.12.2',
                     'ipython>=7.21.0']

setup_kwargs = {
    'name': 'pyexplainer',
    'version': '1.1.0',
    'description': 'Explainable AI tool for Software Quality Assurance (SQA)',
    'long_description': None,
    'author': 'Michael',
    'author_email': 'michaelfu1998@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

