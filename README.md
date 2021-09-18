# Extra processors and variables for music_bg.

This is a plugin for [music_bg](https://github.com/music-bg/music_bg) package.

## Plugin contents

Processors:
* Box blur;
* Gaussian blur;
* Circle;
* pop_filter

Variables:
* uuid4

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

# Variables

You can use "{uuid4}" or "{uuid4.hex}" in your config to generate
UUIDv4.
