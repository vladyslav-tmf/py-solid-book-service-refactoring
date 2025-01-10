import json
from xml.etree import ElementTree

from app.interfaces import BookOperation


class ConsoleDisplay(BookOperation):
    """Display content in console."""

    def process(self, content: str, title: str | None = None) -> None:
        print(content)


class ReverseDisplay(BookOperation):
    """Display content in reverse order in console."""

    def process(self, content: str, title: str | None = None) -> None:
        print(content[::-1])


class ConsolePrint(BookOperation):
    """Print content with title in console."""

    def process(self, content: str, title: str | None = None) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(BookOperation):
    """Print reversed content with title in console."""

    def process(self, content: str, title: str | None = None) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class JsonSerializer(BookOperation):
    """Serialize content to JSON format."""

    def process(self, content: str, title: str | None = None) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(BookOperation):
    """Serialize content to XML format."""

    def process(self, content: str, title: str | None = None) -> str:
        root = ElementTree.Element("book")

        title_element = ElementTree.SubElement(root, "title")
        title_element.text = title

        content_element = ElementTree.SubElement(root, "content")
        content_element.text = content

        return ElementTree.tostring(root, encoding="unicode")
