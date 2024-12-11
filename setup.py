from setuptools import setup, find_packages

setup(
    name='PDFpy',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'f2py'
    ],
    entry_points={
        'console_scripts': [
            'mi_comando=PDFpy.modulo1:calcula_algo',
        ],
    },
    author='Tu Nombre',
    author_email='guillermohdezb15@gmail.com',
    description='Una descripción breve de tu librería',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # url='https://github.com/tu_usuario/PDFpy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
