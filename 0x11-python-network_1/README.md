The `urllib` package is a Python library that allows you to fetch internet resources like web pages, files, and more. It provides several modules, such as `urllib.request`, `urllib.error`, and `urllib.parse`, to work with URLs and make HTTP requests. Here's a basic guide on how to fetch internet resources using the `urllib.request` module:

1. **Import `urllib.request`**:
   
   First, you need to import the `urllib.request` module:

   ```python
   import urllib.request
   ```

2. **Open a URL**:

   You can open a URL using the `urllib.request.urlopen()` function. This function returns a file-like object, which you can use to read the content of the URL:

   ```python
   url = 'https://www.example.com'  # Replace with the URL you want to fetch
   response = urllib.request.urlopen(url)
   ```

3. **Read the Content**:

   You can now read the content of the URL using various methods like `.read()`, `.readline()`, or `.readlines()`. For example, to read the entire content as a string:

   ```python
   html_content = response.read()
   ```

   This will store the HTML content of the web page in the `html_content` variable.

4. **Handling Errors**:

   It's important to handle exceptions that may occur during the request. You can use `urllib.error` to catch and handle errors like `HTTPError` and `URLError`:

   ```python
   import urllib.error

   try:
       response = urllib.request.urlopen(url)
       html_content = response.read()
   except urllib.error.HTTPError as e:
       print(f"HTTPError: {e.code} - {e.reason}")
   except urllib.error.URLError as e:
       print(f"URLError: {e.reason}")
   ```

   This code will print error messages if there are any issues with the request.

5. **Closing the Response**:

   It's good practice to close the response when you're done with it to free up system resources:

   ```python
   response.close()
   ```

6. **Working with Headers**:

   You can access response headers using the `.getheaders()` method:

   ```python
   headers = response.getheaders()
   for header in headers:
       print(header)
   ```

   This allows you to inspect details like the content type, content length, and more.

7. **Working with Cookies and Authentication**:

   If you need to work with cookies or perform authenticated requests, you can use additional libraries or functions like `http.cookiejar` and `urllib.request.HTTPBasicAuthHandler`.

Here's a complete example that fetches and prints the content of a web page:

```python
import urllib.request
import urllib.error

url = 'https://www.example.com'  # Replace with the URL you want to fetch

try:
    response = urllib.request.urlopen(url)
    html_content = response.read()
    print(html_content.decode('utf-8'))  # Decode the content to a string
    response.close()
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"URLError: {e.reason}")
```

This code fetches the web page content from the specified URL and prints it as a string. Remember to handle exceptions appropriately to ensure your code is robust.
