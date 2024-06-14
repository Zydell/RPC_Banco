import radon.complexity as complexity

def analyze_complexity(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return complexity.cc_visit(code)

def print_complexity_results(results, title):
    print(f"\n{title}")
    for item in results:
        print(f"{item.name}: {item.complexity}")

if __name__ == "__main__":
    client_results = analyze_complexity('bank_client.py')
    server_results = analyze_complexity('bank_server.py')

    print_complexity_results(client_results, "Client Code Complexity")
    print_complexity_results(server_results, "Server Code Complexity")

