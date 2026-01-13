# Style and Document

This action automatically styles and documents the R code in a package.

## Inputs

This action has no inputs.

## Example Usage

```yaml
jobs:
  style-and-document:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: ./style-and-document
```
