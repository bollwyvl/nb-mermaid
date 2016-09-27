"${PYTHON}" setup.py install
"${PREFIX}/bin/jupyter-nbextension" install nb-mermaid --py --sys-prefix
