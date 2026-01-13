# Core R CMD Check

This action runs the core set of R CMD checks for a package.

## Inputs

This action has no inputs.

## Example Usage

```yaml
jobs:
  R-CMD-check-core:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: ./R-CMD-check-core
```
