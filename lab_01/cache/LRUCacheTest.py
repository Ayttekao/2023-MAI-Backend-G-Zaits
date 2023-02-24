import unittest

from lab_01.cache.LRUCache import LRUCache


class LRUCacheTest(unittest.TestCase):

    def setUp(self):
        self.cache = LRUCache(3)

    def test_should_return_element_when_adding(self):
        self.cache.set("1", "one")

        self.assertEqual("one", self.cache.get("1"))

    def test_should_return_blank_string_when_get_non_existing_element(self):
        self.assertEqual("", self.cache.get("4"))

    def test_should_return_new_value_when_update_existing_element(self):
        self.cache.set("2", "two")

        self.cache.set("2", "new two")

        self.assertEqual("new two", self.cache.get("2"))

    def test_should_return_blank_string_when_remove_existing_element(self):
        self.cache.set("1", "one")

        self.cache.remove("1")

        self.assertEqual("", self.cache.get("1"))

    def test_should_remove_least_recently_elements_when_adding_new_elements(self):
        self.cache.set("1", "one")
        self.cache.set("2", "two")
        self.cache.set("3", "three")

        self.cache.set("2", "new two")
        self.cache.set("4", "four")
        self.cache.set("5", "five")

        self.assertEqual("", self.cache.get("1"))
        self.assertEqual("new two", self.cache.get("2"))
        self.assertEqual("", self.cache.get("3"))
        self.assertEqual("four", self.cache.get("4"))
        self.assertEqual("five", self.cache.get("5"))

    def test_should_empty_cache_when_remove_all_elements(self):
        self.cache.set("1", "one")
        self.cache.set("2", "two")
        self.cache.set("3", "three")

        self.cache.remove("1")
        self.cache.remove("2")
        self.cache.remove("3")

        self.assertEqual("", self.cache.get("1"))
        self.assertEqual("", self.cache.get("2"))
        self.assertEqual("", self.cache.get("3"))


if __name__ == '__main__':
    unittest.main()
