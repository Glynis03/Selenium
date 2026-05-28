import pytest
from pages.filedownload_page import FileDownload_page
import os
import time
@pytest.mark.order(10)
@pytest.mark.parametrize("page_url",["filedownload_page"],indirect=True)
class TestFileDownload:
      def test_filedownload(self,driver,page_url):
          filedownload=FileDownload_page(driver)
          filedownload.load(page_url)
          file=filedownload.download_file("ksnjdhsbd.txt")
          time.sleep(5)
          print(file)
          assert os.path.exists(file), f"No {file} file is downloaded"
          
