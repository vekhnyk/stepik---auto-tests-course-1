import math
import time

from selenium import webdriver

try:
    def test_substring(full_string, substring):
        assert substring in full_string, f"expected '{substring}' \
to be substring of '{full_string}'"


    test_substring("1211", "111")
finally:
    time.sleep(1)
