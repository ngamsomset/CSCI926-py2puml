# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import inspectnamedtuple as module_0
import builtins as module_1
import py2puml.domain.umlclass as module_2


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    str_0 = ""
    module_0.inspect_namedtuple_type(none_type_0, str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    type_0 = module_1.list
    str_0 = ""
    str_1 = "^b^"
    module_0.inspect_namedtuple_type(str_1, str_0, type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    type_0 = module_1.list
    none_type_0 = None
    module_0.inspect_namedtuple_type(type_0, none_type_0, type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    str_0 = "F*>F8eN"
    str_1 = "J.8vGKKS1G~d2ZY4!SJW"
    set_0 = {str_0}
    uml_class_0 = module_2.UmlClass(str_1, none_type_0, none_type_0, str_1)
    var_0 = uml_class_0.__eq__(set_0)
    var_1 = var_0.__repr__()
    var_2 = var_1.__eq__(str_0)
    dict_0 = {str_1: var_2, var_1: uml_class_0}
    module_0.inspect_namedtuple_type(none_type_0, str_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xb9\xd4\x9b\xe0\xfc\x14\x10\xa1G\xd2k@'"
    none_type_0 = None
    module_0.inspect_namedtuple_type(bytes_0, bytes_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    type_0 = module_1.int
    str_0 = "0e}lf(\n\x0c\\\\}/"
    str_1 = "!N.L&-\n"
    str_2 = "~d[!UTytW&@T%VC(s^"
    none_type_0 = None
    uml_class_0 = module_2.UmlClass(str_1, str_2, none_type_0, str_0)
    str_3 = "'\t,)0*\\Us"
    str_4 = "B"
    str_5 = "^j&{zietc9k+w"
    uml_class_1 = module_2.UmlClass(none_type_0, str_5, str_5)
    dict_0 = {
        str_1: uml_class_0,
        str_3: uml_class_0,
        str_0: uml_class_0,
        str_4: uml_class_1,
    }
    module_0.inspect_namedtuple_type(type_0, str_0, dict_0)
