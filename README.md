
# [nb-mermaid](https://bollwyvl.github.io/nb-mermaid)
> Make [mermaid](https://github.com/knsv/mermaid) diagrams in your
[Jupyter](http://jupyter.org) Notebook Markdown

## install (easy)
```shell
pip install nb-mermaid
```

In the notebook...
```javascript
%reload_ext mermaid
```


## install (less easy)
```shell
git clone -b gh-pages https://github.com/bollwyvl/nb-mermaid.git \
    ~/.ipython/nbextensions/nb-mermaid
```


## activate
In the notebook...
```javascript
%%javascript
IPython.load_ipython_extensions(["nb-mermaid/nb-mermaid"]);
```


## roadmap
- nbviewer support (bookmarklet works now!)
- live editing (a la the [mermaid editor](http://knsv.github.io/mermaid/live_editor))
- pan/zoom
- search

