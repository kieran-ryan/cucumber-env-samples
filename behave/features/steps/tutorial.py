from behave import given, when, then


@given("we have {tool} installed")
def step_impl(context, tool):
    pass


@when("we implement a test")
def step_impl(context):
    assert True is not False


@then("{tool} will test it for us!")
def step_impl(context, tool):
    print(tool)
    assert context.failed is False
