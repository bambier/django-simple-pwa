from setuptools import setup


with open("README.rst", "r+", encoding="UTF-8") as file:
    readme = file.read()


setup(
    name='django-simple-pwa',
    description="A simple Django app to develope and deploy a Progressive Web Application (PWA).",
    long_description=readme,
    long_description_content_type='text/markdown',
    version='3.0.0',
    platforms='ALL',
    license='MIT',
    extras_require={
        'django': ['django>=4.2']
    },
    author='Nima Esmaeili',
    author_email='nimpel2@proton.me',
    maintainer='Nima Esmaeili',
    maintainer_email='nimpel2@proton.me',
    package_dir={'': ''},
    include_package_data=True,
    keywords='django pwa django-simple-pwa',
    project_urls={
        "GitHub":'https://github.com/bambier/django-simple-pwa/',
        "Documents": 'https://github.com/bambier/django-simple-pwa',
    }
    options=[
        "include_package_data = true",
        "packages = find:",
        "python_requires = >=3.8",
        "install_requires =",
        "Django >= 3.7",
    ]
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content ",
    ],
)
