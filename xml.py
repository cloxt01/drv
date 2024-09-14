import requests

# URL endpoint XML-RPC
url = 'https://smkn1rangkasbitung.sch.id/xmlrpc.php'

# Payload XML untuk metode metaWeblog.newPost
xml_payload = '''<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>metaWeblog.newPost</methodName>
  <params>
    <param>
      <value><string>blog_id</string></value>
    </param>
    <param>
      <value><string>admin</string></value>
    </param>
    <param>
      <value><string>admin</string></value>
    </param>
    <param>
      <value>
        <struct>
          <member>
            <name>title</name>
            <value><string>My New Post</string></value>
          </member>
          <member>
            <name>description</name>
            <value><string>This is the content of my new post.</string></value>
          </member>
          <member>
            <name>categories</name>
            <value>
              <array>
                <data>
                  <value><string>Category1</string></value>
                  <value><string>Category2</string></value>
                </data>
              </array>
            </value>
          </member>
        </struct>
      </value>
    </param>
    <param>
      <value><boolean>1</boolean></value>
    </param>
  </params>
</methodCall>'''

# Header untuk permintaan POST
headers = {
    'Content-Type': 'text/xml',
    'User-Agent': 'Python-Requests/2.25.1'
}

# Mengirim permintaan POST
response = requests.post(url, data=xml_payload, headers=headers)

# Menampilkan hasil respons
print('Status Code:', response.status_code)
print('Response Body:', response.text)
