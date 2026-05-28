import pytest
from pages.dragdrop_page import DragDropPage

@pytest.mark.order(3)
@pytest.mark.parametrize("page_url", ["dragdrop_page"], indirect=True)
class TestDragDrop:
    def test_dragDrop_AtoB(self,driver,page_url):
        dragdrop=DragDropPage(driver)
        dragdrop.load(page_url)
        header_a,header_b=dragdrop.check_dragdrop_AtoB()
        assert header_a == "B", f"Expected 'B' but got '{header_a}'"
        assert header_b == "A", f"Expected 'A' but got '{header_b}'"

    def test_dragDrop_BtoA(self,driver,page_url):
        dragdrop=DragDropPage(driver)
        dragdrop.load(page_url)
        header_a,header_b=dragdrop.check_dragdrop_BtoA()
        assert header_a == "B", f"Expected 'B' but got '{header_a}'"
        assert header_b == "A", f"Expected 'A' but got '{header_b}'"