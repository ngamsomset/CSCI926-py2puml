# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import inspectpackage as module_0
import pkgutil as module_1
import py2puml.inspection.inspectmodule as module_2
import py2puml.domain.umlitem as module_3


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = {bool_0}
    str_0 = "_&T68E6/iW"
    bool_1 = True
    none_type_0 = None
    module_0.inspect_package(set_0, str_0, bool_1, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Xo9O{"
    str_1 = "+\x0c#\"NZ'V5nk"
    bool_0 = True
    str_2 = ""
    bool_1 = True
    var_0 = module_1.walk_packages(prefix=bool_1, onerror=str_0)
    dict_0 = {str_2: var_0}
    var_1 = module_2.inspect_module(bool_0, str_1, dict_0, var_0)
    list_0 = [var_1]
    str_3 = "2P`3ap\t@M3K\x0cB7,y"
    var_2 = module_0.inspect_package(str_3, var_0, var_0, list_0)
    str_4 = "\t|7b"
    module_0.inspect_package(str_2, str_4, str_1, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    dict_0 = {}
    list_0 = []
    module_0.inspect_package(none_type_0, none_type_0, dict_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0]
    str_0 = "0]v}/Ug"
    var_0 = module_0.inspect_package(str_0, list_0, list_0, bool_0)
    var_1 = var_0.__eq__(bool_0)
    var_2 = var_1.__repr__()
    module_0.inspect_package(var_1, var_2, var_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "3"
    str_1 = ", expected_line="
    float_0 = -3253.58965
    var_0 = module_2.inspect_module(float_0, str_1, str_0, str_0)
    var_1 = var_0.__eq__(str_1)
    var_2 = var_1.__repr__()
    var_3 = var_2.__repr__()
    var_4 = var_3.__eq__(str_0)
    uml_item_0 = module_3.UmlItem(var_4, var_0)
    var_5 = uml_item_0.__eq__(str_1)
    var_6 = var_4.__eq__(var_1)
    dict_0 = {str_1: var_5, var_3: var_2}
    var_7 = module_0.inspect_package(str_0, str_0, dict_0, var_1)
    none_type_0 = None
    str_2 = "q*0%f"
    str_3 = "\n    Adds the definitions:\n    - of the inspected type\n    - of its static attributes from the class annotations (type and relation)\n    "
    var_8 = module_0.inspect_package(str_2, str_3, var_4, var_1)
    module_0.inspect_package(none_type_0, none_type_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    dict_0 = {}
    module_0.inspect_package(none_type_0, none_type_0, dict_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    tuple_0 = ()
    str_0 = '#w""o62y-d5%Li'
    str_1 = "eb"
    uml_item_0 = module_3.UmlItem(str_1, tuple_0)
    dict_0 = {str_0: uml_item_0, str_0: uml_item_0}
    module_0.inspect_package(tuple_0, tuple_0, dict_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    none_type_0 = None
    str_0 = ""
    module_0.inspect_package(str_0, none_type_0, none_type_0, none_type_0)
