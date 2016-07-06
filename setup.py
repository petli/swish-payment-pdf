#!/usr/bin/env python3

from setuptools import setup

setup(
    name = 'swish-payment-pdf',
    version = '1.0',
    license = 'MIT',
    description = 'Convert a CSV report of Swish payments into separate PDF files for accounting',
    author = 'Peter Liljenberg',
    author_email = 'peter.liljenberg@gmail.com',
    keywords = 'swish accounting',
    url = 'https://github.com/petli/swish-payment-pdf',

    scripts = [ 'swish2pdf' ],

    install_requires = [
        'fpdf >= 1.7, < 2',
    ]
)
