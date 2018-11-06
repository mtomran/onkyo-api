import connexion
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route("/api/v1")
def hello():
    return "Welcome to Onkyo API"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000, debug=True)
	