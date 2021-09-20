# Extra processors and variables for music_bg.

This is a plugin for [music_bg](https://github.com/music-bg/music_bg) package.

## Plugin contents

Processors:
* Box blur;
* Gaussian blur;
* Circle;
* pop_filter
* print
* radial_gradient

Variables:
* uuid4
* most_frequent_color
* least_frequent_color or most_frequent_color_inverted


Source image for all examples is:
![box_blur](https://raw.githubusercontent.com/music-bg/music_bg_extra/master/images/src.png)
This is cover for album "SCUZZY" by [Nikki Nair](https://open.spotify.com/artist/27JCep1zDO3K8GY50trDo6?si=sQZBGPUGSByvyzZY45AduA&dl_branch=1).

# Processors
## Blurs

![box_blur](https://raw.githubusercontent.com/music-bg/music_bg_extra/master/images/box_blur.png)

To blur an image add this to your layer config:
```json
{
    "name": "box_blur",
    "args": {
        "strength": "6"
    }
}
```

![box_blur](https://raw.githubusercontent.com/music-bg/music_bg_extra/master/images/gaussian_blur.png)

You can use gaussian blur.
As an optional parameter you
can adjust radius.
```json
{
    "name": "gaussian_blur",
    "args": {
        "radius": "5.4"
    }
}
```

## Circle processor

![circle](https://raw.githubusercontent.com/music-bg/music_bg_extra/master/images/circle.png)

This processor will crop a circle
out of an image.
To use it add this to your conig file:
```json
{
    "name": "circle"
}
```

It doesn't take any args.

## Pop filter

![pop_filter](https://raw.githubusercontent.com/music-bg/music_bg_extra/master/images/pop_filter.png)

This processor splits image onto 3 color channels and places near each other.

```json
{
    "name": "pop_filter",
    "args": {
        "offset_x": 100,
        "offset_y": 100,
        "increase_factor": 1.4,
        "decrease_factor": 0.8
    }
}
```
increase and decrease factors change
increasing and decreasing incdividual colors for each color chanel.

# Print

![print](https://raw.githubusercontent.com/music-bg/music_bg_extra/master/images/print_processor.png)

This processor renders text on an image.

```json
{
  "name": "print",
  "args": {
    "text": "This text created by processor",
    "color": "#FFFFFF",
    "font": "FiraCode-Retina",
    "font_size": 30,
    "start_x": null,
    "start_y": null,
    }
}
```

you can adjust font and size.
Also you can choose x and y coordinates where to
start draw.


# Radial gradient
![radial_gradient](https://raw.githubusercontent.com/music-bg/music_bg_extra/master/images/radial_gradient.png)

This processor creates radial gradient with
two colors "inner" and "outer".
Inner - color at the center of an image,
outer - color at the border.

# Variables

## uuid4
You can use "{uuid4}" or "{uuid4.hex}" in your config to generate
UUIDv4.


## most_frequent_color

This variable is used to retrieve
most frequent color of an image in
hex format.

## least_frequent_color

This variable is used to retrieve
inverted color to the most frequent one.

It's calculated by inverting the
original color.

inverted = (255 - red, 255 - green, 255 - blue)

Also this variable has a synonym "`most_frequent_color_inverted`".
