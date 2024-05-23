import json
import random

def generate_large_data(num_nodes=100, num_edges=200):
    nodes = []
    edges = []
    categories = ['A', 'B', 'C']
    for i in range(1, num_nodes + 1):
        node = {
            "item_no": f"I{i}",
            "category": random.choice(categories)
        }
        nodes.append(node)

    for _ in range(num_edges):
        source = random.choice(nodes)["item_no"]
        target = random.choice(nodes)["item_no"]
        if source != target:
            edge = {
                "source": source,
                "target": target
            }
            edges.append(edge)

    data = {
        "nodes": nodes,
        "edges": edges
    }
    return data

large_data = generate_large_data()

with open('large_data.json', 'w') as f:
    json.dump(large_data, f, indent=4)

print("Large data JSON file generated: large_data.json")
