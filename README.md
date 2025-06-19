# 🛠️ parser

try out file at http://3.146.105.13:8000/parse
> A custom file parser thats decodes a propritery file type.  
Extracts embedded images, XML, and text files with byte-level precision. 🔍
> This is was built with fastapi becuase it allows for a very quick reponse time over the internet which is ideal for single purporse API endpoints


---

## 🚀 Logic

- 1️⃣ load file bytes as decimal values
- 2️⃣ iterate through each byte
- 3️⃣ If new file/header pattern(%%) is found make note
- 4️⃣ If body start pattern (_SIG/D.C.) is found calculate length of body (from next 4 value) then write body as file using found length
- 5️⃣ Convert all written files to zip and return

---


---

## 🚀 Features

- 🔢 accesable api (http://3.146.105.13:8000/parse)
- 🖼️ flexible algoithm (can work if file was in different order)
- ⚡ Built with FastAPI (backend)

---

## 📁 Project Structure

parser/
├── backend/
│ ├── main.py # Entry point for FastAPI app
│ ├── all_outputs.zip # Sample output archive
│ └── routes/
│ └── parser.py # Core parsing logic
├── sample.env # Test file to parse
└── README.md

yaml
Copy
Edit

---

## 🧪 How to Run

```bash
cd backend
python main.py
Or go to go to:
http://localhost:8000/parse
…and watch the magic happen. 🪄


👩‍💻 Built With
Python 3
FastAPI



## License
 
The MIT License (MIT)

Copyright (c) 2025 Michael Higgins

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
