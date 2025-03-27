Build documents
---------------------------------------

**No version and no multi-language documentation build method**

When you need to quickly build a document just to check the content style, run ``make html`` in the current directory. This command is a simplified version of:

.. code-block:: bash

    sphinx-build -b source html _build/html/zh

After executing the command, the static document will be generated in the ``build/html`` directory.

You can browse the document by opening ``build/html/index.html`` in your web browser.

**Multi-version and multi-language documentation build method**

If you need to build a multi-version and multi-language document with content changes, **you need to commit the document locally** and **re-tag it as test**. 

.. code-block:: bash
    :linenos:
    :emphasize-lines: 2

    git tag -d test
    git tag test -m "Test Version"

After that, you can use the following command:

.. code-block:: bash

    sphinx-multiversion source/ _build/html/en -D language=en_US
    sphinx-multiversion source/ _build/html/zh -D language=zh_CN


After executing the command, the document will be generated in the ``build/html/en`` and ``build/html/zh`` directory.

You need to know the document version build rule before building the document.

According to the configuration in ``source/conf.py``, match all the tags in the current repository and build the multi-version document.

The version matching rule is based on the ``smv_tag_whitelist`` configuration in ``conf.py``, such as ``^\d+\.\d+\.\d+$|^latest$|^test$``, which matches the version number in the format of ``1.0.0``, ``latest``, and ``test``.

You can view the Chinese version of the documentation by opening ``build/html/zh/index.html`` in your browser, and the English version by opening ``build/html/en/index.html``
