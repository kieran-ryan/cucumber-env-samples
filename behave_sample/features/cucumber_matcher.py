from behave.matchers import Matcher
from behave.model_core import Argument
from cucumber_expressions.expression import CucumberExpression


class CucumberExpressionMatcher(Matcher):

    def __init__(
        self,
        func,
        pattern,
        step_type= None,
        parameter_type_registry = None,
    ):
        super().__init__(func, pattern, step_type)
        self.func = func
        self.pattern = pattern
        self.parameter_type_registry = parameter_type_registry
        self.__cucumber_expression_ = CucumberExpression(
            pattern, self.parameter_type_registry
        )

    def check_match(self, step):
        result = self.__cucumber_expression_.match(step)
        if result is None:
            return None
        return [
            Argument(x.group.start, x.group.end, str(x.value), x.value)
            for x in result
        ]

    @property
    def regex_pattern(self):
        self.__cucumber_expression_.regexp


def build_step_matcher(parameter_type_registry):
    def step_matcher(func, pattern):
        return CucumberExpressionMatcher(
            func,
            pattern,
            parameter_type_registry=parameter_type_registry
        )
    return step_matcher
