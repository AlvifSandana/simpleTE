# Module name : test.py
# created by alvifsandanamahardika at 6/11/211
import unittest
from TEngine import TEngine as TemplateE


class TestTE(unittest.TestCase):
    def test_output(self):
        template = r"""
        <html>
            <body>
                <p><% write(name) %></p>
            </body>
        </html>
        """
        rendered = r"""
        <html>
            <body>
                <p>asm</p>
            </body>
        </html>
        """
        t_engine = TemplateE(text=template)
        self.assertEqual(first=t_engine({'name': 'asm'}), second=rendered, msg='Test rendering template')
