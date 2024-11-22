from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from weasyprint import HTML
import io

app = FastAPI()

# Request body model
class HTMLData(BaseModel):
    html_content: str

@app.get("/")
async def read_root():
    return {"message": "FastAPI app is running!"}

@app.post("/generate-pdf/")
async def generate_pdf(data: HTMLData):
    try:
        if not data.html_content.strip():  # Check for empty or whitespace-only content
            raise HTTPException(status_code=400, detail="HTML content cannot be empty")

        # Convert HTML to PDF using WeasyPrint
        pdf_bytes = io.BytesIO()
        HTML(string=data.html_content).write_pdf(pdf_bytes)
        pdf_bytes.seek(0)

        # Return PDF as a response
        return Response(content=pdf_bytes.read(), media_type="application/pdf", headers={
            "Content-Disposition": "attachment; filename=output.pdf"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
