from flask import Flask, request, jsonify
from googlesearch import search
from flask_cors import CORS

def fetch_google_results(query, num_results=1):
    search_results = []
    try:
        for result in search(query, num_results=num_results, advanced=True):
            search_results.append({
                'title': result.title,
                'url': result.url,
                'description': result.description
            })
        return search_results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/generate", methods=["GET"])
def generate_file():
    query = request.args.get("query", "")  
    num_results = request.args.get("num_results", 1, type=int)  
    try:
        search_results = fetch_google_results(query, num_results)
        output = {"results": search_results}
    except Exception as e:
        output = {"error": str(e)}
    print(output)
    return jsonify(output)

if __name__ == "__main__":
    app.run()
