from setuptools import setup


setup(
    name='pytemplate',
    version='0.1',
    py_modules=['pytemplate'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pytemplate=pytemplate:create_python_template
    ''',
)
