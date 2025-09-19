import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'kenneth_app:app',  # Reference the Kenneth-specific FastAPI instance
        host="0.0.0.0",
        port=5004,
        reload=True
    )