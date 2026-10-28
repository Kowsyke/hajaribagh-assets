# Mathematical Geometry Reference for Builders

This reference provides mathematical algorithms and formulas to generate organic shapes in Minecraft.

## Elliptical Rooms and Rotundas

To construct an elliptical chamber with semi-major radius `A` along the X axis and semi-minor radius `B` along the Z axis, centered at (`cx`, `cz`):

### Solid Area Formula
A coordinate (`x`, `z`) belongs inside the floor plan if:
`((x - cx) / (A + 0.5))^2 + ((z - cz) / (B + 0.5))^2 <= 1.0`

### Hollow Perimeter Wall Formula
For a wall of thickness `T`, a block at (`x`, `z`) is a perimeter wall block if:
`((x - cx) / (A - T + 0.5))^2 + ((z - cz) / (B - T + 0.5))^2 > 1.0` and
`((x - cx) / (A + 0.5))^2 + ((z - cz) / (B + 0.5))^2 <= 1.0`

## Vaulted Ceilings and Arches

Catenary curves and inverted parabolas produce structural arches that feel natural and authentic.

### Parabolic Vault Formula
For an arch spanning from `x = -W` to `x = +W` with peak height `H`:
`y = round(H * (1.0 - (x / W)^2))`

### Block Selection by Slope
- Flat apex (slope < 0.5): Use slabs (`minecraft:stone_brick_slab[type=bottom]`).
- Gentle slope (0.5 <= slope <= 1.5): Use regular stairs (`minecraft:stone_brick_stairs`).
- Steep slope (slope > 1.5): Use full solid blocks stacked vertically.

## Hemispherical Domes

For a dome of radius `R` centered at (`cx`, `cy`, `cz`):

### Shell Equation
A block at (`x`, `y`, `z`) forms the outer shell if:
`(R - 1)^2 <= (x - cx)^2 + (y - cy)^2 + (z - cz)^2 <= R^2` with `y >= cy`.

### Ceiling Oculus
Leave a circular opening at the apex by omitting blocks where:
`(x - cx)^2 + (z - cz)^2 <= (R / 4)^2`
Infill the oculus with tinted glass or a suspended brass chandelier.

## Helical Spiral Staircases

A helical staircase climbs vertically while rotating around a central pillar.

### Parametric Equations
Let `N` be the total number of steps, `R` the radius from center, and `cy` the base height:
- Angle per step: `theta = step_index * (pi / 4)` (8 steps per full 360 degree revolution).
- Horizontal offset:
  * `x = cx + round(R * cos(theta))`
  * `z = cz + round(R * sin(theta))`
- Vertical elevation:
  * `y = cy + step_index`

### Orientation Mapping for 8-Step Helix
Map the tangent of `theta` to stair facing:
- Quadrant moving North: `facing=north`
- Quadrant moving East: `facing=east`
- Quadrant moving South: `facing=south`
- Quadrant moving West: `facing=west`
