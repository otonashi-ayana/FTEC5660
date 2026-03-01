import json

def parse_subproblems(json_str: str) -> list:
    """
    Parses a JSON string of subproblems and returns a list of just the clauses.
    Example input: '{"subproblems": [{"clause": "SELECT", "expression": "..."}]}'
    Example output: ['SELECT']
    """
    try:
        data = json.loads(json_str)
        subproblems = data.get("subproblems", [])
        return [item.get("clause", "") for item in subproblems if "clause" in item]
    except Exception as e:
        print(f"Warning: Failed to parse subproblems JSON: {e}")
        return []
