# Modul 1.6 - Latihan 1: Neuron dan Jaringan

## Bagian A: Satu neuron (x=[0.5,-1.0], w=[0.8,0.2], b=-0.1, y=1)

1. Forward
   - z = 0.8*0.5 + 0.2*(-1.0) + (-0.1) = 0.4 - 0.2 - 0.1 = 0.1
   - p = sigmoid(0.1) = 0.525
   - Loss y=1: -ln(0.525) = 0.644
   - Loss y=0: -ln(1-0.525) = 0.744

2. Gradien (sigmoid + BCE: dz = p - y)
   - dz = 0.525 - 1 = -0.475
   - dw = dz * x = [-0.2375, 0.475]
   - db = dz = -0.475

3. Satu langkah gradient descent (lr = 0.1)
   - w baru = w - lr*dw = [0.8+0.02375, 0.2-0.0475] = [0.82375, 0.1525]
   - b baru = -0.1 - 0.1*(-0.475) = -0.0525
   - z baru = 0.82375*0.5 + 0.1525*(-1.0) - 0.0525 = 0.20688
   - p baru = 0.5515, loss baru = 0.595
   - Loss TURUN dari 0.644 ke 0.595.

## Bagian B: Jaringan 2-2-1 (ReLU)

| x | z1 | a1 = ReLU(z1) | z2 | p | Loss y=1 | Loss y=0 |
|---|----|---------------|----|---|----------|----------|
| [1, 2] | [2.0, 3.5] | [2.0, 3.5] | -0.25 | 0.4378 | 0.826 | 0.576 |
| [-1, 0.5] | [-0.75, 2.5] | [0, 2.5] | -0.95 | 0.2789 | 1.277 | 0.327 |

Jumlah parameter: (2x2 + 2) + (2x1 + 1) = 9