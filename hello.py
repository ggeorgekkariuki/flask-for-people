from flask import Flask, render_template

import connexion

# app = Flask(__name__, template_folder="templates")

# We create the 'app' using Connexion rather that Flask. Internally the 
# Flask app exists, but now has additional functionality added to it

app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

@app.route('/')
def home():
  return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)