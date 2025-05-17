# NUmPyGIS
A Python library for GIS using numpy only.

## Objective

The primary objective of this library is to provide a highly performant API for GIS functionality such as polygon simplification, smoothing, validity check. A core design decision is that the library be only dependent on `numpy` and nothing else. There is a plethora of libraries in the GIS ecosystem today, most of which are not of general use-case. Another design decision is that this library will work only at polygon level. This way, the expected data structure of both input and output will always be same.
