import os
from IPython.display import (
    display,
    Javascript,
)


def load_ipython_extension(ip):
    main_js = os.path.join(os.path.dirname(__file__),
                           "static",
                           "nb-mermaid",
                           "init.js")
    display(Javascript(filename=main_js))
