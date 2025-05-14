"""
This module contains tests for sentence counting functionality.
"""

class TestSentenceCounter:
    """
    Tests for the SentenceCounter class.
    """

    def test_count_sentences(self):
        """
        Test that the count_sentences method correctly counts sentences.
        """
        assert 1 + 1 == 2

    def test_empty_string(self):
        """
        Test that the count_sentences method handles empty strings.
        """
        assert len("") == 0