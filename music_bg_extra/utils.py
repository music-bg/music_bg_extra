from typing import Tuple

from PIL import Image


def most_frequent_color(image: Image.Image) -> Tuple[int, int, int]:
    """
    Find the most frequent color of the image.

    :param image: input image.
    :return: color tuple.
    """
    image.thumbnail((100, 100))

    # Reduce colors (uses k-means internally)
    paletted = image.convert("P", palette=Image.ADAPTIVE, colors=16)
    # Find the color that occurs most often
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    palette_index = color_counts[0][1]

    dominant_color = palette[palette_index * 3 : palette_index * 3 + 3]

    return tuple(dominant_color)  # type: ignore


def colorstr_to_tuple(color: str) -> Tuple[int, int, int]:
    """
    Convert color hex to tuple of ints.

    :param color: color hex.
    :raises ValueError: if string has unknown format.
    :return: color tuple (red, green, blue).
    """
    color_hex = color.lstrip("#")
    if len(color_hex) != 6:
        raise ValueError(f"Badly formatted color string: '{color_hex}'")

    red = int(color_hex[:2], base=16)
    green = int(color_hex[2:4], base=16)
    blue = int(color_hex[4:], base=16)

    return red, green, blue
