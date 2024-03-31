# Cucumber Environment Samples

Sample Cucumber environments in different languages and frameworks.

## Behave

Behave can be executed with its default non-cucumber matcher as below.

```console
cd behave_default
pip install --requirement requirements.txt
behave
```

### Behave with Cucumber

Cucumber Expressions are presently unsupported natively by common Python testing frameworks. The following example demonstrates how to integrate support into [behave](https://behave.readthedocs.io).

```console
cd behave_cucumber
pip install --requirement requirements.txt
behave
```

## Cucumber JavaScript

Install dependencies and execute the test.

```console
cd cucumber_js
npm install
npx cucumber-js
```

## Cucumber Rust

Install dependencies and execute the test.

```console
cd cucumber_rs
cargo build
cargo test --test example
```
