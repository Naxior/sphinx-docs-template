Writing Documentation
---------------------------------------

The documentation is written in reStructuredText (reST) format.

Source files are written in English, if you need to add other languages, such as Simple Chinese, you can execute the following command:

.. code-block:: bash

    make gettext
    sphinx-intl update -p ./_build/gettext -l zh_CN

After executing the command, the `zh_CN` language document will be generated in the `locales` directory. Modify the `*.po` file, add the content you need to translate, and then build the multi-language document according to the following method.
