import requests
import json

def test_hello_endpoint():
    """Test the hello endpoint"""
    url = "http://127.0.0.1:5000/api/auth/hello"
    
    try:
        # Send GET request to hello endpoint
        response = requests.get(url)
        
        print("=== HELLO ENDPOINT TEST ===")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            response_data = response.json()
            if 'message' in response_data and 'Hello' in response_data['message']:
                print("✅ Hello endpoint working correctly!")
                return True
            else:
                print("❌ Hello endpoint returned unexpected response!")
                return False
        else:
            print("❌ Hello endpoint failed!")
            return False
            
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("Quiz Master V2 - Hello Endpoint Test")
    print("=" * 50)
    
    # Test hello endpoint
    success = test_hello_endpoint()
    
    if success:
        print("\n🎉 All tests passed!")
    else:
        print("\n❌ Some tests failed!")