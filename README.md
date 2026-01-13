# Public Health Scotland GitHub Workflows

<!-- badges: start -->
[![GitHub release (latest by
date)](https://img.shields.io/github/v/release/Public-Health-Scotland/actions)](https://github.com/Public-Health-Scotland/Public-Health-Scotland/actions/latest)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/Public-Health-Scotland/actions/badge)](https://scorecard.dev/viewer/?uri=github.com/Public-Health-Scotland/actions)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10780/badge)](https://www.bestpractices.dev/projects/10780)
[![CodeQL](https://github.com/Public-Health-Scotland/actions/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Public-Health-Scotland/actions/actions/workflows/github-code-scanning/codeql)
<!-- badges: end -->

## Description

This repository houses GitHub workflows for the Public Health Scotland (PHS) organisation. It centralises the management of workflows to ensure consistent Continuous Integration (CI) practices across PHS projects.

## Workflows

| Workflow | Description |
|---|---|
| [![phs-actions](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_package_checks.yaml/badge.svg)](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_package_checks.yaml) | This workflow ensures that R packages are checked, tested, and styled consistently. It runs a series of checks, including `R-CMD-check-core`, `test-coverage`, and `pkgdown`. |
| [![phs-actions](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_R-CMD-check-core.yaml/badge.svg)](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_R-CMD-check-core.yaml) | This workflow runs `R CMD check` on a package, which is a series of checks to ensure that the package is well-formed and follows R's standards. |
| [![phs-actions](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_test_coverage.yaml/badge.svg)](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_test_coverage.yaml) | This workflow checks the test coverage of a package, which is the percentage of the package's code that is covered by tests. |
| [![phs-actions](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_pkgdown.yaml/badge.svg)](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_pkgdown.yaml) | This workflow builds a `pkgdown` site for a package, which is a website that contains documentation for the package. |
| [![phs-actions](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_style_and_document.yaml/badge.svg)](https://github.com/Public-Health-Scotland/actions/actions/workflows/phs_style_and_document.yaml) | This workflow styles and documents a package, which includes running `styler` to format the code and `roxygen2` to generate documentation. |

## Usage

### `phs_package_checks.yaml`

This workflow runs a series of checks on an R package to ensure that it is well-formed and follows R's standards. It can be used in other repositories by creating a new workflow file (e.g., `.github/workflows/main.yaml`) and adding the following code:

```yaml
name: R Package Checks

on: [push]

jobs:
  package-checks:
    uses: Public-Health-Scotland/actions/.github/workflows/phs_package_checks.yaml@v1
```

#### Inputs

| Name | Description | Default |
|---|---|---|
| `limit_parallel` | Limit concurrent jobs in general and specifically limit `R-CMD-check` to 3 in parallel. | `false` |

#### Outputs

This workflow does not have any outputs.

### `phs_style_and_document.yaml`

This workflow styles and documents a package, which includes running `styler` to format the code and `roxygen2` to generate documentation. It can be used in other repositories by creating a new workflow file (e.g., `.github/workflows/main.yaml`) and adding the following code:

```yaml
name: Style and Document

on: [push]

jobs:
  style-and-document:
    uses: Public-Health-Scotland/actions/.github/workflows/phs_style_and_document.yaml@v1
```

#### Inputs

This workflow does not have any inputs.

#### Outputs

This workflow does not have any outputs.

### `phs_pkgdown.yaml`

This workflow builds a `pkgdown` site for a package, which is a website that contains documentation for the package. It can be used in other repositories by creating a new workflow file (e.g., `.github/workflows/main.yaml`) and adding the following code:

```yaml
name: Build pkgdown site

on: [push]

jobs:
  build-pkgdown:
    uses: Public-Health-Scotland/actions/.github/workflows/phs_pkgdown.yaml@v1
```

#### Inputs

This workflow does not have any inputs.

#### Outputs

This workflow does not have any outputs.

### `phs_test_coverage.yaml`

This workflow checks the test coverage of a package, which is the percentage of the package's code that is covered by tests. It can be used in other repositories by creating a new workflow file (e.g., `.github/workflows/main.yaml`) and adding the following code:

```yaml
name: Test Coverage

on: [push]

jobs:
  test-coverage:
    uses: Public-Health-Scotland/actions/.github/workflows/phs_test_coverage.yaml@v1
```

#### Inputs

This workflow does not have any inputs.

#### Outputs

This workflow does not have any outputs.

### `phs_R-CMD-check-core.yaml`

This workflow runs `R CMD check` on a package, which is a series of checks to ensure that the package is well-formed and follows R's standards. It can be used in other repositories by creating a new workflow file (e.g., `.github/workflows/main.yaml`) and adding the following code:

```yaml
name: R CMD Check Core

on: [push]

jobs:
  r-cmd-check-core:
    uses: Public-Health-Scotland/actions/.github/workflows/phs_R-CMD-check-core.yaml@v1
```

#### Inputs

This workflow does not have any inputs.

#### Outputs

This workflow does not have any outputs.

## Releases and Tags

It is recommended to use the `v1` tag to ensure you are using the latest stable release of the actions. For example:

```yaml
uses: Public-Health-Scotland/actions/.github/workflows/phs_package_checks.yaml@v1
```

## Contributing

We welcome contributions to this repository. Please follow these steps to contribute:

1. **Fork the Repository:** Click the “Fork” button at the top right of the repository page to create a copy of the repository in your GitHub account.
2. **Create a New Branch:** Navigate to your forked repository and click the “Branch” dropdown. Type a new branch name (e.g., `feature-branch`) and click “Create branch”.
3. **Make Your Changes:** Use the GitHub web interface or clone the repository to your local machine to make your changes.
4. **Commit Your Changes:** If using the web interface, navigate to the file you modified, click the “Commit changes” button, and provide a commit message (e.g., `Add some feature`). If using a local clone, commit your changes and push them to your forked repository.
5. **Open a Pull Request:** Go to the original repository and click the “Pull requests” tab. Click the “New pull request” button, select your branch, and click “Create pull request”. Provide a title and description for your pull request.

### Development

To get started with development, you will need to have [R](https://www.r-project.org/) and [RStudio](https://www.rstudio.com/) installed.

### Testing

To run the tests for this repository, you can use the `devtools::test()` function.

### Style Guide

This repository follows the [Tidyverse style guide](https://style.tidyverse.org/). Please ensure that your code adheres to this style guide before submitting a pull request.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for everyone. Please read our [Code of Conduct](https://github.com/Public-Health-Scotland/actions/blob/main/CODE_OF_CONDUCT.md) before contributing.
