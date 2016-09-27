"%PYTHON%" setup.py install
"%PREFIX%\Scripts\jupyter-nbextension.exe" install nb-mermaid --py --sys-prefix
if errorlevel 1 exit 1
