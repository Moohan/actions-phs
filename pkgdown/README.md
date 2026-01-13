# Build and Deploy Pkgdown Site

This action builds and deploys a pkgdown site to GitHub Pages.

## Inputs

This action has no inputs.

## Example Usage

```yaml
jobs:
  pkgdown:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: ./pkgdown
```
