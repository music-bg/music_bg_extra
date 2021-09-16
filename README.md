# Extra processors and variables for music_bg.

This is a plugin for [music_bg](https://github.com/music-bg/music_bg) package.

## Plugin contents

Processors:
* Box blur;
* Gaussian blur;
* Circle;

Variables:
* uuid4

## Variables

You can use "uuid4" or "{uuid4.hex}" in your config to generate
UUIDv4.


## Processors

To blur an image add this to your layer config:
```json
{
    "name": "box_blur",
    "args": {
        "strength": "6"
    }
}
```
Or you can use gaussian blur.
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

### Circle processor
This processor will crop a circle
out of an image.
To use it add this to your conig file:
```
{
    "name": "circle"
}
```

It doesn't take any args.
