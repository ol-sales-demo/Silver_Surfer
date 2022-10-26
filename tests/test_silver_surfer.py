#!/usr/bin/env python

"""Tests for `silver_surfer` package."""


import unittest
from click.testing import CliRunner

from silver_surfer import silver_surfer
from silver_surfer import cli


class TestSilver_surfer(unittest.TestCase):
    """Tests for `silver_surfer` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'silver_surfer.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
