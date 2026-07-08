KNOWN_WIDTHS = {
    "person"        : 50,
    "car"           : 180,
    "bottle"        : 8,
    "chair"         : 50,
    "laptop"        : 35,
    "cell phone"    : 7,
    "cup"           : 8,
    "book"          : 20,
    "tv"            : 80,
    "dog"           : 30,
    "cat"           : 25,
    "bicycle"       : 60,
    "motorbike"     : 80,
    "bus"           : 250,
    "truck"         : 250,
    "default"       : 30,
}

FOCAL_LENGTH = 615

def get_known_width(label: str) -> float:
    return KNOWN_WIDTHS.get(label.lower(), KNOWN_WIDTHS["default"])

def calculate_distance(label: str, pixel_width: float) -> float:
    if pixel_width <= 0:
        return 0.0
    known_width  = get_known_width(label)
    distance_cm  = (known_width * FOCAL_LENGTH) / pixel_width
    distance_m   = distance_cm / 100
    return round(distance_m, 2)

def distance_to_color(distance: float) -> tuple:
    if distance < 1.0:
        return (0, 0, 255)
    elif distance < 2.0:
        return (0, 165, 255)
    else:
        return (0, 255, 0)