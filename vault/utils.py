import docx
from vault.translator import *
from vault.bar import *
import time


class VaultCore:
    @staticmethod
    def CreateDocument(src, dest, langs):
        doc = docx.Document(src)
        paragraphs = doc.paragraphs
        ok = True

        n = len(paragraphs)
        util = GoogleTranslate()

        newDoc = docx.Document()
        showProgress(0, n, prefix='Progress:', suffix='Complete', length=25)

        for i, line in enumerate(paragraphs):
            try:
                VaultCore.WriteParagraph(util, newDoc, paragraphs[i], langs)
                time.sleep(.2)
                showProgress(i + 1, n, prefix='Progress:', suffix='Complete', length=25)
            except AttributeError:
                ok = False
                break

        if ok:
            newDoc.save(dest)
            print("\n Successfully translate document!")

    @staticmethod
    def WriteParagraph(util, doc, paragraph, langs):
        newParagraph = doc.add_paragraph()

        for run in paragraph.runs:
            newLine = util.GetText(run.text, src=langs[0], dest=langs[1])
            output_run = newParagraph.add_run(newLine)
            output_run.bold = run.bold
            output_run.italic = run.italic

            output_run.underline = run.underline
            output_run.font.color.rgb = run.font.color.rgb
            output_run.style.name = run.style.name

        newParagraph.paragraph_format.alignment = paragraph.paragraph_format.alignment
