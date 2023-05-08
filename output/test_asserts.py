# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import asserts as module_0
import py2puml.py2puml as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "l4B.3\x0cw$?\x0bovGaeE"
    str_1 = "zz8E-t`\n,M$YP)\nkn%H&"
    bool_0 = False
    module_0.assert_py2puml_is_stringio(str_0, str_1, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.assert_py2puml_is_stringio(none_type_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "r"
    list_0 = [str_0]
    var_0 = module_0.assert_multilines(list_0, list_0)
    str_1 = "\n    Given a module and a partially namespaced type name, returns a tuple of information about the type:\n    - the full-namespaced type name, to draw relationships between types without ambiguity\n    - the short type name, for display purposes\n\n    Different approaches are combined to derive the type information:\n    - when the partially namespaced type is found during AST parsing (class constructors)\n    - when the partially namespaced type is found during class inspection (dataclasses, class static variables, named tuples, enums)\n\n    The two approaches are a bit entangled for now, they could be separated a bit more for performance sake.\n    "
    none_type_0 = None
    module_0.assert_multilines(none_type_0, str_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 0
    module_0.assert_py2puml_is_file_content(int_0, int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 0
    module_0.assert_py2puml_is_file_content(int_0, int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "l!V7',J)v1~"
    str_1 = '"Mpf+cx{#p%v.fuXZt&'
    module_0.assert_py2puml_is_stringio(str_1, str_0, str_0)


def test_case_6():
    list_0 = []
    with pytest.raises(AssertionError):
        module_0.assert_multilines(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "__annotations__"
    str_1 = "55f"
    module_0.assert_py2puml_is_stringio(str_1, str_1, str_0)


def test_case_8():
    str_0 = "]S,9):"
    str_1 = ", expected_line="
    list_0 = [str_0, str_1]
    iterable_0 = module_1.py2puml(str_1, str_0)
    with pytest.raises(AssertionError):
        module_0.assert_multilines(list_0, iterable_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    none_type_0 = None
    list_0 = []
    module_0.assert_multilines(list_0, none_type_0)


def test_case_10():
    str_0 = "9 \r0FJU6DP`=;1"
    list_0 = [str_0, str_0, str_0, str_0]
    with pytest.raises(AssertionError):
        module_0.assert_multilines(list_0, str_0)
