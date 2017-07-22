from setuptools import Extension, setup
from Cython.Build import cythonize


paq_ext = Extension(
    name="paq._paq",
    sources=["paq/_paq.pyx"],
    include_dirs=['paq'],
    extra_compile_args=['-O3'],
    language='c++',
)


setup(name='paq',
      version='0.1.1',
      description='Python binding for paq9a',
      author='Jingchao Hu',
      author_email='jingchaohu@gmail.com',
      url='http://github.com/observerss/paq',
      packages=['paq'],
      package_data={'paq': ['*.pyx', '*.h']},
      include_package_data=True,
      install_requires=['cython'],
      python_requires='>=3.5',
      ext_modules=cythonize([paq_ext]),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Topic :: System :: Archiving :: Compression',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ]
      )
