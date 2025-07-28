import requests
import json
import sqlite3
import os

def test_registration():
    """Test user registration"""
    url = "http://127.0.0.1:5000/api/register"
    
    # Test user data
    user_data = {
        "full_name": "Test User",
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }
    
    try:
        # Send registration request
        response = requests.post(url, json=user_data)
        
        print("=== REGISTRATION TEST ===")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 201:
            print("✅ Registration successful!")
        else:
            print("❌ Registration failed!")
            
    except Exception as e:
        print(f"Error: {e}")

def view_database():
    """View the database contents"""
    try:
        # Check if database exists
        db_path = "quizzy.db"
        if not os.path.exists(db_path):
            print("❌ Database file not found!")
            return
        
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get table info
        cursor.execute("PRAGMA table_info(user)")
        columns = cursor.fetchall()
        
        print("\n=== DATABASE STRUCTURE ===")
        for col in columns:
            print(f"Column: {col[1]} | Type: {col[2]} | Not Null: {col[3]}")
        
        # Get all users
        cursor.execute("SELECT * FROM user")
        users = cursor.fetchall()
        
        print(f"\n=== ALL USERS ({len(users)} total) ===")
        for user in users:
            print(f"ID: {user[0]}")
            print(f"Full Name: {user[1]}")
            print(f"Username: {user[2]}")
            print(f"Email: {user[3]}")
            print(f"Password Hash: {user[4][:50]}...")
            print(f"Created At: {user[5]}")
            print("-" * 50)
        
        conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("Quizzy Registration Test")
    print("=" * 50)
    
    # Test registration
    test_registration()
    
    # View database
    view_database() 