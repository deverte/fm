# FM 

Functional-like mathematics notation C++11 header-only library.

## Installation

Add repo (just once):

```sh
conan remote add astro https://gitea.zarux.ru/api/packages/astro/conan
```

Install:

```sh
conan install --remote=astro --requires=fm/<VERSION>
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

### Indexed Family

Indexed family, monad compherension (e.g. set comprehension (set-builder
notation, set abstraction), list comprehension).

Indexed family notation:

$$
v = \left( v_i \right)_{i = \overline{0, 9}} =
    \left( i^2 \right)_{i = \overline{0, 9}}
$$

or set-builder notation:

$$
v = \{ i^2 | i \in \mathbb{Z}, 0 \leq i \leq 9 \}
$$

or lambda expression:

$$
v_i = (i) \rightarrow i^2 \ \forall \ i \in \mathbb{Z}, \ 0 \leq i \leq 9
$$

```cpp
std::vector<double> v() {
  std::vector<double> res;
  fm::family(0, 9, [&](int i) { res[i] = i * i; });
  return res;
}
```

## License

License: [GPL-3](./LICENSE)  
Author: [Artem Shepelin](mailto:4.shepelin@gmail.com)