from docx import Document


class ResumeGenerator:

    @staticmethod
    def generate(resume_text: str, output_path: str):

        document = Document()

        for line in resume_text.split("\n"):

            line = line.strip()

            if not line:
                continue

            # Treat ALL CAPS or title-like short lines as headings
            if len(line) < 40 and (
                line.isupper()
                or line.endswith(":")
            ):
                document.add_heading(
                    line.replace(":", ""),
                    level=2,
                )
            else:
                document.add_paragraph(line)

        document.save(output_path)