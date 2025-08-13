from flask import Blueprint, request, jsonify, render_template
from policy_fetch.fetch import fetch_performance_data
from policy_trigger.trigger import trigger_policy_creation, created_policies

bp = Blueprint('policy_routes', __name__)

@bp.route('/metrics', methods=['GET'])
def metrics():
    query = '''
        from(bucket: "pm-logg-bucket")
        |> range(start: -30d)
        |> filter(fn: (r) => r["_field"] == "DRB.UEThpDl" or r["_field"] == "RRU.PrbDl")
    '''
    data = fetch_performance_data(query, trigger_policy_creation)
    return jsonify(data) if data else (jsonify({"error": "No metrics found"}), 404)

@bp.route('/policies', methods=['POST'])
def handle_policy():
    try:
        data = request.get_json()
        print(f"[INFO] Policy received: {data}")
        return jsonify({"status": "Policy received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/policies/view', methods=['GET'])
def view_created_policies():
    return render_template("view.html", policies=created_policies)

