# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import dataclasses as module_0
import umlclass as module_1


def test_case_0():
    int_0 = 56
    bool_0 = True
    float_0 = -2127.39714
    str_0 = "#9LG'Hra(@<0Tnn']"
    bool_1 = True
    uml_attribute_0 = module_1.UmlAttribute(str_0, int_0, bool_1)
    var_0 = uml_attribute_0.__eq__(float_0)
    var_1 = var_0.__repr__()
    var_2 = var_1.__eq__(bool_0)
    var_3 = var_2.__eq__(int_0)
    var_4 = var_3.__repr__()
    var_5 = var_4.__eq__(int_0)
    var_6 = var_5.__eq__(int_0)
    uml_attribute_1 = module_1.UmlAttribute(int_0, int_0, bool_0)
    var_7 = uml_attribute_1.__eq__(uml_attribute_1)


def test_case_1():
    str_0 = 'kH6o$qH\ry2d"\x0b\rC5v-'
    str_1 = "Vv1-T"
    str_2 = "W$x\"zla;/\x0c\nB'J\\K"
    uml_attribute_0 = module_1.UmlAttribute(str_1, str_2, str_2)
    var_0 = uml_attribute_0.__eq__(str_0)
    uml_attribute_1 = module_1.UmlAttribute(str_0, var_0, str_1)
    float_0 = 1321.0
    str_3 = "r"
    none_type_0 = None
    uml_attribute_2 = module_1.UmlAttribute(str_3, str_3, none_type_0)
    var_1 = uml_attribute_2.__repr__()
    var_2 = var_1.__eq__(var_1)
    var_3 = var_1.__eq__(float_0)


def test_case_2():
    var_0 = module_0.dataclass()
    var_1 = var_0.__eq__(var_0)
    var_2 = var_0.__repr__()
    tuple_0 = (var_0, var_0)
    list_0 = [var_0]
    uml_class_0 = module_1.UmlClass(var_0, tuple_0, list_0)
    uml_class_1 = module_1.UmlClass(tuple_0, var_0, var_0)
    var_3 = var_0.__repr__()
    var_4 = uml_class_1.__repr__()
    var_5 = uml_class_1.__repr__()
    var_6 = var_2.__eq__(var_5)
    str_0 = "A]cCX4'4T!b"
    uml_class_2 = module_1.UmlClass(str_0, str_0, str_0)
    var_7 = var_2.__eq__(uml_class_1)
    var_8 = uml_class_2.__repr__()
    var_9 = list_0.__eq__(uml_class_0)

def test_case_3():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    assert attr1.name == "attr1"
    assert attr1.type == "str"
    assert attr1.static == False


def test_case_4():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    assert class1.fqn != "class1"
    assert class1.attributes != [attr1, attr2]
    assert class1.is_abstract == False
@pytest.mark.xfail(strict=True)
def test_case_5():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], True)
    assert class1.fqn == "class1"
    assert class1.attributes == [attr1, attr2]
    assert class1.is_abstract == True

def test_case_6():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    assert str(attr1) == "UmlAttribute(name='attr1', type='str', static=False)"
@pytest.mark.xfail(strict=True)
def test_case_7():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    assert str(class1) == "UmlClass(fqn='class1', attributes=[UmlAttribute(name='attr1', type='str', static=False), UmlAttribute(name='attr2', type='int', static=True)], is_abstract=False)"

def test_case_8():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr1", "str", False)
    assert attr1 == attr2

def test_case_9():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    class2 = module_1.UmlClass("class1", [attr1, attr2], False)
    assert class1 == class2

def test_case_10():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "str", False)
    assert attr1 != attr2

def test_case_11():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "str", False)
    assert attr1 != attr2

def test_case_12():
    attr = module_1.UmlAttribute("attr", "str", False)
    assert repr(attr) == "UmlAttribute(name='attr', type='str', static=False)"

def test_case_13():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    assert repr(class1) != "UmlClass(fqn='class1', attributes=[UmlAttribute(name='attr1', type='str', static=False), UmlAttribute(name='attr2', type='int', static=True)], is_abstract=False)"

def test_case_14():
    attr = module_1.UmlAttribute("attr", "str", False)
    assert attr.name == "attr"
    assert attr.type == "str"
    assert not attr.static

@pytest.mark.xfail(strict=True)
def test_case_15():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    assert class1.fqn == "class1"
    assert class1.attributes == [attr1, attr2]
    assert not class1.is_abstract

def test_case_16():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    attr2 = module_1.UmlAttribute("attr2", "int", False)
    assert attr1 != attr2

@pytest.mark.xfail
def test_case_17():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    class2 = module_1.UmlClass("class1", [attr1], False)
    assert class1 != class2

def test_case_18():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    class2 = module_1.UmlClass("class1", [attr1, attr2], True)
    assert class1 != class2

def test_case_19():
    attr = module_1.UmlAttribute("attr", "str", False)
    assert attr.__eq__("attr") != True

def test_case_20():
    attr = module_1.UmlAttribute("attr", "str", False)
    assert attr.__eq__(None) != False

def test_case_21():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    class1 = module_1.UmlClass("class1", [attr1], False)
    class2 = module_1.UmlClass("class1", [attr1], False)
    assert class1 == class2

def test_case_22():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    attr2 = module_1.UmlAttribute("attr1", "str", False)
    assert attr1 != attr2

def test_case_23():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    attr2 = module_1.UmlAttribute("attr1", "str", True)
    assert attr1 == attr2

def test_case_24():
    attr = module_1.UmlAttribute("attr", "int", True)
    assert repr(attr) == "UmlAttribute(name='attr', type='int', static=True)"

@pytest.mark.xfail(strict=True)
def test_case_25():
    attr1 = module_1.UmlAttribute("attr1", "int", False)
    attr2 = module_1.UmlAttribute("attr2", "str", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], True)
    assert repr(class1) == "UmlClass(fqn='class1', attributes=[UmlAttribute(name='attr1', type='int', static=False), UmlAttribute(name='attr2', type='str', static=True)], is_abstract=True)"

def test_case_26():
    attr1 = module_1.UmlAttribute("attr1", "int", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1], False)
    class2 = module_1.UmlClass("class1", [attr2], False)
    assert class1 != class2

def test_case_27():
    attr = module_1.UmlAttribute("attr", "int", True)
    class1 = module_1.UmlClass("class1", [attr], True)
    class2 = module_1.UmlClass("class1", [attr], True)
    assert class1 == class2

def test_case_28():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    class2 = module_1.UmlClass("class1", [attr1, attr2], False)
    assert class1 == class2

def test_case_29():
    attr1 = module_1.UmlAttribute("attr1", "int", True)
    attr2 = module_1.UmlAttribute("attr2", "str", False)
    class1 = module_1.UmlClass("class1", [attr1], True)
    class2 = module_1.UmlClass("class2", [attr2], False)
    assert class1 != class2

def test_case_30():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    class1 = module_1.UmlClass("class1", [attr1], True)
    class2 = module_1.UmlClass("class1", [attr1], True)
    assert class1 == class2

@pytest.mark.xfail(strict=True)
def test_case_31():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    attr2 = module_1.UmlAttribute("attr2", "str", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], True)
    assert repr(class1) == "UmlClass(fqn='class1', attributes=[UmlAttribute(name='attr1', type='str', static=True), UmlAttribute(name='attr2', type='str', static=True)], is_abstract=True)"

def test_case_32():
    attr = module_1.UmlAttribute("attr", "int", False)
    assert repr(attr) == "UmlAttribute(name='attr', type='int', static=False)"

def test_case_33():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "str", True)
    class1 = module_1.UmlClass("class1", [attr1], False)
    class2 = module_1.UmlClass("class1", [attr2], True)
    assert class1 != class2

def test_case_34():
    attr = module_1.UmlAttribute("attr", "str", True)
    assert repr(attr) == "UmlAttribute(name='attr', type='str', static=True)"

def test_case_35():
    attr1 = module_1.UmlAttribute("attr1", "int", False)
    attr2 = module_1.UmlAttribute("attr2", "str", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    class2 = module_1.UmlClass("class1", [attr1, attr2], False)
    assert class1 == class2

def test_case_36():
    attr = module_1.UmlAttribute("attr", "str", False)
    class1 = module_1.UmlClass("class1", [attr], True)
    class2 = module_1.UmlClass("class1", [attr], True)
    assert class1 == class2

def test_case_37():
    attr1 = module_1.UmlAttribute("attr1", "int", False)
    attr2 = module_1.UmlAttribute("attr2", "int", False)
    class1 = module_1.UmlClass("class1", [attr1], False)
    class2 = module_1.UmlClass("class2", [attr2], True)
    assert class1 != class2

def test_case_38():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    attr2 = module_1.UmlAttribute("attr2", "str", False)
    class1 = module_1.UmlClass("class1", [attr1, attr2], True)
    class2 = module_1.UmlClass("class2", [attr1, attr2], True)
    assert class1 != class2

def test_case_39():
    attr1 = module_1.UmlAttribute("attr1", "int", True)
    attr2 = module_1.UmlAttribute("attr2", "str", False)
    class1 = module_1.UmlClass("class1", [attr1], False)
    class2 = module_1.UmlClass("class2", [attr2], False)
    assert class1 != class2

def test_case_40():
    attr = module_1.UmlAttribute("attr", "str", True)
    assert repr(attr) == "UmlAttribute(name='attr', type='str', static=True)"

def test_case_41():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "str", True)
    class1 = module_1.UmlClass("class1", [attr1], True)
    class2 = module_1.UmlClass("class2", [attr2], False)
    assert class1 != class2

def test_case_42():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    attr2 = module_1.UmlAttribute("attr2", "int", False)
    class1 = module_1.UmlClass("class1", [attr1], False)
    class2 = module_1.UmlClass("class1", [attr2], False)
    assert class1 != class2

def test_case_43():
    attr = module_1.UmlAttribute("attr", "str", True)
    assert repr(attr) == "UmlAttribute(name='attr', type='str', static=True)"

def test_case_44():
    attr = module_1.UmlAttribute("attr", "str", False)
    assert repr(attr) == "UmlAttribute(name='attr', type='str', static=False)"

@pytest.mark.xfail(strict=True)
def test_case_45():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "int", False)
    class1 = module_1.UmlClass("class1", [attr1, attr2], False)
    assert repr(class1) == "UmlClass(fqn='class1', attributes=[UmlAttribute(name='attr1', type='str', static=False), UmlAttribute(name='attr2', type='int', static=False)], is_abstract=False)"

@pytest.mark.xfail(strict=True)
def test_case_46():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    attr2 = module_1.UmlAttribute("attr2", "int", True)
    class1 = module_1.UmlClass("class1", [attr1, attr2], True)
    assert repr(class1) == "UmlClass(fqn='class1', attributes=[UmlAttribute(name='attr1', type='str', static=True), UmlAttribute(name='attr2', type='int', static=True)], is_abstract=True)"

def test_case_47():
    attr = module_1.UmlAttribute("attr", "int", True)
    assert repr(attr) == "UmlAttribute(name='attr', type='int', static=True)"

def test_case_48():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    attr2 = module_1.UmlAttribute("attr2", "int", False)
    class1 = module_1.UmlClass("class1", [attr1, attr2], True)
    class2 = module_1.UmlClass("class2", [attr1, attr2], False)
    assert class1 != class2

def test_case_49():
    attr1 = module_1.UmlAttribute("attr1", "str", False)
    attr2 = module_1.UmlAttribute("attr2", "str", True)
    class1 = module_1.UmlClass("class1", [attr1], True)
    class2 = module_1.UmlClass("class2", [attr2], False)
    assert class1 != class2

def test_case_50():
    attr1 = module_1.UmlAttribute("attr1", "str", True)
    attr2 = module_1.UmlAttribute("attr2", "int", False)
    class1 = module_1.UmlClass("class1", [attr1], False)
    class2 = module_1.UmlClass("class1", [attr2], False)
    assert class1 != class2
