Sphinx Documentation Template
=======================================

A starter project for a Sphinx documentation template that includes support for internationalization (i18n) and version control using sphinx-multiversion.

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

.. raw:: html

   <div class="two-column">
      <div>
   </embed>

In this Document, you can set the icon |myicon| inline. This icon sets a maximum height of 24px so that the icon does not exceed the line height. If you need to modify it, please adjust it in the ``.default-inline-image`` class in ``source/_static/css/custom.css``.

.. |myicon| image:: _static/img/logo.png
   :class: default-inline-image

.. raw:: html

      </div>
      <div>
   </embed>

And you can also display the text content in two columns, like it is now.

.. raw:: html

      </div>
   </div>

.. toctree::
   :maxdepth: 2
   :caption: Contents

   01_project_structure.rst
   02_running_in_virtual_environment.rst
   03_writing_documentation.rst
   04_build_documents.rst