# A rational counterexample to Karp's fractional-degree Legendre Turán conjecture

Haobo Ma (ChronoAI Pte Ltd, Singapore), followed by Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore). CC BY 4.0.

## Result

For `F_nu(y) = 2F1(-nu, 1+nu; 1; y)`, the triple `mu=3/2`, `delta=63/64`, `y=4095/4096` satisfies

`F_mu(y)^2 - F_(mu+delta)(y) F_(mu-delta)(y) <= -97/5000 < 0`.

All degrees are positive. The central function value is positive and both shifted values are negative. This refutes Conjecture 4 on physical page 52 (also pages 53–54) of [Karp's 2011 SF21 slides](https://math.nist.gov/~DLozier/SF21/SF21slides/Karp.pdf).

## Rebuild

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a standard LaTeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is embedded in `note.tex`; no BibTeX pass or external data is required. The packages are `geometry`, `amsmath`, `amssymb`, `amsthm`, `booktabs`, `array`, `fontenc`, `lmodern`, and `hyperref`.

## Exact computation

Python 3.10 or later, standard library only:

```sh
python3 check_bounds.py > bounds-rebuilt.json
diff -u bounds.json bounds-rebuilt.json
```

The JSON ends with `"status": "ALL_CHECKS_OK"`. The computation uses outward integer rounding at scale `10^12` through term 10000 for each of the three degrees, and a proved geometric tail bound. It also checks 18 exact terminating-series values. `bounds.json` contains the scaled integer endpoints, rational tail bounds, and a strictly negative rational enclosure of the Turánian. No floating-point arithmetic is used.

## Mathematical coverage

The note gives the recurrence invariant and the infinite-series tail argument. Its written corollaries establish strict negativity on an open neighborhood and positivity near zero for each fixed admissible pair of parameters. The zero-balanced continuation formula, [DLMF 15.8.10](https://dlmf.nist.gov/15.8.E10), gives

`T(mu,delta,y) = sin(pi*delta)^2/pi^2 * log(1-y)^2 + O(abs(log(1-y)))`

as `y` tends to one for each fixed admissible pair. Thus the comparison is positive sufficiently near both endpoints, and the rational parameter pair has at least two distinct interior zeros. At shift one, the leading logarithmic terms cancel and

`T(mu,1,y) = -2*sin(pi*mu)^2/[pi^2*mu*(mu+1)] * [-log(1-y) + h_mu - 2] + o(1)`,

where `h_mu = 2*psi(1) - psi(-mu) - psi(1+mu)`. For every positive noninteger `mu` this tends to negative infinity. Continuity in the shift gives negative interior values for all shifts sufficiently close to one from below. If `mu>1`, the three degrees are positive. The proof does not classify all zeros or positive-valued restrictions. All additional statements are labeled as consequences, not as separately posed conjectures.

The fixed [FractionalLegendreTuran.lean](https://github.com/the-omega-institute/trureturing/blob/b8d708b1b89112061f30f218f031c1bf3672ebd8/D5/S3/Analytic/GaussZeroBalanced/FractionalLegendreTuran.lean) exports `D5.S3.Analytic.GaussZeroBalanced.FractionalLegendreTuran.result : ¬ claim`, the negation of the fully quantified strict comparison. Its private `minus_enclosure`, `center_enclosure`, and `plus_enclosure` declarations give the three rational intervals, and `witness_negative` proves strict negativity. In the same prefix namespace, [Defs.lean](https://github.com/the-omega-institute/trureturing/blob/b8d708b1b89112061f30f218f031c1bf3672ebd8/D5/S3/Analytic/GaussZeroBalanced/Defs.lean) defines `Defs.gauss` as the real Gauss hypergeometric function, and [Series.lean](https://github.com/the-omega-institute/trureturing/blob/b8d708b1b89112061f30f218f031c1bf3672ebd8/D5/S3/Analytic/GaussZeroBalanced/Series.lean) proves `Series.coefficient_recurrence` for a positive denominator parameter. The non-strict consequence, continuity, endpoint expansions, noninteger-degree family, and two-zero consequence are written proofs in the note. The recurrence evaluations and polynomial controls are finite exact checks. The complete source-item mapping is in the note's coverage table.

## Files

- `note.tex`: main source, complete argument, embedded bibliography.
- `check_bounds.py`: exact recurrence and finite controls.
- `bounds.json`: exact arithmetic output.
- `metadata.json`: title, creators, license, problem identity, mathematical coverage.
- `README.md`: build and checking instructions.

The matching readable PDF is `note.pdf`.

## Polynomial siblings

The coverage discussion also explains the geometric equality boundary of the polynomial conjectures on slide 31. For `f_k=c*r^k`, the rising-factorial Vandermonde identity makes that polynomial identically zero. This is the scaled equality case already in [Karp, arXiv:1203.1482v1, Lemma 3](https://arxiv.org/abs/1203.1482v1). His Theorem 1 proves the positive-coefficient result for `alpha=beta=1` under strict log-concavity. Those polynomial results are credited to Karp; the general strict cases and the other non-Legendre conjectures are not covered by the note.
