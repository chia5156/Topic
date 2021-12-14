import requests

if __name__ == "__main__":
    
    url = "https://course.fcu.edu.tw/"
    response = requests.get(url)
    print(response.status_code)
    print(response.headers)
    """
    headers = response.headers
    cookies = response.cookies
    r = requests.get(url, cookies = cookies)
    """
