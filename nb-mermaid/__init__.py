from ._version import version_info, __version__

def _jupyter_nbextension_paths():
  return [dict(section="notebook",
               src="static/nb-mermaid",
               dest="nb-mermaid",
               require="nb-mermaid/init")]
