import requests

BASE_URL = "http://127.0.0.1:5000"

def test_health_check():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

if __name__ == "__main__":
    test_health_check()
    print("Health check test passed.")
