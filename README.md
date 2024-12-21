# Cucumber Environments Playground

A playground for [Cucumber](https://cucumber.io/) implementations across languages and frameworks.

## Getting Started

Launch the project within a codespace that is configured for running each of the frameworks without additional setup.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/kieran-ryan/cucumber-env-samples)

Use the [Task Runner](https://marketplace.visualstudio.com/items?itemName=SanaAjani.taskrunnercode) tab in the VSCode file explorer to run each framework.

### Running Locally

Running through the [devcontainer](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) is recommended when running locally. Though each framework can be installed and run independently.

#### [Behave](https://github.com/behave/behave)

Running Behave - a Python-based framework.

```console
cd behave_default
pip install --requirement requirements.txt
behave
```

##### [Behave with Cucumber](https://github.com/kieran-ryan/behave-cucumber-matcher)

Running Behave - a Python-based framework - with [Cucumber Expressions](https://github.com/cucumber/cucumber-expressions).

Cucumber Expressions are presently unsupported natively by common Python testing frameworks. The following example demonstrates how to integrate support into [behave](https://behave.readthedocs.io).

```console
cd behave_cucumber
pip install --requirement requirements.txt
behave
```

#### [Cucumber JavaScript](https://github.com/cucumber/cucumber-js)

Running Cucumber with JavaScript.

```console
cd cucumber_js
npm install
npx cucumber-js
```

#### [Cucumber Rust](https://github.com/cucumber-rs/cucumber)

Running Cucumber with Rust.

```console
cd cucumber_rs
cargo build
cargo test
```

#### [Godog](https://github.com/cucumber/godog)

Running Cucumber with Go.

```console
cd godog
go test -v godogs_test.go
```
