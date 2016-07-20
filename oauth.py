import webbrowser
import tweepy
from flask import Flask, request

app = Flask(__name__)

consumer_key = 'EnPaX5HTms295YDmouVFrpERJ'
consumer_secret = 'yGuaL0ql77s5c3Nq16AtgBzULiXC1vbdioNS2CC5A84g4dsIea'
callback_url = 'http://localhost:5000/history'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_url)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/oauth')
def post():
  print('in here')
# Open authorization URL in browser
  webbrowser.open(auth.get_authorization_url())

@app.route('/history')
def main():
  return 'sup'

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)

  # Get access token
  #token = auth.get_access_token(verifier=pin)
