import math


def calculate_included_angle(A, B, C, side_opposite):
    """
    Calculates the included angle (in degrees) given three sides of a triangle.

    Parameters:
    A, B, C - sides of the triangle
    side_opposite - which angle to calculate ('a', 'b', or 'c')
        - 'a' is opposite side A
        - 'b' is opposite side B
        - 'c' is opposite side C

    Returns:
    Angle in degrees, rounded to 4 decimals
    """
    if side_opposite == 'a':
        # angle a is opposite side A
        cos_a = (B ** 2 + C ** 2 - A ** 2) / (2 * B * C)
        angle = math.degrees(math.acos(cos_a))
        return angle

    elif side_opposite == 'b':
        # angle b is opposite side B
        cos_b = (A ** 2 + C ** 2 - B ** 2) / (2 * A * C)
        angle = math.degrees(math.acos(cos_b))
        return angle

    elif side_opposite == 'c':
        # angle c is opposite side C
        cos_c = (A ** 2 + B ** 2 - C ** 2) / (2 * A * B)
        angle = math.degrees(math.acos(cos_c))
        return angle

    else:
        raise ValueError("side_opposite must be one of: 'a', 'b', or 'c'")

import math

def calculate_third_side(A=None, B=None, C=None, a=None, b=None, c=None):
    """
    Calculates the third side of a triangle.
    Two sides and one angle (in degrees) must be provided.

    Parameters:
    A, B, C - sides of the triangle
    a, b, c - angles opposite A, B, C respectively (in degrees)

    Returns:
    The missing third side, rounded to 4 decimals.
    """
    # Convert degrees to radians
    a_rad = math.radians(a) if a is not None else None
    b_rad = math.radians(b) if b is not None else None
    c_rad = math.radians(c) if c is not None else None

    # === Case 1: Law of Cosines directly (included angle) ===
    if C is None and A and B and c is not None:
        return round(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(c_rad)), 4)

    if B is None and A and C and b is not None:
        return round(math.sqrt(A**2 + C**2 - 2*A*C*math.cos(b_rad)), 4)

    if A is None and B and C and a is not None:
        return round(math.sqrt(B**2 + C**2 - 2*B*C*math.cos(a_rad)), 4)

    # === Case 2: SSA → Use Law of Sines to get included angle, then Law of Cosines ===
    if C is None and A and B and a is not None:
        sin_b = B * math.sin(a_rad) / A
        if not 0 <= sin_b <= 1:
            raise ValueError("Invalid triangle: angle computation failed.")
        b_rad = math.asin(sin_b)
        c_rad = math.pi - a_rad - b_rad
        return round(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(c_rad)), 4)

    if B is None and A and C and a is not None:
        sin_c = C * math.sin(a_rad) / A
        if not 0 <= sin_c <= 1:
            raise ValueError("Invalid triangle: angle computation failed.")
        c_rad = math.asin(sin_c)
        b_rad = math.pi - a_rad - c_rad
        return round(math.sqrt(A**2 + C**2 - 2*A*C*math.cos(b_rad)), 4)

    if A is None and B and C and b is not None:
        sin_c = C * math.sin(b_rad) / B
        if not 0 <= sin_c <= 1:
            raise ValueError("Invalid triangle: angle computation failed.")
        c_rad = math.asin(sin_c)
        a_rad = math.pi - b_rad - c_rad
        return round(math.sqrt(B**2 + C**2 - 2*B*C*math.cos(a_rad)), 4)

    raise ValueError("Provide exactly two sides and one angle (in degrees).")
