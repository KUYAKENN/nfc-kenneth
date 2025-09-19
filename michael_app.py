from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, FileResponse, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/favicon.ico")
def favicon():
    return FileResponse("static/logo.png")

@app.get("/nfc/michael/", response_class=HTMLResponse)
def get_michael_contact(request: Request):
    contact_data = {
        "full_name": "Michael Anthony Maxwell",
        "email": "michael.quanbyit.com",
        "phone_number": "+6396 1580 1028",
        "company": "QUANBY Solutions, Inc.",
        "title": "Chief Technology Officer",
        "address": "1862-B Dominga Street Pasay City",
        "base_url": "https://recognitionbe.quanbyit.com"
    }
    return templates.TemplateResponse("contact.html", {"request": request, "contact": contact_data})

@app.get("/nfc/michael/vcard")
def download_michael_vcard():
    """Download Michael's vCard file"""
    contact_data = {
        "full_name": "Michael Anthony Maxwell",
        "email": "michael.quanbyit.com",
        "phone_number": "+6396 1580 1028",
        "company": "QUANBY Solutions, Inc.",
        "title": "Chief Technology Officer",
        "address": "1862-B Dominga Street Pasay City"
    }
    
    # Generate vCard content
    vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{contact_data['full_name']}
TEL:{contact_data['phone_number']}
EMAIL:{contact_data['email']}
ORG:{contact_data['company']}
TITLE:{contact_data['title']}
ADR:;;{contact_data['address']};;;;
END:VCARD"""
    
    return Response(
        content=vcard_content,
        media_type="text/vcard",
        headers={
            "Content-Disposition": f"attachment; filename=Michael_Anthony_Maxwell.vcf",
            "Content-Type": "text/vcard; charset=utf-8"
        }
    )