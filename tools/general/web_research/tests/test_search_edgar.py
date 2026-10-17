"""Tests for search_edgar - offline (no network), 2026-10-17."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import search_edgar as se  # noqa: E402


SAMPLE = {
    "hits": {
        "total": {"value": 28},
        "hits": [
            {
                "_id": "0000950137-09-001359:c48958e10vk.htm",
                "_source": {
                    "ciks": ["0000277509"],
                    "display_names": ["FEDERAL SIGNAL CORP /DE/  (FSS)  (CIK 0000277509)"],
                    "root_form": "10-K",
                    "file_date": "2009-02-27",
                },
            }
        ],
    }
}


class TestBuildUrl(unittest.TestCase):
    def test_query_only(self):
        url = se.build_url("test", None, None, None)
        self.assertIn("q=test", url)
        self.assertNotIn("forms=", url)

    def test_form_and_dates(self):
        url = se.build_url("anpr", "10-K", "2025-01-01", "2026-10-17")
        self.assertIn("forms=10-K", url)
        self.assertIn("startdt=2025-01-01", url)
        self.assertIn("enddt=2026-10-17", url)

    def test_query_is_escaped(self):
        url = se.build_url('"license plate"', None, None, None)
        self.assertNotIn(" ", url)


class TestFormatHits(unittest.TestCase):
    def test_total_and_archive_url(self):
        out = se.format_hits(SAMPLE, 5)
        self.assertIn("total hits: 28", out)
        self.assertIn(
            "https://www.sec.gov/Archives/edgar/data/277509/000095013709001359/c48958e10vk.htm", out
        )
        self.assertIn("FEDERAL SIGNAL", out)
        self.assertIn("filed 2009-02-27", out)

    def test_limit_n(self):
        out = se.format_hits(SAMPLE, 0)
        self.assertIn("showing 0", out)
        self.assertNotIn("FEDERAL SIGNAL", out)

    def test_empty_response(self):
        out = se.format_hits({}, 5)
        self.assertIn("total hits: 0", out)


if __name__ == "__main__":
    unittest.main()
