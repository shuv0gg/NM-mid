

## 1. Programs you should practice

| Priority | Topic | What to practice in code |
| --- | --- | --- |
| 1 | Significant Digits | Calculate relative error and significant digits |
| 2 | Banker’s Rounding Rule | Round numbers using ties-to-even |
| 3 | Horner’s Method | Evaluate a polynomial efficiently |
| 4 | Bisection Method | Find a root using an interval |
| 5 | False Position Method | Find a root using the regula falsi formula |
| 6 | Fixed Point Method | Iterate $x=g(x)$ |
| 7 | Newton-Raphson Method | Find a root using the derivative |
| 8 | Secant Method | Find a root using two initial guesses |
| 9 | Newton’s Forward & Backward Interpolation | Interpolation using a difference table |
| 10 | Bessel’s Formula | Central interpolation using a difference table |
| Replacement | Newton’s Divided Difference | Interpolation for equally or unequally spaced data |

Important: Newton’s Divided Difference is your replacement for Gauss Forward & Backward, not necessarily a replacement for Bessel’s formula. Confirm with your teacher whether the replacement changes the total number of programs.

## 2. The main C++ code patterns to memorize

These are the most important formulas to know how to translate into code.

### Root-finding methods

Bisection

$$
c=\frac{a+b}{2}
$$

False Position

$$
c=\frac{af(b)-bf(a)}{f(b)-f(a)}
$$

Newton-Raphson

$$
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
$$

Secant

$$
x_{n+1}=x_n-\frac{f(x_n)(x_n-x_{n-1})}{f(x_n)-f(x_{n-1})}
$$

Fixed Point

$$
x_{n+1}=g(x_n)
$$

### Interpolation methods

- Newton Forward: use the forward difference table.
- Newton Backward: use the backward difference table.
- Bessel: use central differences when the interpolation point is near the center.
- Newton Divided Difference: construct divided differences and evaluate the interpolation polynomial.

## 3. Which programs should you start coding today?

I recommend this order:

1. Horner’s Method — easiest to implement.
2. Bisection Method — simple loop and condition.
3. False Position Method — similar structure to bisection.
4. Newton-Raphson — learn derivatives and stopping conditions.
5. Secant Method — similar to Newton-Raphson but without derivatives.
6. Fixed Point Method — straightforward iteration.
7. Significant Digits and Banker’s Rounding.
8. Newton Forward/Backward, Bessel, and Divided Difference — practice difference tables carefully.

For every program, learn to change the function, initial values, tolerance, and number of iterations without rewriting the entire code.

My advice: Don't just memorize the final output. Practice writing each program from a blank editor and test it with a sample problem.