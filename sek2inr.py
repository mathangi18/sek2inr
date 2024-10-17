from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    # Example: SEK to INR forecast logic
    sek_data = yf.download('SEKINR=X', period='1mo', interval='1d')
    prediction = sek_data['Close'][-1]  # Predict using the last close price (dummy model)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
