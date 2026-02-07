from llm_client import generate_response

if __name__ == "__main__": # ensures that the program is executed not import 
    user_input = input("Enter prompt: ")
    
    result = generate_response(user_input)
    
    if result["success"]:
        print(f"\nResponse: {result['response']}")
        print(f"\nMetadata:")
        print(f"  Latency: {result['latency']:.2f}s")
        print(f"  Retries: {result['retries']}")
        print(f"  Prompt length: {result['prompt_length']} chars")
    else:
        print("\n✗ Request Failed")
        print(f"  Error: {result.get('error', 'Unknown error')}")
        print(f"  Retries attempted: {result['retries']}")