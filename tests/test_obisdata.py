from src.smartmeter_austria_energy.supplier import (SupplierTINETZ)
from src.smartmeter_austria_energy.obisdata import(ObisData)
from src.smartmeter_austria_energy.decrypt import(Decrypt)

def foo():
    """Test the Suppliers class."""
    # arrange
    # act
   
    # assert

def t_Obisdata_no_wanted_values():
    """Test the ObisObisDataValue class."""
    # arrange
    my_wanted_values: list[str] = []
    my_supplier = SupplierTINETZ()
    frame1 = ""
    frame2 = ""
    my_key_hex_string = ""
    
    my_decrypt = Decrypt(my_supplier, frame1, frame2, my_key_hex_string)
    
    # act
    my_obisdata = ObisData(dec=my_decrypt, wanted_values=my_wanted_values)
    
    # assert
