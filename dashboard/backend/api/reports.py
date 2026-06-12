from fastapi import APIRouter
from fastapi.responses import FileResponse
from reports.pdf_generator import generate_pdf
from api.attacks import ATTACKS
from api.defense import EVENTS, SCORE

router = APIRouter()

@router.get("/pdf")
def download_report():
    path = generate_pdf(ATTACKS, EVENTS, SCORE)
    return FileResponse(path, media_type="application/pdf", filename="kubredops-report.pdf")
