# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import asserts as module_0
import _io as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ": it needs to be imported explicitely."
    str_1 = "id"
    list_0 = [str_0, str_0, str_0, str_1]
    var_0 = module_0.assert_multilines(list_0, list_0)
    i_o_base_0 = module_1._IOBase()
    module_0.assert_multilines(var_0, i_o_base_0)


def test_case_1():
    str_0 = "G<7Bk!"
    str_1 = '"'
    str_2 = 'qiY\na|xf/("Yr|[a;g'
    list_0 = [str_0, str_1, str_2]
    with pytest.raises(AssertionError):
        module_0.assert_multilines(list_0, str_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\\d^(8u=}"
    module_0.assert_py2puml_is_file_content(str_0, str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Mm5Hi"
    str_1 = "%HdqQe9]r79"
    module_0.assert_py2puml_is_file_content(str_1, str_0, str_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    module_0.assert_py2puml_is_file_content(bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = False
    module_0.assert_py2puml_is_file_content(bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "mY[DA4E}7x)0#$IjuV\\"
    str_1 = 'q[\x0c[#e"$'
    module_0.assert_py2puml_is_file_content(str_0, str_1, str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "gIN3,\r,6]rpbwP PC"
    none_type_0 = None
    module_0.assert_py2puml_is_stringio(none_type_0, str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    int_0 = 0
    module_0.assert_multilines(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = '@startuml SFUuo"\n'
    string_i_o_0 = module_1.StringIO()
    module_0.assert_py2puml_is_stringio(str_0, str_0, string_i_o_0)
