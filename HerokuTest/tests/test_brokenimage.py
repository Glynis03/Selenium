import pytest
from pages.brokenimage_page import BrokenImage

@pytest.mark.order(5)
@pytest.mark.parametrize("page_url", ["brokenimage_page"], indirect=True)
class TestBrokenImage:
    def test_brokenimage_request(self,driver,page_url):
        brokenimage=BrokenImage(driver)
        brokenimage.load(page_url)
        broken_images = []
        checkimage=brokenimage.check_brokenimage_request()
        for url, value in checkimage.items():
           if value == "Broken":
               broken_images.append(url)
        assert broken_images, "Expected broken images but none were found"
        print("Broken images found:")
        for img in broken_images:
            print(img)
    
    def test_brokenimage_script(self,driver,page_url):
        brokenimage=BrokenImage(driver)
        brokenimage.load(page_url)
        broken_images = []
        checkimage=brokenimage.check_brokenimage_script()
        for url, value in checkimage.items():
           if value == "Broken":
               broken_images.append(url)
        assert broken_images, "Expected broken images but none were found"
        print("Broken images found:")
        for img in broken_images:
            print(img)
    