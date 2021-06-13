from TEngine import TEngine


def render(txt):
    template = TEngine(txt=txt)
    print(template({'name': 'asm'}))


if __name__ == '__main__':
    txt_template = r"""
    <html>
        <body>
            <p><% emit(name) %></p>
        </body>
    </html>
    """
    render(txt=txt_template)
