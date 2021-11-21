import json

with open("states.json") as f:
    data = json.load(f)

for state in data["states"]:
    del state["area_codes"]
    # print(state["name"], state["abbreviation"])

with open("new_states_2.json", "w") as f:
    json.dump(data, f, indent=2)