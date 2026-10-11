from flask import Flask, jsonify, request

app = Flask(__name__)

# Store gym members in memory for this assignment.
members = []
next_member_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness & Gym API",
        "status": "running"
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(members), 200


@app.route("/members", methods=["POST"])
def add_member():
    global next_member_id

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    name = data.get("name")
    plan = data.get("plan")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Member name is required"}), 400

    if not isinstance(plan, str) or not plan.strip():
        return jsonify({"error": "Membership plan is required"}), 400

    member = {
        "id": next_member_id,
        "name": name.strip(),
        "plan": plan.strip()
    }

    members.append(member)
    next_member_id += 1

    return jsonify(member), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)