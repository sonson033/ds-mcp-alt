from mcp.server.fastmcp import FastMCP

mcp: FastMCP = FastMCP("MyMathServer", host="127.0.0.1", port=54321)


@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b


@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raises base to the given exponent."""
    return base**exponent


@mcp.tool()
def percentage(value: float, percent: float) -> float:
    """Returns the given percent of a value, e.g. 15 percent of 200 is 30."""
    return value * percent / 100


if __name__ == "__main__":
    print("🚀 Starting My Math Server on http://127.0.0.1:54321/sse ...")
    mcp.run(transport="sse")
