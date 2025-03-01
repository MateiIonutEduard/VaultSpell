import os
import time

import docx
from docx.text.paragraph import Paragraph
from docx2pdf import convert

from vault.bar import *
from vault.translator import *
import VaultConfigFactory as vcf


class VaultCore:
    @staticmethod
    def CreateDocument(vaultConfig: vcf.VaultConfigFactory, src: str, dest: str, langs: list[str]):
        doc = docx.Document(src)
        paragraphs = doc.paragraphs
        ok = True

        n = len(paragraphs)
        util = GoogleTranslate()

        newDoc = docx.Document()
        config = vaultConfig.vaultConfig
        waitingTime = float(config.waitingTimeMilis) / 1000

        if config.verbose:
            print("Start translating Word document...")

        if config.showProgress:
            showProgress(0, n, prefix='Progress:', suffix='Complete', length=25)

        for i, line in enumerate(paragraphs):
            try:
                VaultCore.WriteParagraph(util, newDoc, paragraphs[i], langs)
                time.sleep(waitingTime)

                if config.showProgress:
                    showProgress(i + 1, n, prefix='Progress:', suffix='Complete', length=25)
            except AttributeError as e:
                if config.enableErrorThrowing:
                    print(f"something bad happens: {e}")
                ok = False
                break

        if ok:
            index = dest.rindex(".")

            if dest[index + 1:] == "docx":
                newDoc.save(dest)
            elif dest[index + 1:] == "pdf":
                newPath = "{}.docx".format(dest[:index])
                doc.save(newPath)

                convert(newPath, dest)
                os.remove(newPath)

            if config.verbose:
                print("Successfully translate document!")

    @staticmethod
    def GetText(src: str, dest: str):
        size = len(src)
        v = [' ', '\t', '\n']
        res = src
        ok = True

        if size >= 2:
            for i in range(len(v)):
                if src[0] == v[i]:
                    ok = False
                    break

            if not ok:
                res = "{}{}".format(src[0], dest)

            ok = True

            for i in range(len(v)):
                if src[size - 1] == v[i]:
                    ok = False
                    break

            if not ok:
                res = "{}{}".format(dest, src[size - 1])

            return res

        return dest

    @staticmethod
    def WriteParagraph(util: GoogleTranslate, doc: docx.Document, paragraph: Paragraph, langs: list[str]):
        newParagraph = doc.add_paragraph()

        for run in paragraph.runs:
            if "pic:pic" in run.element.xml:
                newParagraph.runs.append(run)
            else:
                newLine = util.GetText(run.text, src=langs[0], dest=langs[1])
                newLine = VaultCore.GetText(run.text, newLine)

                output_run = newParagraph.add_run(newLine)
                output_run.bold = run.bold
                output_run.italic = run.italic

                output_run.underline = run.underline
                output_run.font.color.rgb = run.font.color.rgb
                output_run.style.name = run.style.name

        newParagraph.paragraph_format.alignment = paragraph.paragraph_format.alignment
