# Math Tunes

Tunes and live graphs generated from math functions. A single static HTML
file with no dependencies, no server and no API key.

## Run

Open `index.html` in any browser (desktop or phone) and press **Play**.

## How it works

Each tune is three expressions:

- `s(t)`: control signal (the black graph)
- `f(s, t)`: frequency in Hz
- `a(t)`: loudness envelope

For every audio sample the engine computes `phase += f / sampleRate` and
plays `wave(phase)`, so the sound and the graph come from the same numbers.

## Host it

Any static host works (GitHub Pages, Netlify, Cloudflare Pages): upload this
folder as-is.
