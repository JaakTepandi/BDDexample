# ----------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ----------------------------------------------------------------------------
from behave import register_type

def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return float(text)
# -- REGISTER: User-defined type converter (parse_type).
register_type(Number=parse_number)

# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, equal_to
from atm import ATM

@given('I have a Platinum account and am withdrawing cash from an ATM')
def step_impl(context):
    context.atm = ATM()

@when('I have "{x:Number}" on my account and want to withdraw "{y:Number}"')
def step_impl(context, x, y):
    assert isinstance(x, float)
    assert isinstance(y, float)
    context.atm.cash(x, y)

@then('the atm returns "{expected:Number}"')
def step_impl(context, expected):
    assert isinstance(expected, float)
    assert_that(context.atm.result, equal_to(expected))
