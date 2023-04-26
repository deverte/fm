# FM 

Functional-like mathematics notation C++11 header-only library.

## Installation

Add repo (just once):

```sh
conan remote add astro https://gitea.zarux.ru/api/packages/astro/conan
```

Install:

```sh
conan install --remote=astro fm/0.1.0
```

## Documentation

### Sum

Mathematical summation of a sequence Sigma-notation.

$$
f(x) = x \sum_{i = 1}^{10} \frac{x}{i}
$$

```cpp
double f(double x) {
  return x * fm::sum(1, 10, [&](int i) { return x / double(i); });
}
```

### Product

Mathematical product of a sequence Pi-notation.

$$
f(x) = 3.14 \prod_{i = 0}^{10} (x + i)
$$

```cpp
double f(double x) {
  return 3.14 * fm::prod(0, 10, [&](int i) { return x + i; });
}
```

### Cases (Piecewise)

Mathematical definition by cases (piecewise-defined function, hybrid function).

$$
f(x) =
\begin{cases}
  x^2, & x \ge 0 \\
  -x, & otherwise
\end{cases}
$$

```cpp
double f(double x) {
  return fm::cases({
    {[&]() { return x * x; }, x >= 0.0},
    {[&]() { return -x; }, true},
  });
}
```

## License

GPL