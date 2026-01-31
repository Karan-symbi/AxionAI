from flask import Flask, request, jsonify, render_template
from evaluator import InterviewEvaluator

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

evaluator = InterviewEvaluator()

@app.route("/")
def interview():
    return render_template("interview.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    result = evaluator.evaluate(data["answers"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
