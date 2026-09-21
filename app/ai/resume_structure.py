import re


SECTION_NAMES = {
    "certifications",
    "education",
    "experience",
    "professional experience",
    "professional summary",
    "projects",
    "skills",
    "technical skills",
    "work experience",
}


def clean_line(line: str) -> str:
    line = re.sub(r"^#{1,6}\s*", "", line.strip())
    line = line.replace("**", "").replace("__", "")
    return line.strip()


def is_section_heading(line: str) -> bool:
    heading = clean_line(line).rstrip(":").strip()
    return len(heading) < 40 and (
        heading.isupper() or heading.lower() in SECTION_NAMES
    )


def split_resume_blocks(resume_text: str) -> list[str]:
    """Group a resume preamble and its sections without changing their text."""
    lines = [line.strip() for line in resume_text.splitlines() if line.strip()]
    blocks: list[list[str]] = []

    for line in lines:
        if not blocks or is_section_heading(line):
            blocks.append([line])
        else:
            blocks[-1].append(line)

    return ["\n".join(block) for block in blocks]
