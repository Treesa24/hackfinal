from fastapi import FastAPI
from app.api.receipt import router as receipt_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Carbon Receipt Tracker",
    description="Scan receipts and calculate carbon footprint",
    version="1.0"
)

# 1. ADD MIDDLEWARE FIRST
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



# 2. REGISTER ROUTES AFTER MIDDLEWARE
app.include_router(receipt_router)

@app.get("/")
def root():
    return {"message": "Carbon Receipt Tracker API is running"}