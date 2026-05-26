from pages.dragdrop_page import DragDropPage
def test_dragDrop_AtoB(driver):
    dragdrop=DragDropPage(driver)
    dragdrop.load()
    header_a,header_b=dragdrop.check_dragdrop_AtoB()
    assert header_a == "B", f"Expected 'B' but got '{header_a}'"
    assert header_b == "A", f"Expected 'A' but got '{header_b}'"

def test_dragDrop_BtoA(driver):
    dragdrop=DragDropPage(driver)
    dragdrop.load()
    header_a,header_b=dragdrop.check_dragdrop_BtoA()
    assert header_a == "B", f"Expected 'B' but got '{header_a}'"
    assert header_b == "A", f"Expected 'A' but got '{header_b}'"