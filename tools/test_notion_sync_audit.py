"""Offline checks for safe source matching: no Notion credentials required."""
import unittest
from tools import notion_sync_audit as audit

class SourceMappingTests(unittest.TestCase):
    def setUp(self):
        self.known={"00_CONCEPT.md","01_PROLOGUE.md","covers/QUANTUM_NOIR_GUIDE.md"}

    def test_ignores_unlabeled_crosslinks(self):
        body=("See https://github.com/Yugatn/story-x/blob/main/01_PROLOGUE.md"
              "\n\nИсточник: https://github.com/Yugatn/story-x/blob/main/00_CONCEPT.md")
        self.assertEqual(audit.identify_source(body,self.known),["00_CONCEPT.md"])

    def test_split_source_label_and_url(self):
        body="Источник:\n\nhttps://github.com/Yugatn/story-x/blob/main/covers/QUANTUM_NOIR_GUIDE.md"
        self.assertEqual(audit.identify_source(body,self.known),["covers/QUANTUM_NOIR_GUIDE.md"])

    def test_bare_source_path(self):
        body="Исходный файл: `01_PROLOGUE.md`"
        self.assertEqual(audit.identify_source(body,self.known),["01_PROLOGUE.md"])

    def test_multiple_explicit_sources_require_manual_review(self):
        body=("Источник: https://github.com/Yugatn/story-x/blob/main/00_CONCEPT.md\n"
              "Источник: https://github.com/Yugatn/story-x/blob/main/01_PROLOGUE.md")
        self.assertEqual(len(audit.identify_source(body,self.known)),2)

    def test_normalizer_ignores_markdown_emphasis(self):
        self.assertEqual(audit.norm("**Признание** другого"),"Признание другого")

    def test_join_rich_text_fragments(self):
        original_children=audit.children
        try:
            audit.children=lambda page: iter([{"type":"paragraph","paragraph":{"rich_text":[
                {"plain_text":"Город "},{"plain_text":"Икс","href":None},{"plain_text":" живёт."}
            ]},"has_children":False}])
            self.assertIn("Город Икс живёт.",audit.text_blocks("fake-page"))
        finally:
            audit.children=original_children

if __name__=="__main__":
    unittest.main()
