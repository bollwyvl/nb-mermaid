
`nb-mermaid <https://bollwyvl.github.io/nb-mermaid>`__
======================================================

    Make `mermaid <https://github.com/knsv/mermaid>`__ diagrams in your
    `Jupyter <http://jupyter.org>`__ Notebook Markdown

install (easy)
--------------

.. code:: shell

    pip install nb-mermaid

In the notebook...

.. code:: javascript

    %reload_ext mermaid

install (less easy)
-------------------

.. code:: shell

    git clone -b gh-pages https://github.com/bollwyvl/nb-mermaid.git \
        ~/.ipython/nbextensions/nb-mermaid

activate
--------

In the notebook...

.. code:: javascript

    %%javascript
    IPython.load_ipython_extensions(["nb-mermaid/nb-mermaid"]);

roadmap
-------

-  nbviewer support (bookmarklet works now!)
-  live editing (a la the `mermaid
   editor <http://knsv.github.io/mermaid/live_editor>`__)
-  pan/zoom
-  search
