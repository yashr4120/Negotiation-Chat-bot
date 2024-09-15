# Negotiation-Chat-bot
Frontend
index.html
Description: A simple HTML form to submit price offers and view the chatbot's response.
Key Elements:
Form with a numeric input for price offers.
JavaScript to handle form submission and display the chatbot’s response.
Code Explanation
Backend (Flask)
Imports:

Flask: Web framework to create the server and handle routes.
request, jsonify, render_template: Flask utilities for handling requests and rendering HTML.
pipeline from transformers: For sentiment analysis.
Routes:

/negotiate:

Processes the user’s price offer.
Uses analyze_sentiment to determine sentiment.
Returns an appropriate negotiation response.
/:

Renders the main HTML page for user interaction.
Frontend (HTML + JavaScript)
Form:

Allows the user to input a price offer.
Submits the offer to the /negotiate endpoint.
JavaScript:

Handles form submission.
Fetches the response from the server.
Displays the result in the browser.
Troubleshooting
404 Not Found:

Ensure the server is running and listening on the correct port.
Check that the endpoint URL is correct.
400 Bad Request:

Verify that the request body is properly formatted JSON.
Ensure the server is properly parsing the incoming JSON.
Dependencies Issues:

Ensure all required libraries are installed.
Check for version conflicts and resolve them.
Future Enhancements
User Authentication: Add user authentication for more secure access.
Advanced NLP Features: Integrate more advanced NLP models or services.
UI Improvements: Enhance the web interface for a better user experience.
problem statement 
the api key is not rendering due key excessed 
