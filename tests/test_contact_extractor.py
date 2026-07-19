from app.resume_analysis.extractors import extract_contact


def test_extract_contact():
    text = """
    John Doe
    john.doe@gmail.com
    +91 9876543210
    https://linkedin.com/in/johndoe
    https://github.com/johndoe
    """

    contact = extract_contact(text)

    assert contact.email == "john.doe@gmail.com"
    assert contact.phone == "+91 9876543210"
    assert contact.linkedin == "https://linkedin.com/in/johndoe"
    assert contact.github == "https://github.com/johndoe"