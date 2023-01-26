"""Tests the Smartmeter class."""

import threading

from src.smartmeter_austria_energy.obisdata import (ObisDataEventArgs)
from src.smartmeter_austria_energy.supplier import (SUPPLIER_EVN_NAME)
from src.smartmeter_austria_energy.smartmeter import (Smartmeter)


def test_smartmeter_constructor():
    """Test the constructor of the smartmeter class with an empty port."""
    
    # arrange
    supplier_name = SUPPLIER_EVN_NAME
    key_hex_string = "some_hex"
    port = "COM5"

    # act
    my_smartmeter = Smartmeter(supplier_name, port, key_hex_string)
    
    # assert
    assert isinstance(my_smartmeter, Smartmeter)

def test_smartmeter_properties():
    """Test the constructor of the smartmeter class with an empty port."""
    
    # arrange
    supplier_name = SUPPLIER_EVN_NAME
    key_hex_string = "some_hex"
    port = "anyString"

    my_smartmeter = Smartmeter(supplier_name, port, key_hex_string)

    # act
    result_is_running = my_smartmeter.is_running
    
    # assert
    assert result_is_running == False

def test_smartmeter_close_method():
    """Test the constructor of the smartmeter class with an empty port."""
    
    # arrange
    supplier_name = SUPPLIER_EVN_NAME
    key_hex_string = "some_hex"
    port = "anyString"

    my_smartmeter = Smartmeter(supplier_name, port, key_hex_string)
    my_smartmeter._is_running = True

    # act
    my_smartmeter.close()
    
    # assert
    assert my_smartmeter.is_running == False


def test_smartmeter_has_empty_port():
    """Test the read method of the smartmeter class with an empty port."""
    event = threading.Event();
    
    # arrange
    def obisdata_changed(sender,  args):
        event.set()
        return
        
    supplier_name = SUPPLIER_EVN_NAME
    key_hex_string = "some_hex"
    port = ""

    # act
    my_smartmeter = Smartmeter(supplier_name, port, key_hex_string)
    my_smartmeter.start_reading()
    my_smartmeter.obisdata_changed += obisdata_changed
    
    result = event.wait(10)
    
    # assert
    assert result == False
