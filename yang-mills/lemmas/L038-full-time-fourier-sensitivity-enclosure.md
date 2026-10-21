# L038 — Full-time Fourier sensitivity lies below the retained budgets

## Hypotheses

Use exactly L035's cutoff-112 sensitivity S_i(eta), i=3,6, tau=1/16,
with eta=10^-12. Its approximate Fourier coefficients are the exact
complex dyadic values specified by L037's complete saved hexadecimal
table, not values regenerated in another environment. Keep L008's
relative normalized modes, L032's two pure potentials and exact axial
odd-frequency exclusion, and all four second-index components.

The weak operators and collected rational monomial products are those
in L035: Q_i^alpha at degree zero and N^alpha at degree one in L030's
formal stencil. The implementation reuses the exact rational expansion
`operators` and collection `product_terms` already used by L033–L035.
The formulas in L030(5)–(8) retain the incidence 1/24 corrections,
plane/link 1/8 averages, coefficient 1/6 corrections, symmetrization
and both probe subtractions. No numerical threshold deletes terms.

## Conclusion

For this specified table and the exact FULL infinite time integrals,

\[
 S_3(10^{-12})<0.074779<100,\qquad
 S_6(10^{-12})<0.280424<1000.                         \tag{1}
\]

L037 discharges L035's Fourier-input hypothesis. Consequently (1)
bounds the difference between the exact cutoff-112 pure-sector sum
I_(i,112) and its exact table-substituted counterpart Ihat_(i,112).
This does not enclose the signed counterpart itself. A reported value
still needs a separately established error E_i covering its weight and
tensor arithmetic. No sign, compensated power coefficient, complete
Ward logarithm, finite matching, reflected error <=c_box/2 or mass gap
is asserted.

## Proof

### Infinite time integration by a positive envelope

Let E_i(s,r) denote the sum of L035(6)'s nonnegative allowances over
all collected products, with their absolute rational coefficients,
without the overall factor 8. Expanding its finite coordinate sums
and nonempty perturbation subsets gives nonnegative coefficients
w_(k,ell,v) independent of s,r such that

\[
 E_i(s,r)=\sum_{k,\ell,v}w_{k,\ell,v}
                        e^{-s\lambda_k-r\lambda_\ell}.
\]

Every relative one-form has three positive sine indices. L008's
lambda=(pi/8)^2|k|^2 and pi>3 therefore give lambda>g_*=27/64
for both indices, including every allowed zero cosine. Hence

\[
 E_i(\tau+u,\tau+v)\le E_i(\tau,\tau)e^{-g_*(u+v)}
 \quad(u,v\ge0).
\]

L035's exact separated representation and elementary exponential
integrals now imply

\[
 S_i\le8E_i(\tau,\tau)
 \int_0^\infty ue^{-g_*u}\,du\int_0^\infty e^{-g_*v}\,dv
 =8(64/27)^3E_i(\tau,\tau).                         \tag{2}
\]

This uses neither a time window nor a numerical inverse-weight rule.
Both time tails are included. Finite sums and positivity justify every
interchange. The deliberately loose envelope is sufficient for (1).

### Outward weak-integral and heat tables

The generator uses integers scaled by S=10^80 and L036's outward
interval operations: multiplication takes the minimum/maximum endpoint
products divided by S with floor/ceiling; rational input division is
outward. Thus induction encloses each evaluated exact expression.
The complete L037 table is parsed as exact dyadics, each enclosed
outward, and its coverage is checked against h=0,1 and -224<=n<=224.
The certificate hashes that input file; no regenerated table is used.

An interval for pi is obtained from the standard Machin identity
pi=16 arctan(1/5)-4 arctan(1/239). The rational alternating sums
through j=79 and those sums plus term j=80 enclose each arctangent.
Its lower endpoint exceeds 3. For the zero cosine, let
z=floor(S/sqrt(8)), computed by integer square root. The exact checks
8z^2<=S^2<8(z+1)^2 enclose 1/sqrt(8) in [z,z+1]/S.
Positive sine/cosine amplitudes are exactly 1/4 for each exponential.

Here is the exact real-part calculation used for a weak integral.
Its left waves have p=+/-k for k>0 and p=0 for a zero cosine;
the right waves have q=+/-ell or q=0. A positive cosine wave has
phase i^p, and a positive sine wave has phase -i sign(p)i^p.
Argument derivatives multiply by (ip omega)^a and (iq omega)^b;
integration by parts contributes [-i(p+q)omega]^d. Extract the
common positive factor

\[
 f=\omega^{a+b+d}4^{-P}(1/\sqrt8)^Z,
 \quad P+Z=2,
\]

where Z counts zero cosine waves. For each wave pair, start with
integer coefficient p^a q^b(p+q)^d and phase i^(p+q+a+b-d).
For each sine factor, multiply the coefficient by its frequency sign
and subtract one from the phase exponent. Powers of i are EXACT
quarter-turns, so the real part selects Fhat's real/imaginary part
with the appropriate sign. Sum these interval-enclosed real terms
before multiplying by f. This encloses the exact approximate integral,
including cancellation; its endpoint absolute maximum supplies b_A.
A positive derivative of a zero mode, or an absent zero sine, gives
zero. Powers 0^0 are one. The exact parity test
h+d+a+b+lp+rp modulo 2, with lp=k for cosine and k+1 for sine,
is imposed before evaluation, as in L035.

The multiplier allowance d_A in L035(2) has upper bound given by the
same positive factor f times

\[
 \eta H_h\sum_{p,q}|p|^a|q|^b|p+q|^d.
\]

A zero cosine is represented by ONE wave of amplitude 1/sqrt(8).
All these expressions have nonnegative outward upper endpoints;
no cancellation is used to reduce a multiplier allowance.

For each frequency n=0,...,112, enclose
exp[-tau omega^2 n^2] by the alternating Taylor method described in
L037: reduce its nonnegative argument by powers of two to at most
1/8, bound exp(-x) between Taylor sums of orders 61 and 60, and square
outward back to the original argument. Terms decrease on that range.
The complete saved upper heat endpoints lie in [0,1]. No machine
exponential or floating-point value of pi is used as an enclosure.

For a pair of features, let integer b_1,b_2,d_1,d_2 be their scaled
upper bounds and let h_k,h_ell be the scaled heat upper endpoints.
The initial coordinate tables use the integer upper contributions

\[
 \left\lceil b_1b_2h_kh_\ell/S^3\right\rceil,
 \quad
 \left\lceil(d_1b_2+b_1d_2+d_1d_2)h_kh_\ell/S^3\right\rceil.
\]

Sum these over every coordinate mode pair. In the axial coordinate
k=0 and the right frequency is zero when allowed, or any positive
even frequency through 112; transverse coordinates keep their complete
positive/allowed-zero domains. The two axial parts may be combined
here because the upper bound is nonnegative. The four coordinate
upper tables enter L035(6) using outward nonnegative products.
Absolute collected rational coefficients are applied with upward
integer division and summed. This gives an upper bound for E_i(tau,tau)
by interval induction, not by empirical floating-point agreement.

### Complete finite evidence and bounds

Reproduce with

```sh
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_full_time_sensitivity_enclosure.py
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/audit_full_time_sensitivity_enclosure.py
```

The complete certificate is
`scripts/combined-ward-response/full-time-sensitivity-enclosure-certificate.json`;
the audit is
`scripts/combined-ward-response/full-time-sensitivity-enclosure-audit.json`.
All 1,293 coordinate feature records and 3,405 collected product records
are present. The audit reconstructs the rational operator products,
checks exact feature and term coverage without duplicates, independently
enumerates all fifteen nonempty subsets for EVERY product and checks
that the saved recurrence dominates them. It recomputes every recurrence,
rational coefficient contribution, total and final budget inequality.
There are no failures. Weak-integral table enclosures and Taylor heat
evaluation rely on the generator's outward induction above; the audit
does not independently reevaluate those tables. This is an informal
finite certificate, not proof-assistant verification.

Multiplying the saved integer totals by the exact rational factor
8(64/27)^3 and rounding upward gives decimal upper bounds

\[
 0.074778904027897264552804,\qquad
 0.280423339433096960540244.
\]

The complete load-bearing integer bounds and empty failure list were
inspected. Both decimal bounds are strictly below the rounded bounds
in (1), proving (1). L035(5) and L037 give the stated coefficient-error
consequence. The signed counterpart, all other Ward contributions and
the reflected comparison remain separate tasks.

General flow/matching inputs remain imported by their precise citations
and scope in `drafts/literature/2026-09-26-current-target.md`; none
supplies this numerical allowance. The elementary positive-envelope
specialization and outward implementation are needed for the actual
specified table, rather than a reproof of those general results. This
is local standard-method progress, with no originality claim beyond
the sources checked.

## Mathlib

Full matching coverage for this finite sensitivity enclosure: not checked.
Supporting spectral-gap exponential integrals, exact complex phases,
finite-product expansion and outward interval arithmetic: not checked.
No matching theorem or direct Mathlib link is asserted. Unknown coverage
is not evidence of absence; the certificate is not a formalization.
