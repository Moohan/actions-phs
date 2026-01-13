# Extended R CMD Check

This action runs an extended set of R CMD checks for a package on a specific OS and R version.

## Inputs

- `r-version`: The R version to use. (Required)
- `http-user-agent`: The HTTP user agent to use for `setup-r`. (Optional)

## Example Usage

```yaml
jobs:
  R-CMD-check-extended:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: ./R-CMD-check-extended
        with:
          r-version: 'release'
```
