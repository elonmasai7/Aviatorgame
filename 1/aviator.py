from flask import Flask, render_template

app = Flask(__name__)

class KenyuAviationGame:
    def __init__(self):
        self.player_balance = 0
        self.min_bet = 5
        self.max_bet = 100000

    def accept_payment(self, amount):
        # Simulating payment processing - replace this with actual PayPal integration
        print(f"Simulating payment of {amount} KES received.")
        self.player_balance += amount

    def place_bet(self, amount):
        if amount < self.min_bet or amount > self.max_bet:
            print("Invalid bet amount. Please place a bet between 5 KES and 100,000 KES.")
            return False

        return True

game = KenyuAviationGame()

@app.route('/')
def index():
    return render_template('index.html', balance=game.player_balance)

if __name__ == "__main__":
    app.run(debug=True)
