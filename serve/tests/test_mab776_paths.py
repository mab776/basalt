"""mab776: Windows paths written quoted or in a list without escaped backslashes keep their backslashes."""
import unittest

from serve.frontend import _decode_param

ANY = {"anyOf": [{"type": "string"}, {"type": "array", "items": {"type": "string"}}]}
ARR = {"type": "array", "items": {"type": "string"}}
P = r"c:\new\repos\form-analysis\backend\relevance\tests\fixtures\baseline"


class MangledPaths(unittest.TestCase):
    def test_quoted_unescaped(self):
        self.assertEqual(_decode_param('"' + P + '"', ANY), P)

    def test_list_unescaped(self):
        self.assertEqual(_decode_param('["' + P + '"]', ARR), [P])

    def test_escaped_json_unchanged(self):
        self.assertEqual(_decode_param('["c:\\\\new\\\\repos"]', ARR), [r"c:\new\repos"])

    def test_real_newline_escape_kept(self):
        self.assertEqual(_decode_param('["line one\\nline two"]', ARR), ["line one\nline two"])

    def test_raw_path_text(self):
        self.assertEqual(_decode_param(P, ANY), P)


if __name__ == "__main__":
    unittest.main()
