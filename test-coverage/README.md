# Test Coverage

This action generates and uploads a test coverage report.

## Inputs

- `codecov-token`: The Codecov token. (Optional)

## Example Usage

```yaml
jobs:
  test-coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: ./test-coverage
        with:
          codecov-token: ${{ secrets.CODECOV_TOKEN }}
```
