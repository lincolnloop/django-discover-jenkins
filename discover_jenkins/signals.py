from django.dispatch import Signal

setup_test_environment = Signal()
teardown_test_environment = Signal()

before_suite_run = Signal()
after_suite_run = Signal()

test_failure = Signal(providing_args=['test', 'err'])
test_error = Signal(providing_args=['test', 'err'])
test_success = Signal(providing_args=['test'])
test_skip = Signal(providing_args=['test', 'reason'])
test_expected_failure = Signal(providing_args=['test', 'err'])
test_unexpected_success = Signal(providing_args=['test'])