import unittest

from main import greet


class TestGreeting(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet(), "Привет, мир! Codex готов к работе.")

    def test_custom_name(self):
        self.assertEqual(greet("Кристина"), "Привет, Кристина! Codex готов к работе.")


if __name__ == "__main__":
    unittest.main()
