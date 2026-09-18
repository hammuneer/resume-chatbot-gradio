from resume_chatbot.utils import extract_pdf_text


def test_extract_pdf_text_concatenates_pages(monkeypatch):
    class FakePage:
        def __init__(self, text):
            self._text = text

        def extract_text(self):
            return self._text

    class FakeReader:
        def __init__(self, _path):
            self.pages = [FakePage("Hello "), FakePage(None), FakePage("world.")]

    monkeypatch.setattr("resume_chatbot.utils.PdfReader", FakeReader)

    assert extract_pdf_text("ignored.pdf") == "Hello world."
