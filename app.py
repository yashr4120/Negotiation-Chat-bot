from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Set your OpenAI API key
# Make sure to replace the key with your own key or use environment variables
OpenAI.api_key = "YOUR_API_KEY"

# Negotiation logic for price offers
INITIAL_PRICE = 100
MINIMUM_PRICE = 80

def negotiate_price(user_offer):
    if user_offer >= INITIAL_PRICE:
        return {"status": "accept", "message": "Great! The price is acceptable.", "final_price": user_offer}
    elif user_offer >= MINIMUM_PRICE:
        counter_offer = user_offer + 5  # Bot proposes a counteroffer slightly above user offer
        return {"status": "counter_offer", "message": f"I can give you a discount, how about {counter_offer}?", "counter_offer": counter_offer}
    else:
        return {"status": "reject", "message": "Sorry, that price is too low."}

@app.route('/negotiate', methods=['POST'])
def negotiate():
    # Get user input from the request (price offer)
    user_input = request.json['user_input']
    user_offer = int(user_input)

    # Generate bot's response
    bot_response = negotiate_price(user_offer)

    return jsonify(bot_response)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
