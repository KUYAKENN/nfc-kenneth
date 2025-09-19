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

@app.get("/nfc/kenneth/", response_class=HTMLResponse)
def get_kenneth_contact(request: Request):
    contact_data = {
        "full_name": "Kenneth Aycardo",
        "email": "software@quanbyit.com",
        "phone_number": "09094983466",
        "company": "QUANBY Solutions, Inc.",
        "title": "Software Developer",
        "address": "1862-B Dominga Street Pasay City",
        "base_url": "https://recognitionbe.quanbyit.com"
    }
    return templates.TemplateResponse("contact.html", {"request": request, "contact": contact_data})

@app.get("/nfc/kenneth/vcard")
def download_kenneth_vcard():
    """Download Kenneth's vCard file"""
    contact_data = {
        "full_name": "Kenneth Aycardo",
        "email": "software@quanbyit.com",
        "phone_number": "09094983466",
        "company": "QUANBY Solutions, Inc.",
        "title": "Software Developer",
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
            "Content-Disposition": f"attachment; filename=Kenneth_Aycardo.vcf",
            "Content-Type": "text/vcard; charset=utf-8"
        }
    )