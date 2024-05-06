#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name='holidays',
        version='0.48.1',
        description='Generate and work with holidays in Python',
        long_description= open('README.rst', encoding='utf-8').read(),
        author='Aziz Nechi',
        author_email='aziz.nechi@factset.com',
        url='https://github.com/anechii/python36-holidays/',
        packages= find_packages(include=["holidays*"]),
        install_requires=[
            'python-dateutil',
        ],
        keywords='holidays, calendar, l10n',
        python_requires='>=3.6',
    )
