Project Structure
---------------------------------------

.. code::

    source/                   ---- Source code directory for documentation
        ├── conf.py               ---- Configuration file
        ├── index.rst             ---- Main page
        ├── _static               ---- Static files
        │   ├── img/           ---- Images
        │   ├── css/              ---- CSS
        │   └── js/               ---- JS
        └── _templates            ---- Template files
    locales/                ---- Language files
        └── zh_CN/              ---- Simple Chindese language files
    build/                  ---- Documentation build directory
        ├── html/               ---- Documentation build directory
        │   ├── en/             ---- English documentation build directory
        │   └── zh/             ---- Simple Chinese documentation build directory
        └── gettext/            ---- Translation documentation build directory
    .gitignore                ---- Ignore file
    requirements.txt          ---- Dependencies file
    Makefile                  ---- Makefile
    make.bat                  ---- Makefile script
    README.md                 ---- README file
