from app.main import app


def test_unprotected_stored_resume_routes_are_not_exposed():
    paths = set(app.openapi()["paths"])

    assert "/users" not in paths
    assert "/users/{user_id}" not in paths
    assert "/resumes" not in paths
    assert "/resumes/{resume_id}" not in paths
    assert "/resumes/user/{user_id}" not in paths
    assert {"/analyze", "/tailor", "/health"} <= paths
