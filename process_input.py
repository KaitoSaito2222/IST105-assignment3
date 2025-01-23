import sys

def process_input(x, y, z):
    html_response = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Script Result</title>
    </head>
    <body>
        <h1>Assignment #3</h1>
        <h2>Python Script Result</h2>
        <p><strong>Original Values:</strong></p>
        <ul>
            <li>x: {x}</li>
            <li>y: {y}</li>
            <li>z: {z}</li>
        </ul>
        <p><strong>Calculation Steps:</strong></p>
        <ol>
            <li>Initial value of x: {x}</li>
    """

    # Perform operations
    # Add y to x using x += y
    x += y
    html_response += f"<li>After x += y: {x}</li>"
    # Subtract z from x using x -= z
    x -= z
    html_response += f"<li>After x -= z: {x}</li>"
    # Multiply x by y using x *= y
    x *= y
    html_response += f"<li>After x *= y: {x}</li>"
    # Divide x by z using x /= z(ensure z is not zero)
    x %= z
    html_response += f"<li>After x %= z: {x}</li>"

    if z != 0:
        x /= z
        html_response += f"<li>After x /= z: {x}</li>"
    else:
        html_response += "<li>Division by zero is not allowed.</li>"
    
    html_response += "</ol>"
    # Add all values for final result
    final_result = x + y + z
    html_response += f"""
            <p><strong>Final Result: x + y + z is: {x} + {y} + {z} = {final_result}</strong></p>

    </body>
    </html>
    """
    return html_response

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python process_input.py <x> <y> <z>")
        sys.exit(1)
    
    # Read input values from command-line arguments
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    except ValueError:
        print("Invalid input: Please provide numerical values for x, y, and z.")
        sys.exit(1)
    
    # Generate the HTML response
    html_output = process_input(x, y, z)
    print(html_output)
