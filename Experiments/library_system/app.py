from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-Memory "Database"
db = {
    "books": [
        {"id": 1, "title": "Database System Concepts", "author": "Silberschatz", "year": "2", "sem": "3", "available": True},
        {"id": 2, "title": "Operating System Concepts", "author": "Galvin", "year": "3", "sem": "5", "available": True},
        {"id": 3, "title": "Design Patterns", "author": "GoF", "year": "4", "sem": "7", "available": False}
    ],
    "fines": [],
    "history": []
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(db["books"])

@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = {
        "id": len(db["books"]) + 1,
        "title": data.get("title"),
        "author": data.get("author"),
        "year": data.get("year"),
        "sem": data.get("sem"),
        "available": True
    }
    db["books"].append(new_book)
    return jsonify({"message": "Book added successfully!", "book": new_book})

@app.route('/api/borrow', methods=['POST'])
def borrow_book():
    data = request.json
    book_id = data.get("id")
    for book in db["books"]:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                # Log to history
                db["history"].append({"book": book["title"], "status": "Issued"})
                return jsonify({"message": "Book issued successfully!"})
            else:
                return jsonify({"error": "Book is currently unavailable"}), 400
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
