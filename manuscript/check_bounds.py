from fractions import Fraction
import json


def ceiling_divide(numerator, denominator):
    return -((-numerator) // denominator)


def series_bounds(degree, argument, steps=10000, scale=10**12):
    assert 0 <= degree < steps and 0 < argument < 1
    lower = upper = partial_lower = partial_upper = scale
    degree_numerator, degree_denominator = degree.numerator, degree.denominator
    argument_numerator, argument_denominator = argument.numerator, argument.denominator
    for index in range(steps):
        numerator = ((index * degree_denominator - degree_numerator)
                     * ((index + 1) * degree_denominator + degree_numerator)
                     * argument_numerator)
        denominator = degree_denominator**2 * (index + 1)**2 * argument_denominator
        products = lower * numerator, upper * numerator
        lower = min(products) // denominator
        upper = ceiling_divide(max(products), denominator)
        partial_lower += lower
        partial_upper += upper
    endpoint_magnitude = max(abs(lower), abs(upper))
    tail = Fraction(endpoint_magnitude, scale) * argument / (1 - argument)
    enclosure = (Fraction(partial_lower, scale) - tail,
                 Fraction(partial_upper, scale) + tail)
    return {
        'degree': str(degree), 'steps': steps, 'scale': scale,
        'term_lower_scaled': lower, 'term_upper_scaled': upper,
        'sum_lower_scaled': partial_lower, 'sum_upper_scaled': partial_upper,
        'tail_bound': str(tail), 'enclosure': [str(value) for value in enclosure],
    }, enclosure


def exact_polynomial(degree, argument):
    term = total = Fraction(1)
    for index in range(degree):
        term *= argument * (index - degree) * (index + degree + 1) / (index + 1)**2
        total += term
    return total


def main():
    argument = Fraction(4095, 4096)
    records = []
    intervals = []
    expected = [(-Fraction(23, 10), -Fraction(227, 100)),
                (Fraction(181, 100), Fraction(184, 100)),
                (-Fraction(153, 100), -Fraction(150, 100))]
    for degree, outer in zip([Fraction(33, 64), Fraction(3, 2), Fraction(159, 64)], expected):
        record, enclosure = series_bounds(degree, argument)
        assert outer[0] <= enclosure[0] <= enclosure[1] <= outer[1]
        records.append(record)
        intervals.append(enclosure)
    minus, center, plus = intervals
    assert center[0] > 0 and minus[1] < 0 and plus[1] < 0
    products = [left * right for left in minus for right in plus]
    turan = center[0]**2 - max(products), center[1]**2 - min(products)
    assert turan[1] < -Fraction(6, 100)
    coarse_upper = Fraction(184, 100)**2 - Fraction(227, 100) * Fraction(150, 100)
    assert coarse_upper == -Fraction(97, 5000)
    controls = 0
    for degree in range(1, 7):
        for point in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
            _, enclosure = series_bounds(Fraction(degree), point, 16)
            assert enclosure[0] <= exact_polynomial(degree, point) <= enclosure[1]
            controls += 1
    assert (exact_polynomial(1, Fraction(1, 2))**2
            - exact_polynomial(0, Fraction(1, 2)) * exact_polynomial(2, Fraction(1, 2))
            == Fraction(1, 2))
    print(json.dumps({
        'arithmetic': 'Exact integers and rational numbers; outward floor and ceiling rounding',
        'argument': str(argument), 'mu': '3/2', 'delta': '63/64',
        'series': records, 'turan_enclosure': [str(value) for value in turan],
        'coarse_turan_upper': str(coarse_upper),
        'terminating_series_controls': controls, 'status': 'ALL_CHECKS_OK',
    }, indent=2))


if __name__ == '__main__':
    main()
