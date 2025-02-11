# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import puml as module_0
import builtins as module_1
import py2puml.domain.umlclass as module_2
import py2puml.domain.umlitem as module_3
import py2puml.domain.umlenum as module_4
import py2puml.domain.umlrelation as module_5

def test_case_0():
    tuple_0 = ()
    iterable_0 = module_0.to_puml_content(tuple_0, tuple_0, tuple_0)
    assert module_0.PUML_FILE_START == "@startuml {diagram_name}\n"
    assert module_0.PUML_FILE_FOOTER == "footer Generated by //py2puml//\n"
    assert module_0.PUML_FILE_END == "@enduml\n"
    assert module_0.PUML_ITEM_START_TPL == "{item_type} {item_fqn} {{\n"
    assert module_0.PUML_ATTR_TPL == "  {attr_name}: {attr_type}{staticity}\n"
    assert module_0.PUML_ITEM_END == "}\n"
    assert module_0.PUML_RELATION_TPL == "{source_fqn} {rel_type}-- {target_fqn}\n"
    assert module_0.FEATURE_STATIC == " {static}"
    assert module_0.FEATURE_INSTANCE == ""


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "k|+\roh77[9O"
    list_0 = []
    iterable_0 = module_0.to_puml_content(str_0, list_0, str_0)
    assert module_0.PUML_FILE_START == "@startuml {diagram_name}\n"
    assert module_0.PUML_FILE_FOOTER == "footer Generated by //py2puml//\n"
    assert module_0.PUML_FILE_END == "@enduml\n"
    assert module_0.PUML_ITEM_START_TPL == "{item_type} {item_fqn} {{\n"
    assert module_0.PUML_ATTR_TPL == "  {attr_name}: {attr_type}{staticity}\n"
    assert module_0.PUML_ITEM_END == "}\n"
    assert module_0.PUML_RELATION_TPL == "{source_fqn} {rel_type}-- {target_fqn}\n"
    assert module_0.FEATURE_STATIC == " {static}"
    assert module_0.FEATURE_INSTANCE == ""
    module_1.object(*iterable_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    iterable_0 = module_0.to_puml_content(list_0, list_0, list_0)
    assert module_0.PUML_FILE_START == "@startuml {diagram_name}\n"
    assert module_0.PUML_FILE_FOOTER == "footer Generated by //py2puml//\n"
    assert module_0.PUML_FILE_END == "@enduml\n"
    assert module_0.PUML_ITEM_START_TPL == "{item_type} {item_fqn} {{\n"
    assert module_0.PUML_ATTR_TPL == "  {attr_name}: {attr_type}{staticity}\n"
    assert module_0.PUML_ITEM_END == "}\n"
    assert module_0.PUML_RELATION_TPL == "{source_fqn} {rel_type}-- {target_fqn}\n"
    assert module_0.FEATURE_STATIC == " {static}"
    assert module_0.FEATURE_INSTANCE == ""
    module_1.object(*iterable_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "T|+Qoh7aE7[FO"
    uml_class_0 = module_2.UmlClass(str_0, str_0, str_0)
    list_0 = [uml_class_0]
    iterable_0 = module_0.to_puml_content(str_0, list_0, str_0)
    assert module_0.PUML_FILE_START == "@startuml {diagram_name}\n"
    assert module_0.PUML_FILE_FOOTER == "footer Generated by //py2puml//\n"
    assert module_0.PUML_FILE_END == "@enduml\n"
    assert module_0.PUML_ITEM_START_TPL == "{item_type} {item_fqn} {{\n"
    assert module_0.PUML_ATTR_TPL == "  {attr_name}: {attr_type}{staticity}\n"
    assert module_0.PUML_ITEM_END == "}\n"
    assert module_0.PUML_RELATION_TPL == "{source_fqn} {rel_type}-- {target_fqn}\n"
    assert module_0.FEATURE_STATIC == " {static}"
    assert module_0.FEATURE_INSTANCE == ""
    module_1.object(*iterable_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "k|+\roh77[9O"
    uml_item_0 = module_3.UmlItem(str_0, str_0)
    list_0 = [uml_item_0]
    iterable_0 = module_0.to_puml_content(str_0, list_0, str_0)
    assert module_0.PUML_FILE_START == "@startuml {diagram_name}\n"
    assert module_0.PUML_FILE_FOOTER == "footer Generated by //py2puml//\n"
    assert module_0.PUML_FILE_END == "@enduml\n"
    assert module_0.PUML_ITEM_START_TPL == "{item_type} {item_fqn} {{\n"
    assert module_0.PUML_ATTR_TPL == "  {attr_name}: {attr_type}{staticity}\n"
    assert module_0.PUML_ITEM_END == "}\n"
    assert module_0.PUML_RELATION_TPL == "{source_fqn} {rel_type}-- {target_fqn}\n"
    assert module_0.FEATURE_STATIC == " {static}"
    assert module_0.FEATURE_INSTANCE == ""
    module_1.object(*iterable_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "VEwp"
    uml_enum_0 = module_4.UmlEnum(str_0, str_0, str_0)
    list_0 = [uml_enum_0]
    iterable_0 = module_0.to_puml_content(str_0, list_0, str_0)
    assert module_0.PUML_FILE_START == "@startuml {diagram_name}\n"
    assert module_0.PUML_FILE_FOOTER == "footer Generated by //py2puml//\n"
    assert module_0.PUML_FILE_END == "@enduml\n"
    assert module_0.PUML_ITEM_START_TPL == "{item_type} {item_fqn} {{\n"
    assert module_0.PUML_ATTR_TPL == "  {attr_name}: {attr_type}{staticity}\n"
    assert module_0.PUML_ITEM_END == "}\n"
    assert module_0.PUML_RELATION_TPL == "{source_fqn} {rel_type}-- {target_fqn}\n"
    assert module_0.FEATURE_STATIC == " {static}"
    assert module_0.FEATURE_INSTANCE == ""
    module_1.object(*iterable_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "h"
    uml_class_0 = module_2.UmlClass(str_0, str_0, str_0, str_0)
    list_0 = [uml_class_0]
    iterable_0 = module_0.to_puml_content(str_0, list_0, str_0)
    assert module_0.PUML_FILE_START == "@startuml {diagram_name}\n"
    assert module_0.PUML_FILE_FOOTER == "footer Generated by //py2puml//\n"
    assert module_0.PUML_FILE_END == "@enduml\n"
    assert module_0.PUML_ITEM_START_TPL == "{item_type} {item_fqn} {{\n"
    assert module_0.PUML_ATTR_TPL == "  {attr_name}: {attr_type}{staticity}\n"
    assert module_0.PUML_ITEM_END == "}\n"
    assert module_0.PUML_RELATION_TPL == "{source_fqn} {rel_type}-- {target_fqn}\n"
    assert module_0.FEATURE_STATIC == " {static}"
    assert module_0.FEATURE_INSTANCE == ""
    module_1.object(*iterable_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = ""
    uml_class_0 = module_2.UmlClass(str_0, str_0, str_0)
    list_0 = [uml_class_0]
    iterable_0 = module_0.to_puml_content(str_0, list_0, str_0)
    assert module_0.PUML_FILE_START == "@startuml {diagram_name}\n"
    assert module_0.PUML_FILE_FOOTER == "footer Generated by //py2puml//\n"
    assert module_0.PUML_FILE_END == "@enduml\n"
    assert module_0.PUML_ITEM_START_TPL == "{item_type} {item_fqn} {{\n"
    assert module_0.PUML_ATTR_TPL == "  {attr_name}: {attr_type}{staticity}\n"
    assert module_0.PUML_ITEM_END == "}\n"
    assert module_0.PUML_RELATION_TPL == "{source_fqn} {rel_type}-- {target_fqn}\n"
    assert module_0.FEATURE_STATIC == " {static}"
    assert module_0.FEATURE_INSTANCE == ""
    module_1.object(*iterable_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = ""
    uml_enum_0 = module_4.UmlEnum(str_0, str_0, str_0)
    list_0 = [uml_enum_0]
    iterable_0 = module_0.to_puml_content(str_0, list_0, str_0)
    assert module_0.PUML_FILE_START == "@startuml {diagram_name}\n"
    assert module_0.PUML_FILE_FOOTER == "footer Generated by //py2puml//\n"
    assert module_0.PUML_FILE_END == "@enduml\n"
    assert module_0.PUML_ITEM_START_TPL == "{item_type} {item_fqn} {{\n"
    assert module_0.PUML_ATTR_TPL == "  {attr_name}: {attr_type}{staticity}\n"
    assert module_0.PUML_ITEM_END == "}\n"
    assert module_0.PUML_RELATION_TPL == "{source_fqn} {rel_type}-- {target_fqn}\n"
    assert module_0.FEATURE_STATIC == " {static}"
    assert module_0.FEATURE_INSTANCE == ""
    module_1.object(*iterable_0)

@pytest.mark.xfail(strict=True)
def test_case_9():
    with pytest.raises(TypeError):
        module_0.to_puml_content(123, [], [])

@pytest.mark.xfail(strict=True)
def test_case_10():
    with pytest.raises(TypeError):
        module_0.to_puml_content("diagram", [123], [])

@pytest.mark.xfail(strict=True)
def test_case_11():
    with pytest.raises(TypeError):
        module_0.to_puml_content("diagram", [], [123])

@pytest.mark.xfail(strict=True)
def test_case_12():
    uml_class_0 = module_2.UmlClass(123, "name", "module")
    with pytest.raises(TypeError):
        module_0.to_puml_content("diagram", [uml_class_0], [])

@pytest.mark.xfail(strict=True)
def test_case_13():
    uml_enum_0 = module_4.UmlEnum(123, "name", "module")
    with pytest.raises(TypeError):
        module_0.to_puml_content("diagram", [uml_enum_0], [])

@pytest.mark.xfail(strict=True)
def test_case_14():
    uml_class_0 = module_2.UmlClass("fqn", 123, "module")
    with pytest.raises(TypeError):
        module_0.to_puml_content("diagram", [uml_class_0], [])

@pytest.mark.xfail(strict=True)
def test_case_15():
    uml_enum_0 = module_4.UmlEnum("fqn", 123, "module")
    with pytest.raises(TypeError):
        module_0.to_puml_content("diagram", [uml_enum_0], [])

@pytest.mark.xfail(strict=True)
def test_case_16():
    uml_class_0 = module_2.UmlClass("fqn", "name", 123)
    with pytest.raises(TypeError):
        module_0.to_puml_content("diagram", [uml_class_0], [])

@pytest.mark.xfail(strict=True)
def test_case_17():
    uml_enum_0 = module_4.UmlEnum("fqn", "name", 123)
    with pytest.raises(TypeError):
        module_0.to_puml_content("diagram", [uml_enum_0], [])


def test_case_18():
    uml_class_0 = module_2.UmlClass("fqn", "name", "module", 123)
    module_0.to_puml_content("diagram", [uml_class_0], [])


@pytest.mark.xfail(strict=True)
def test_case_19():
    # Create instances of UmlClass for the test
    uml_class = module_2.UmlClass("module.Class1", "Class1", "module")
    uml_class2 = module_2.UmlClass("module.Class2", "Class2", "module")
    uml_items = [uml_class, uml_class2]

    # Create an instance of UmlRelation for the test
    uml_relation = module_5.UmlRelation(uml_class.fqn, uml_class2.fqn, uml_class2.fqn)
    uml_relations = [uml_relation]

    output = list(module_0.to_puml_content("TestDiagram", uml_items, uml_relations))

    # Make assertions about the output
    assert output[0] == "@startuml TestDiagram\n"
    assert output[1] == "class module.Class1 {\n"
    assert output[2] == "}\n"
    assert output[3] == "class module.Class2 {\n"
    assert output[4] == "}\n"
    assert output[5] == "module.Class2 <|-- module.Class1\n"
    assert output[6] == "footer Generated by //py2puml//\n"
    assert output[7] == "@enduml\n"

@pytest.mark.xfail(strict=True)
def test_case_20():
    diagram_name = ""
    uml_class = module_2.UmlClass("module.Class", "Class", "module")
    uml_items = [uml_class]
    uml_relations = []
    with pytest.raises(ValueError):
        list(module_0.to_puml_content(diagram_name, uml_items, uml_relations))

@pytest.mark.xfail(strict=True)
def test_case_21():
    with pytest.raises(TypeError):
        list(module_0.to_puml_content(123, [], []))

@pytest.mark.xfail(strict=True)
def test_case_22():
    with pytest.raises(TypeError):
        list(module_0.to_puml_content("TestDiagram", "not a list", []))
@pytest.mark.xfail(strict=True)
def test_case_23():
    with pytest.raises(TypeError):
        list(module_0.to_puml_content("TestDiagram", [], "not a list"))
@pytest.mark.xfail(strict=True)
def test_case_24():
    diagram_name = "TestDiagram"
    uml_class = module_2.UmlClass("module.Class", "Class", "module")
    uml_items = ["not a UmlClass"]
    uml_relations = []
    with pytest.raises(TypeError):
        list(module_0.to_puml_content(diagram_name, uml_items, uml_relations))
@pytest.mark.xfail(strict=True)
def test_case_25():
    diagram_name = "TestDiagram"
    uml_class = module_2.UmlClass("module.Class", "Class", "module")
    uml_items = [uml_class]
    uml_relations = ["not a UmlRelation"]
    with pytest.raises(TypeError):
        list(module_0.to_puml_content(diagram_name, uml_items, uml_relations))
@pytest.mark.xfail(strict=True)
def test_case_26():
    diagram_name = "TestDiagram"
    uml_class = module_2.UmlClass("module.Class", "Class", "module")
    uml_items = [uml_class, uml_class]
    uml_relations = []
    with pytest.raises(ValueError):
        list(module_0.to_puml_content(diagram_name, uml_items, uml_relations))
@pytest.mark.xfail(strict=True)
def test_case_27():
    diagram_name = "TestDiagram"
    uml_class = module_2.UmlClass("module.Class1", "Class1", "module")
    uml_class2 = module_2.UmlClass("module.Class2", "Class2", "module")
    uml_items = [uml_class, uml_class2]
    uml_relation = module_5.UmlRelation(uml_class.fqn, module_5.RelType.INHERITANCE, uml_class2.fqn)
    uml_relations = [uml_relation, uml_relation]
    with pytest.raises(ValueError):
        list(module_0.to_puml_content(diagram_name, uml_items, uml_relations))
@pytest.mark.xfail(strict=True)
def test_case_28():
    diagram_name = "TestDiagram"
    uml_class = module_2.UmlClass("module.Class1", "Class1", "module")
    uml_class2 = module_2.UmlClass("module.Class2", "Class2", "module")
    uml_items = [uml_class, uml_class2]
    uml_relation = module_5.UmlRelation(uml_class.fqn, module_5.RelType.INHERITANCE, uml_class2.fqn)
    uml_relation2 = module_5.UmlRelation(uml_class2.fqn, module_5.RelType.INHERITANCE, uml_class.fqn)
    uml_relations = [uml_relation, uml_relation2]
    with pytest.raises(ValueError):
        list(module_0.to_puml_content(diagram_name, uml_items, uml_relations))
@pytest.mark.xfail(strict=True)
def test_case_29():
    with pytest.raises(TypeError):
        list(module_0.to_puml_content("TestDiagram", [123], []))
@pytest.mark.xfail(strict=True)
def test_case_30():
    with pytest.raises(TypeError):
        list(module_0.to_puml_content("TestDiagram", [], [123]))
@pytest.mark.xfail(strict=True)
def test_case_31():
    diagram_name = "TestDiagram"
    uml_class = module_2.UmlClass("module.Class1", "Class1", "module")
    uml_class2 = module_2.UmlClass("module.Class2", "Class2", "module")
    uml_items = [uml_class, uml_class2]
    uml_relation = module_5.UmlRelation(uml_class.fqn, module_5.RelType.INHERITANCE, uml_class2.fqn)
    uml_relations = [uml_relation]
    output = list(module_0.to_puml_content(diagram_name, uml_items, uml_relations))
    assert len(output) == 8
    assert output[0] == "@startuml TestDiagram\n"
    assert output[1] == "class module.Class1 {\n"
    assert output[2] == "}\n"
    assert output[3] == "class module.Class2 {\n"
    assert output[4] == "}\n"
    assert output[5] == "module.Class2 <|-- module.Class1\n"
    assert output[6] == "footer Generated by //py2puml//\n"
    assert output[7] == "@enduml\n"

def test_case_32():
    relation = module_5.UmlRelation(source_fqn='source', target_fqn='target', type=module_5.RelType.COMPOSITION)
    assert isinstance(relation, module_5.UmlRelation)

def test_case_33():
    module_5.UmlRelation(source_fqn='source', target_fqn='target', type='NotValidType')

def test_case_34():
    relation = module_5.UmlRelation(source_fqn='source', target_fqn='target', type=module_5.RelType.COMPOSITION)
    assert relation.source_fqn == 'source'

def test_case_35():
    relation = module_5.UmlRelation(source_fqn='source', target_fqn='target', type=module_5.RelType.COMPOSITION)
    assert relation.target_fqn == 'target'

def test_case_36():
    relation = module_5.UmlRelation(source_fqn='source', target_fqn='target', type=module_5.RelType.COMPOSITION)
    assert relation.type == module_5.RelType.COMPOSITION

def test_case_37():
    relation = module_5.UmlRelation(source_fqn='source', target_fqn='target', type=module_5.RelType.INHERITANCE)
    assert relation.type == module_5.RelType.INHERITANCE

def test_case_38():
    relation = module_5.UmlRelation(source_fqn='source', target_fqn='target', type=module_5.RelType.COMPOSITION)
    assert relation.source_fqn != 'wrong_source'

def test_case_39():
    relation = module_5.UmlRelation(source_fqn='source', target_fqn='target', type=module_5.RelType.COMPOSITION)
    assert relation.target_fqn != 'wrong_target'

def test_case_40():
    relation = module_5.UmlRelation(source_fqn='source', target_fqn='target', type=module_5.RelType.COMPOSITION)
    assert relation.type != module_5.RelType.INHERITANCE

def test_case_41():
    relation = module_5.UmlRelation(source_fqn='source', target_fqn='target', type=module_5.RelType.INHERITANCE)
    assert relation.type != module_5.RelType.COMPOSITION

def test_case_42():
    assert module_5.RelType.COMPOSITION.value == '*'

def test_case_43():
    assert module_5.RelType.INHERITANCE.value == '<|'

def test_case_44():
    with pytest.raises(AttributeError):
        module_5.RelType.AGGREGATION

def test_case_45():
    assert module_5.RelType.__members__['COMPOSITION'] == module_5.RelType.COMPOSITION

def test_case_46():
    assert module_5.RelType.__members__['INHERITANCE'] == module_5.RelType.INHERITANCE

def test_case_47():
    with pytest.raises(KeyError):
        module_5.RelType.__members__['AGGREGATION']

def test_case_48():
    assert len(module_5.RelType.__members__) == 2

def test_case_49():
    assert set(module_5.RelType.__members__.values()) == {module_5.RelType.COMPOSITION, module_5.RelType.INHERITANCE}
