import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

def init_db():
    try:
        # Prefer environment variable (Railway / production)
        firebase_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")

        if firebase_json:
            cred = credentials.Certificate(json.loads(firebase_json))
        else:
            # Fallback for local development
            cred = credentials.Certificate("app/firebase_key.json")

        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)

        print("Firebase initialized successfully")
        return firestore.client()

    except Exception as e:
        print(f"Firebase initialization failed: {e}. Using mock database.")

        # Mock database (safe fallback)
        class MockDB:
            def collection(self, name):
                return self
            
            def add(self, data):
                print(f"Mock save: {data}")
                return None, "mock-id"
            
            def stream(self):
                return []

        return MockDB()

db = init_db()
