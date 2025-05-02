import yaml

def generate_network_policy(service_name, namespace, pod_selector, ingress_rules, egress_rules):
    """
    Generate a Kubernetes NetworkPolicy YAML file.

    Args:
        service_name (str): Name of the service.
        namespace (str): Namespace of the service.
        pod_selector (dict): Selector for the pods the policy applies to.
        ingress_rules (list): List of ingress rules.
        egress_rules (list): List of egress rules.

    Returns:
        dict: NetworkPolicy YAML as a dictionary.
    """
    network_policy = {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "NetworkPolicy",
        "metadata": {
            "name": f"{service_name}-network-policy",
            "namespace": namespace
        },
        "spec": {
            "podSelector": pod_selector,
            "policyTypes": []
        }
    }

    if ingress_rules:
        network_policy["spec"]["policyTypes"].append("Ingress")
        network_policy["spec"]["ingress"] = ingress_rules

    if egress_rules:
        network_policy["spec"]["policyTypes"].append("Egress")
        network_policy["spec"]["egress"] = egress_rules

    return network_policy

def save_to_yaml_file(data, file_name):
    """Save a dictionary to a YAML file."""
    with open(file_name, "w") as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"NetworkPolicy YAML saved to {file_name}")

if __name__ == "__main__":
    # Input details for the NetworkPolicy
    service_name = input("Enter the service name: ").strip()
    namespace = input("Enter the namespace: ").strip()
    pod_selector = {"matchLabels": {"app": service_name}}

    # Example ingress and egress rules
    ingress_rules = [
        {
            "from": [
                {"ipBlock": {"cidr": "192.168.1.0/24"}}
            ],
            "ports": [
                {"protocol": "TCP", "port": 80}
            ]
        }
    ]

    egress_rules = [
        {
            "to": [
                {"ipBlock": {"cidr": "0.0.0.0/0"}}
            ],
            "ports": [
                {"protocol": "TCP", "port": 443}
            ]
        }
    ]

    # Generate the NetworkPolicy
    network_policy = generate_network_policy(service_name, namespace, pod_selector, ingress_rules, egress_rules)

    # Save to a YAML file
    file_name = f"{service_name}-network-policy.yaml"
    save_to_yaml_file(network_policy, file_name)