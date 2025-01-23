from flask import Flask, render_template, request, jsonify
import json
import os
import urllib.parse

app = Flask(__name__)

# Load subsidies from JSON
def load_subsidies():
    with open(os.path.join("data", "subsidies.json"), "r") as file:
        return json.load(file)

subsidies = load_subsidies()

@app.route('/')
def index():
    return render_template('index.html', subsidies=subsidies)

@app.route('/subsidy/<int:subsidy_id>')
def subsidy_details(subsidy_id):
    subsidy = next((s for s in subsidies if s['id'] == subsidy_id), None)
    return render_template('subsidy_details.html', subsidy=subsidy)

@app.route('/search', methods=['POST'])
def search():
    user_data = request.get_json()
    keyword = user_data.get('keyword', '').lower()
    
    # Search in the JSON file
    results = [
        subsidy for subsidy in subsidies
        if keyword in subsidy['name'].lower() or keyword in subsidy['category'].lower() or keyword in subsidy['eligibility'].lower()
    ]

    if results:
        return jsonify(results)
    
    # If no results found, create a Google search link
    google_search_url = f"https://www.google.com/search?q={urllib.parse.quote(keyword)}+government+subsidy+India"
    return jsonify([{
        "name": f"Search results for '{keyword}'",
        "category": "Google Search",
        "official_link": google_search_url,
        "eligibility": "Click the link to view search results on Google."
    }])

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    #init_db()
    app.run(host='0.0.0.0', port=5000)
