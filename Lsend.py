import socket
from color import Print , Choice
from http.server import HTTPServer, BaseHTTPRequestHandler
import re


s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.connect(("8.8.8.8" , 80))
ip = s.getsockname()[0]
s.close()

Print.color("server started...\n" , Choice.green , lamp=True)
Print.color(f"ipv4 : {ip}" , Choice.purple)

Print.color(f"open this URL on your MOBILE to send file OR message -->" , Choice.cyan)
Print.color(f"http://{ip}:8080/" , Choice.black , highlight=True)
print("<----------------------------------------------->") 



class Lsend(BaseHTTPRequestHandler):
    def do_GET(self):
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <style>

        input{

            border-radius: 8px;
            outline: none;
            border:none;
            box-shadow: 0 10 0;
        }
         div{
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        body{
            background-color: #262626;
        }

        
        h2 , label{
            color: white;
        }


    </style>
        
        </head>
        <body>
            <h2>L-send</h2>
            <div>
            <form method="POST" enctype="multipart/form-data">
                <label>message:</label><br>
                <input type="text" name="message" placeholder="Enter your message"><br><br>
                <label>file:</label><br>
                <input type="file" name="file"><br><br>
                <input type="submit" value="send" style="background-color: blue;width:70px; height:20px;">
            </form>
            </div>
        </body>
        </html>
        '''
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content_type = self.headers['Content-Type']
        boundary = content_type.split("boundary=")[1].encode()

        # read all data
        body = self.rfile.read(content_length)

        
        parts = body.split(b'--' + boundary)
        message = ""
        filename = None
        file_content = b""

        for part in parts:
            if b'Content-Disposition' in part:
                headers, content = part.split(b'\r\n\r\n', 1)
                headers_str = headers.decode(errors='ignore')
                content = content.rstrip(b'\r\n--')

                if 'name="message"' in headers_str:
                    message = content.decode(errors='ignore').strip()
                    Print.color(f"Received -> {message}" , Choice.green)

                elif 'name="file"' in headers_str and 'filename="' in headers_str:
                    # get file name
                    match = re.search(r'filename="(.+)"', headers_str)
                    if match:
                        filename = match.group(1)
                        file_content = content

        # save file
        if filename:
            with open(filename, "wb") as f:
                f.write(file_content)
            file_status = f"'{filename}' saved"
        else:
            file_status = "there is no File"

        # result
        response = f"""
        <html style="background-color: #202020;"><meta charset="utf-8"><body>
        <h2 style="color: white;">Received message -></h2 style="color: white;"><p style="color: white;">{message}</p>
        <h3 style="color: white;">{file_status}</h3>
        <a href="/">back</a>
        </body></html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))

# start server...
HTTPServer(("0.0.0.0", 8080), Lsend).serve_forever()