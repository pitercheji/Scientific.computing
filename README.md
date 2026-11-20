# Scientific-Computing.
A collection of Python exercises exploring numerical methods and scientific computing concepts through practical, real-world examples.

The repository progresses from NumPy fundamentals and linear algebra to differentiation, integration, optimization, differential equations, and Monte Carlo simulation. Each topic is organized into a numbered directory containing a standalone Python script.
## Requirements

- Python 3
- NumPy
- Matplotlib
- SciPy
- Pandas (used where applicable)
# Topics covered
| Topic | Example | Concepts |
|---|---|---|
| [NumPy fundamentals](./1.NumPy) | Heart-rate analysis | Arrays, statistics, filtering |
| [Vectorization](./2.Vectorization) | Audio RMS calculation | Efficient array operations |
| [Floating-point arithmetic](./3.Floating%20Point%20Arithmetics%20and%20Numerical%20Errors) | Numerical error exercises | Precision and floating-point behavior |
| [Matrix algebra](./4.Matrix%20Algebra%20and%20Operations) | Drone navigation | Matrix and vector operations |
| [Systems of linear equations](./5.Systems%20of%20Linear%20Equations) | Calorie planning | Solving linear systems |
| [Gaussian elimination and LU decomposition](./6.Gaussian%20Elimination%20and%20LU%20Decomposition) | Structural load cases | Direct linear methods |
| [Iterative linear systems](./7.Iteration%20on%20Linear%20Systems) | Pressure calculations | Iterative solvers |
| [Eigenvalues and eigenvectors](./8.EigenValues%20and%20EigenVectors) | Resonance analysis | Spectral matrix analysis |
| [Bisection and fixed-point methods](./9.Root%20Finding_Bisection%20of%20Fixed-Point%20Methods) | Break-even analysis | Root finding |
| [Newton-Raphson and secant methods](./10.Root%20Finding_Newton-Raphson%20and%20Secant%20methods) | Circuit analysis | Open root-finding methods |
| [Polynomial and nonlinear equations](./11.Solving%20polynomial%20and%20non-linear%20equations) | Robot navigation | Polynomial and nonlinear roots |
| [Interpolation](./12.Interpolation) | Waypoint elevations | Intermediate value estimation |
| [Curve fitting](./13.Curve%20fitting%20and%20approximation) | Bacterial growth | Approximation and fitting |
| [Numerical differentiation](./14.Numerical%20Differentiation) | Vehicle test track | Derivative approximation |
| [Numerical integration](./15.Numerical%20Integration) | Plasma drug concentration | Trapezoidal and Simpson integration |
| [Euler's method](./16.ODE-Euler%20Method) | Iodine-131 decay | Numerical solutions of ODEs |
| [Numerical solutions of ODEs](./17.Numerical%20solutions%20of%20ODEs) | Predator-prey dynamics | Multi-variable differential equations |
| [Numerical optimization](./18.Numerical%20Optimizations) | Product ratio optimization | Finding optimal values |
| [Monte Carlo methods](./19.Monte%20Carlo%20Methods%20and%20Random%20Numbers) | Construction risk | Random sampling and probability estimates |

Install the dependencies:

```bash
python -m pip install numpy matplotlib scipy pandas
```


## Getting Started

Clone the repository:

```bash
git clone https://github.com/kariukiii-oss/Scientific-Computing..git
cd Scientific-Computing.
```

Run an example:

```bash
python "1.NumPy/Heartrate.py"
```


Scripts with Matplotlib visualizations open a graphical window. Console-based examples print their numerical results in the terminal.

## Example

The NumPy heart-rate example calculates the mean, minimum, maximum, and readings above 100 bpm:

```bash
python "1.NumPy/Heartrate.py"
```

END.
