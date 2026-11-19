import pytest

from sched import timing_wheel as mod

CASES = [
    ('slot_for', [100, 10, 8], 2, False),
    ('slot_for', [0, 10, 8], 0, False),
    ('add_timer', [{}, 'a', 25, 10, 8], {2: [['a', 25]]}, False),
    ('tick', [{2: [['a', 25]]}, 25, 10, 8], ['a'], False),
    ('tick', [{2: [['a', 35]]}, 25, 10, 8], [], False),
    ('cancel', [{2: [['a', 25], ['b', 45]]}, 'a'], {2: [['b', 45]]}, False),
    ('next_deadline', [{1: [['a', 15]], 2: [['b', 25]]}], 15, False),
    ('next_deadline', [{}], None, False),
    ('slot_for', [25, 10, 8], 2, False),
    ('slot_for', [80, 10, 8], 0, False),
    ('add_timer', [{}, 'b', 5, 10, 8], {0: [['b', 5]]}, False),
    ('tick', [{0: [['a', 5]]}, 5, 10, 8], ['a'], False),
    ('tick', [{0: [['a', 15]]}, 5, 10, 8], [], False),
    ('cancel', [{0: [['a', 5]]}, 'missing'], {0: [['a', 5]]}, False),
    ('next_deadline', [{0: [['a', 5]], 1: [['b', 15]]}], 5, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_timing_wheel_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
