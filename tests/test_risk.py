from trader.risk import position_size

def test_position_size_is_capped_by_cash():
    assert position_size(1000, 100, 0.01, 0.02) <= 10

def test_invalid_inputs_return_zero():
    assert position_size(0, 100, 0.01, 0.02) == 0
