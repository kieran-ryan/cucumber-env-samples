# Cucumber Environment Samples

Sample Cucumber environments in different languages and frameworks.

## Behave

Cucumber Expressions are presently unsupported natively by common Python testing frameworks. The following example demonstrates how to integrate support into [behave](https://behave.readthedocs.io).

```console
cd behave_sample
pip install --requirement requirements.txt
behave
```

## Cucumber Rust

Install dependencies and execute the test.

```console
cd cucumber-rs
cargo build
cargo test --test example
```
