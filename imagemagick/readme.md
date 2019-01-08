## convert
* To list formats recognized by imagemagick
```bash
identify -list format
```

* To convert one image format to another format
```bash
convert ../data/space.jpg space.gif
convert ../data/space.jpg space.png
```

* To display an image
```bash
display ../data/space.jpg
```

* To get a screenshot of the whole screen
```bash
import -window root screenshot.png
```

* To get a screenshot of a region
```bash
import screenshot.png
```

* To resize image
```bash
convert ../data/space.jpg -resize "20%" resized_space.jpg
convert ../data/space.jpg -resize 256x space_256.jpg
```

* To apply some filters
```bash
convert ../data/space.jpg -monochrome monochrome_space.jpg
convert ../data/space.jpg -charcoal 1.2 charcoal_space.jpg
convert ../data/space.jpg -edge 3 edge_space.jpg
convert ../data/space.jpg -colors 4 colors_space.jpg
```