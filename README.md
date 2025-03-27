# sphinx-docs-template

A starter project for a Sphinx documentation template that includes support for internationalization (i18n) and version control using sphinx-multiversion.

## Project Structure

```plain text
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
```

## Running in virtual environment

environment: python3.13

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Writing Documentation

The documentation is written in reStructuredText (reST) format.

Source files are written in English, if you need to add other languages, such as Simple Chinese, you can execute the following command:

```bash
make gettext
sphinx-intl update -p ./_build/gettext -l zh_CN
```

After executing the command, the `zh_CN` language document will be generated in the `locales` directory. Modify the `*.po` file, add the content you need to translate, and then build the multi-language document according to the following method.

## Build documents

> No version and no multi-language documentation build method

When you need to quickly build a document just to check the content style, run `make html` in the current directory. This command is a simplified version of:

```bash
sphinx-build -b source html _build/html/zh
```

After executing the command, the static document will be generated in the `build/html` directory.

You can browse the document by opening `build/html/index.html` in your web browser.

> Multi-version and multi-language documentation build method

If you need to build a multi-version and multi-language document with content changes, **you need to commit the document locally** and **re-tag it as test**.

```bash
git tag -d test
git tag test -m "Test Version"
```

After that, you can use the following command:

```bash
sphinx-multiversion source/ _build/html/en -D language=en_US
sphinx-multiversion source/ _build/html/zh -D language=zh_CN
```

After executing the command, the document will be generated in the `build/html/en` and `build/html/zh` directory.

You need to know the document version build rule before building the document.

According to the configuration in `source/conf.py`, match all the tags in the current repository and build the multi-version document.

The version matching rule is based on the `smv_tag_whitelist` configuration in `conf.py`, such as `^\d+\.\d+\.\d+$|^latest$|^test$`, which matches the version number in the format of `1.0.0`, `latest`, and `test`.

You can view the Chinese version of the documentation by opening `build/html/zh/index.html` in your browser, and the English version by opening `build/html/en/index.html`
