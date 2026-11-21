# Centered theta additive factors: common-symbol stop

The approved degree2/3 test gives a strict necessary-condition failure.
The canonical derivation and qualifications are in
[L825](../lemmas/L825-centered-theta-additive-factors-appell-obstruction.md).
The entire derivative defect is the constant Delta in (9.582501,9.582502),
where a common constant-coefficient symbol requires exactly zero.
Full certificate: `scripts/central-jacobi/centered-appell-629.json`,
27 finite checks, no failures, under the inherited L778/L791 contracts.
The separate step631 finite audit passes under those inherited contracts:
`scripts/central-jacobi/audit-631/audit-report.json`, 100 checks, no failures.
All coefficients and the strict full enclosure survive; this is local
validation of a known-method specialization, not a new general theorem.

**WHY IT FAILS.** Centering before additive inversion does not make the
unique monic factors degree-compatible: the cubic factor's derivative
differs from three times the quadratic factor. Thus one fixed-coordinate
formal constant-coefficient differential symbol cannot realize both.
Do not repair this test by independent degree dilations, reversal or a
degree sweep. This excludes neither degree-dependent symbols nor a
variable-coefficient realization, individual factor real roots, other
positive realizations, mixed/shifted positivity or RH. Reopening this
common-symbol bridge requires a materially changed mechanism and a new
independently testable claim, with its own source coverage; the historical
stop does not ban other theta work.

Recovery decision, step631: close this finite compatibility/audit sequence;
do not repeat its source retrieval, replay or adjust normalization. Compared
three mechanisms: (1) common-symbol lowering is now strictly obstructed;
(2) automatic Laguerre-adjoint closure retains the unpaid signed forcing
and boundary obligations recorded in its existing stop;
(3) an actual-kernel endpoint asymptotic test of L821's normalized Q_3
uses a different observable and can test a necessary global translation
condition without inverting polynomials. Select (3) for separate source
coverage only. It is not a parameter/minor sweep, does not reopen automatic
variation-diminishing transfer, and leaves lower oscillation and all-degree
signs open. The new assessment is REVIEW_REQUIRED; no endpoint asymptotic
has been calculated or approved here.
