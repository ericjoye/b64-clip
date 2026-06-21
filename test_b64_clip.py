#!/usr/bin/env python3
"""Unit tests for b64-clip — Base64 encode/decode with clipboard."""

import base64
import importlib.util
import io
import os
import subprocess
import sys
import unittest
from unittest.mock import patch

# Load b64_clip module from file
_test_dir = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("b64_clip", os.path.join(_test_dir, "b64_clip.py"))
b64_clip = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b64_clip)


class TestEncode(unittest.TestCase):
    """Test the encode function."""

    def _make_args(self, string=None, file=None):
        """Create mock args object."""
        class Args:
            pass
        args = Args()
        args.string = string
        args.file = file
        return args

    def test_encode_simple_string(self):
        """Test encoding a simple string."""
        args = self._make_args(string="hello")
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(b64_clip, 'copy_to_clipboard'):
                b64_clip.encode(args)
        self.assertEqual(mock_stdout.getvalue().strip(), "aGVsbG8=")

    def test_encode_empty_string(self):
        """Test encoding an empty string — empty string is falsy so it reads from stdin.
        We mock stdin to return empty bytes."""
        args = self._make_args(string="")
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(b64_clip, 'copy_to_clipboard'):
                with patch('sys.stdin') as mock_stdin:
                    mock_stdin.isatty.return_value = False
                    mock_stdin.buffer.read.return_value = b""
                    b64_clip.encode(args)
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_encode_unicode(self):
        """Test encoding a Unicode string."""
        args = self._make_args(string="héllo wörld")
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(b64_clip, 'copy_to_clipboard'):
                b64_clip.encode(args)
        expected = base64.b64encode("héllo wörld".encode()).decode()
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    def test_encode_special_chars(self):
        """Test encoding special characters."""
        args = self._make_args(string="!@#$%^&*()")
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(b64_clip, 'copy_to_clipboard'):
                b64_clip.encode(args)
        expected = base64.b64encode("!@#$%^&*()".encode()).decode()
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    def test_encode_binary_like(self):
        """Test encoding binary-like data via bytes."""
        args = self._make_args(string="\x00\x01\x02\x03")
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(b64_clip, 'copy_to_clipboard'):
                b64_clip.encode(args)
        expected = base64.b64encode(b"\x00\x01\x02\x03").decode()
        self.assertEqual(mock_stdout.getvalue().strip(), expected)


class TestDecode(unittest.TestCase):
    """Test the decode function."""

    def _make_args(self, string=None, file=None, url_safe=False):
        class Args:
            pass
        args = Args()
        args.string = string
        args.file = file
        args.url_safe = url_safe
        return args

    def test_decode_simple(self):
        """Test decoding a simple base64 string."""
        args = self._make_args(string="aGVsbG8=")
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(b64_clip, 'copy_to_clipboard'):
                b64_clip.decode(args)
        self.assertEqual(mock_stdout.getvalue().strip(), "hello")

    def test_decode_unicode(self):
        """Test decoding Unicode base64."""
        encoded = base64.b64encode("héllo".encode()).decode()
        args = self._make_args(string=encoded)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(b64_clip, 'copy_to_clipboard'):
                b64_clip.decode(args)
        self.assertEqual(mock_stdout.getvalue().strip(), "héllo")

    def test_decode_url_safe(self):
        """Test decoding URL-safe base64."""
        # Use text that produces _ in URL-safe encoding (standard would have /)
        raw = "subjects?_d"
        url_safe_encoded = base64.urlsafe_b64encode(raw.encode()).decode()
        self.assertIn("_", url_safe_encoded)  # Verify it uses URL-safe chars
        args = self._make_args(string=url_safe_encoded, url_safe=True)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(b64_clip, 'copy_to_clipboard'):
                b64_clip.decode(args, url_safe=True)
        self.assertEqual(mock_stdout.getvalue().strip(), raw)

    def test_decode_auto_detect_url_safe(self):
        """Test auto-detection of URL-safe base64."""
        raw = "subjects?_d"
        url_safe_encoded = base64.urlsafe_b64encode(raw.encode()).decode()
        self.assertIn("_", url_safe_encoded)  # Verify auto-detection will trigger
        args = self._make_args(string=url_safe_encoded)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(b64_clip, 'copy_to_clipboard'):
                b64_clip.decode(args)
        self.assertEqual(mock_stdout.getvalue().strip(), raw)

    def test_decode_invalid_base64(self):
        """Test decoding invalid base64 exits with error."""
        args = self._make_args(string="not-valid-base64!!!")
        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new_callable=io.StringIO):
                with patch.object(b64_clip, 'copy_to_clipboard'):
                    b64_clip.decode(args)


class TestRoundtrip(unittest.TestCase):
    """Test encode → decode roundtrip."""

    def test_roundtrip_ascii(self):
        """Test roundtrip with ASCII text."""
        original = "Hello, World!"
        encoded = base64.b64encode(original.encode()).decode()
        decoded = base64.b64decode(encoded).decode()
        self.assertEqual(decoded, original)

    def test_roundtrip_unicode(self):
        """Test roundtrip with Unicode text."""
        original = "Héllo Wörld 🌍"
        encoded = base64.b64encode(original.encode()).decode()
        decoded = base64.b64decode(encoded).decode()
        self.assertEqual(decoded, original)

    def test_roundtrip_binary(self):
        """Test roundtrip with binary data."""
        original = bytes(range(256))
        encoded = base64.b64encode(original).decode()
        decoded = base64.b64decode(encoded)
        self.assertEqual(decoded, original)

    def test_roundtrip_empty(self):
        """Test roundtrip with empty input."""
        original = ""
        encoded = base64.b64encode(original.encode()).decode()
        decoded = base64.b64decode(encoded).decode()
        self.assertEqual(decoded, original)


class TestFileInput(unittest.TestCase):
    """Test file input handling."""

    def test_encode_file(self):
        """Test encoding from a file."""
        import tempfile
        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.txt') as f:
            f.write(b"file content")
            f.flush()
            fname = f.name

        try:
            class Args:
                pass
            args = Args()
            args.string = None
            args.file = fname
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                with patch.object(b64_clip, 'copy_to_clipboard'):
                    b64_clip.encode(args)
            expected = base64.b64encode(b"file content").decode()
            self.assertEqual(mock_stdout.getvalue().strip(), expected)
        finally:
            os.unlink(fname)

    def test_encode_file_not_found(self):
        """Test encoding from a non-existent file exits with error."""
        class Args:
            pass
        args = Args()
        args.string = None
        args.file = "/nonexistent/file.txt"
        with self.assertRaises(SystemExit):
            b64_clip.encode(args)


class TestStdinInput(unittest.TestCase):
    """Test stdin pipe input."""

    def test_encode_stdin(self):
        """Test encoding from stdin pipe."""
        class Args:
            pass
        args = Args()
        args.string = None
        args.file = None

        with patch('sys.stdin') as mock_stdin:
            mock_stdin.isatty.return_value = False
            mock_stdin.buffer.read.return_value = b"piped data"
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                with patch.object(b64_clip, 'copy_to_clipboard'):
                    b64_clip.encode(args)
        expected = base64.b64encode(b"piped data").decode()
        self.assertEqual(mock_stdout.getvalue().strip(), expected)


class TestCLI(unittest.TestCase):
    """Test CLI invocation via subprocess."""

    def test_cli_encode(self):
        """Test CLI encode command."""
        result = subprocess.run(
            [sys.executable, os.path.join(_test_dir, "b64_clip.py"), "encode", "test"],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), base64.b64encode(b"test").decode())

    def test_cli_decode(self):
        """Test CLI decode command."""
        encoded = base64.b64encode(b"test").decode()
        result = subprocess.run(
            [sys.executable, os.path.join(_test_dir, "b64_clip.py"), "decode", encoded],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "test")

    def test_cli_no_args(self):
        """Test CLI with no arguments exits with error."""
        result = subprocess.run(
            [sys.executable, os.path.join(_test_dir, "b64_clip.py")],
            capture_output=True, text=True
        )
        self.assertNotEqual(result.returncode, 0)

    def test_cli_encode_file(self):
        """Test CLI encode with --file flag."""
        import tempfile
        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.txt') as f:
            f.write(b"cli file test")
            f.flush()
            fname = f.name

        try:
            result = subprocess.run(
                [sys.executable, os.path.join(_test_dir, "b64_clip.py"), "encode", "--file", fname],
                capture_output=True, text=True
            )
            self.assertEqual(result.returncode, 0)
            expected = base64.b64encode(b"cli file test").decode()
            self.assertEqual(result.stdout.strip(), expected)
        finally:
            os.unlink(fname)


class TestClipboard(unittest.TestCase):
    """Test clipboard functionality."""

    def test_copy_to_clipboard_returns_bool(self):
        """Test that copy_to_clipboard returns a boolean."""
        result = b64_clip.copy_to_clipboard("test")
        self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main()
