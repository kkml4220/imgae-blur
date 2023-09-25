# blur

画像の平滑化(ぼかし)

![lena](./images/lena.jpg)
![blured_image](./images/blured_lena.jpg)

## Installation

```bash
pip install poetry
poetry install
```

## Usage

デフォルトでは`blur_size=4`で平滑化されます。

```bash
poetry run python blur.py images/lena.jpg
poetry run python blur.py path/to/image
```
