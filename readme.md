(Blogging) from Jupyter
=======================

## Installation

This package is compatible with Python 3.8 and higher

```shell
pip install from-jupyter
```

If you want to be able to export data frames to images, it is also necessary to install [wkhtmltopdf](https://wkhtmltopdf.org/):

```shell
# Debian
sudo apt-get install wkhtmltopdf
# MacOS with brew
brew install --cask wkhtmltopdf
```

## Usage

*from-jupyter* relies heavily on cell metadata, whenever you want to export a cell, you probably need to add metadata
to make sure the export happens as you want.

### Exporting images

Given a code cell that produces a *matplotlib* plot:

```python
import matplotlib.pyplot as plt

plt.plot(1, 2, 3)
```

It is necessary to add the `"image"` key to the metadata, the value should be the name you want the plot to have when
exported to the local file system.

![Set image metadata](https://ik.imagekit.io/thatcsharpguy/posts/from-jupyter/image-export.gif?ik-sdk-version=javascript-1.4.3&updatedAt=1652333071909)

The command below will output the plot to the path `output/showcase/my-first-plot.png`:

```shell
from-jupyter images showcase.ipynb
```

The output:

![my-first-plot.png](https://ik.imagekit.io/thatcsharpguy/posts/from-jupyter/my-first-plot.png?ik-sdk-version=javascript-1.4.3&updatedAt=1652334258025)

### Exporting *pandas* data frames

Given a cell that outputs a *pandas* data frame as a table:

```python
import pandas as pd

my_frame = pd.DataFrame([
    (1, 2),
    (3, 4),
    (5, 6),
], columns=["column 1", "column 2"])

my_frame.head()
```

It is necessary to add the `"dataframe"` key to the metadata, the value should be the name you want the exported
dataframe to have in the local file system.

![Set dataframe metadata](https://ik.imagekit.io/thatcsharpguy/posts/from-jupyter/my-dataframe.gif?ik-sdk-version=javascript-1.4.3&updatedAt=1652334019004)

The command below will generate the dataframe as image located in `output/showcase/my-dataframe.png`:

```shell
from-jupyter frames showcase.ipynb
```

The output:

![my-dataframe.png](https://ik.imagekit.io/thatcsharpguy/posts/from-jupyter/my-dataframe.png?ik-sdk-version=javascript-1.4.3&updatedAt=1652334258980)

### Exporting code

Any code cell can also be exported to an independent code file, to do this, it is necessary to add the "gist" key to the
cell, with the value being the name of the file you want to take.

To export them to the output folder, one needs to use:

```shell
from-jupyter code showcase.ipynb
```

## Similar projects

 - [IPyPublish](https://github.com/chrisjsewell/ipypublish)
 - [Jupyter Book](https://github.com/executablebooks/jupyter-book)
 