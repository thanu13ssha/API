from flask import Flask, jsonify, request

app = Flask(__name__)

# a Sample book data
books = [
    {"id": 1, "book_name": "Book1", "author": "Author1", "publisher": "Publisher1"},
    {"id": 2, "book_name": "Book2", "author": "Author2", "publisher": "Publisher2"},
]



# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    if 'book_name' not in data or 'author' not in data or 'publisher' not in data:
        return jsonify({'error': 'Missing fields'}), 400
    new_book = {
        'id': len(books) + 1,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Read a specific book
@app.route('/books/<int:book_id>', methods=['get'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(data)
        return jsonify(bok)
    else:
        return jsonify({'error': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)

