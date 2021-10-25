require {
  paths:
    "nb-mermaid": [
      # embedded, in notebook
      "/nbextensions/nb-mermaid/nb-mermaid"
      # embedded, published
      "https://bollwyvl.github.io/nb-mermaid/nb-mermaid"
    ]
}, [
  "nb-mermaid"
], (nbmermaid) ->
  nbmermaid()