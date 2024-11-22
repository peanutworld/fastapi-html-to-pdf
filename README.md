# HTML to PDF Converter

A simple FastAPI app to convert HTML content into PDF using WeasyPrint.

## Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/peanutworld/fastapi-html-to-pdf.git
   cd fastapi-html-to-pdf

2. **Create and activate a virtual environment (optional):**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

## Run the Application

1. **Start the FastAPI app:**

   ```bash
   python -m uvicorn main:app --reload

2. **Health Check**

   ```bash
   curl http://127.0.0.1:8000/
   
3. **Generate PDF**

   ```bash
   curl -X POST http://127.0.0.1:8000/generate-pdf/ -H "Content-Type: application/json" -d '{"html_content": "<h1>PDF Example</h1>"}' --output output.pdf

## Testing

1. **Run tests:**

   ```bash
    python -m pytest test_main.py

## License
This project is licensed under the MIT License.

