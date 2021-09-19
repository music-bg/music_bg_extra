from music_bg.context import Context
from PIL import Image


def most_frequent_color(context: Context) -> str:  # noqa: WPS210
    """
    The most frequent color of an album cover.

    returns color in format like "#FFFFFF".

    :param context: current context.
    :return: hex color.
    """
    if context.src_image is None:
        return "#000000"
    img: Image.Image = context.src_image.copy()

    img.thumbnail((100, 100))

    # Reduce colors (uses k-means internally)
    paletted = img.convert("P", palette=Image.ADAPTIVE, colors=16)  # noqa: WPS432
    # Find the color that occurs most often
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    palette_index = color_counts[0][1]

    dominant_color = palette[palette_index * 3 : palette_index * 3 + 3]

    return "#%02X%02X%02X" % tuple(dominant_color)  # noqa: WPS323
