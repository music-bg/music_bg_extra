from music_bg.context import Context

from music_bg_extra.utils import most_frequent_color


def most_frequent_color_var(context: Context) -> str:
    """
    The most frequent color of an album cover.

    returns color in format like "#FFFFFF".

    :param context: current context.
    :return: hex color.
    """
    if context.src_image is None:
        return "#000000"
    dominant_color = most_frequent_color(context.src_image.copy())
    return "#%02X%02X%02X" % dominant_color  # noqa: WPS323


def most_frequent_color_inverted_var(context: Context) -> str:
    """
    The most frequent color of an album cover.

    returns color in format like "#FFFFFF".

    :param context: current context.
    :return: hex color.
    """
    if context.src_image is None:
        return "#000000"
    red, green, blue = most_frequent_color(context.src_image.copy())
    return "#%02X%02X%02X" % (  # noqa: WPS323
        255 - red,
        255 - green,
        255 - blue,
    )
