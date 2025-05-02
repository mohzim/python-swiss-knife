import subprocess

def build_docker_image(image_name, dockerfile_path="."):
    """Build a Docker image."""
    print(f"Building Docker image: {image_name}")
    try:
        subprocess.run(
            ["docker", "build", "-t", image_name, dockerfile_path],
            check=True,
            text=True
        )
        print(f"Docker image {image_name} built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error building Docker image: {e}")
        exit(1)

def push_docker_image(image_name):
    """Push the Docker image to a container registry."""
    print(f"Pushing Docker image: {image_name}")
    try:
        subprocess.run(
            ["docker", "push", image_name],
            check=True,
            text=True
        )
        print(f"Docker image {image_name} pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing Docker image: {e}")
        exit(1)

def deploy_to_kubernetes(deployment_file):
    """Deploy the application to Kubernetes using a YAML file."""
    print(f"Deploying to Kubernetes using {deployment_file}")
    try:
        subprocess.run(
            ["kubectl", "apply", "-f", deployment_file],
            check=True,
            text=True
        )
        print(f"Deployment applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deploying to Kubernetes: {e}")
        exit(1)

if __name__ == "__main__":
    # Define variables
    docker_image_name = input("Enter the Docker image name (e.g., myapp:latest): ").strip()
    dockerfile_path = input("Enter the path to the Dockerfile (default is current directory): ").strip() or "."
    deployment_yaml = input("Enter the path to the Kubernetes deployment YAML file: ").strip()

    # Automate the process
    build_docker_image(docker_image_name, dockerfile_path)
    push_docker_image(docker_image_name)
    deploy_to_kubernetes(deployment_yaml)