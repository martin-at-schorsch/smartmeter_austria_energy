import pytest
from src.smartmeter_austria_energy.exceptions import (SmartmeterSerialException)
from src.smartmeter_austria_energy.supplier import (SUPPLIER_EVN_NAME)
from src.smartmeter_austria_energy.smartmeter import (Smartmeter)


def test_smartmeter_has_empty_port():
    supplier_name = SUPPLIER_EVN_NAME
    key_hex_string = "some_hex"
    port = ""

    my_smartmeter = Smartmeter(supplier_name, port, key_hex_string)
    with pytest.raises(SmartmeterSerialException):
        my_smartmeter.read()
