from stem.control import Controller
import json

with Controller.from_port(port=9051) as controller:
    controller.authenticate()

    circuits = []
    for circ in controller.get_circuits():
        circuit_info = {
            "id": circ.id,
            "path": [(r[0].address, r[1]) for r in circ.path],
            "purpose": circ.purpose,
            "build_flags": circ.build_flags
        }
        circuits.append(circuit_info)

with open('../data/circuit_data.json', 'w') as f:
    json.dump(circuits, f, indent=4)
