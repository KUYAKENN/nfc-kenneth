import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'michael_app:app',  # Reference the Michael-specific FastAPI instance
        host="0.0.0.0",
        port=5003,
        reload=True
    )


