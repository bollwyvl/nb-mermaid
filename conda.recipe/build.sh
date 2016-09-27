bower install
npm install
npm run build
"${PYTHON}" setup.py install
"${PREFIX}/bin/jupyter-nbextension" install nb-mermaid --py --sys-prefix
