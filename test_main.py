from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_pdf_success():
    response = client.post(
        "/generate-pdf/",
        json={"html_content": "<h1>Hello, World!</h1>"}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.headers["content-disposition"] == 'attachment; filename=output.pdf'

def test_generate_pdf_empty_content():
    response = client.post(
        "/generate-pdf/",
        json={"html_content": ""}
    )
    assert response.status_code == 500  # Assuming an error is raised for empty input

def test_generate_pdf_invalid_data():
    response = client.post(
        "/generate-pdf/",
        json={"invalid_field": "<h1>Test</h1>"}  # Missing 'html_content'
    )
    assert response.status_code == 422  # Validation error
