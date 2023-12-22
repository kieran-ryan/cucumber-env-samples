from behave import given, then, when
from behave.matchers import matcher_mapping
from cucumber_expressions.parameter_type import ParameterType

# Define the parameter type
color = ParameterType(
    name="color",
    regexp="red|blue|yellow",
    type=str,
    transformer=lambda s: s,
    use_for_snippets=True,
    prefer_for_regexp_match=False,
)

# Pass the parameter type to the registry instance
matcher = matcher_mapping["cucumber_expressions"](None, "")
parameter_registry = matcher.parameter_type_registry
parameter_registry.define_parameter_type(color)


@given("I am on the profile customization page")
def step_given(context):
    assert True


# Reference the parameter type in the step definition pattern
@when('I select the color "{color}"')
def step_when(context, color):
    assert color
    context.selected_color = color


@then('the profile color should change to "{color}"')
def step_then(context, color):
    assert color
    assert context.selected_color == color
