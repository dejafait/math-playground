# Lemma 781: fixed reciprocal-tail Taylor inertia — nondiscriminating test

## Hypotheses

Use L777's actual normalization b=p/F and L779's repaired and audited
fixed pair (r,R)=(3,2048). In particular P(z)=(z-alpha_1)(z-alpha_2),
F(z)=G(2048z)/P(z), p(z)=z^-2 P(z). L779 certifies the two distinct
real simple interior zeros and zero-freeness of F on a neighborhood of
|z|<=9/8. This is local grouping, with no global real-zero hypothesis.
Let beta_n be b's real Laurent coefficient at index n>=1; “positive
index” does not mean a positive coefficient value.

Retain L779's analytic and trusted arithmetic qualifications: the
theta/Cauchy and contour reasoning, directed Decimal/mpdecimal finite
arithmetic, and correctly rounded exp/sqrt widened by adjacent values
under its documented backend contracts. The installed executable is not
independently attested or formally verified. Use the repaired audit copy
`scripts/actual-fredholm/audit-439/independent-phase-certificate-437.json`,
not the failed recursive-phase coefficient certificate. No new evaluator
replay, precision increase or parameter change is assumed here.

## Conclusion

For h_3(z)=sum_(n>=0) beta_(4+n) z^(n+1), g_3=-h_3, define

    H=(-beta_(4+i+j))_(i,j=0)^2.

The complete error-inclusive inertia is

    (n_+(H),n_-(H),n_0(H))=(2,1,0).

This misses the nominated obstruction threshold n_-(H)>=2. It neither
rejects nor establishes the optional generalized Nevanlinna premise
g_3 in N_1. No half-plane membership, prescribed J-Q inertia, mixed-minor
sign, new general sign theorem or RH conclusion follows. The fixed
diagnostic is closed without an automatic larger-matrix or precision test.
This is a known-method reproduction/specialization, not a claim of
progress beyond the inspected source results.

## Proof

**Known necessary condition and indexing.** Import Song–Hao–Hu–Chen,
*Some Propositions on Generalized Nevanlinna Functions of the Class N_k*,
Advances in Mathematical Physics (2014), Article605492,
[publisher PDF](https://onlinelibrary.wiley.com/doi/pdf/10.1155/2014/605492),
expansion(66) p.9 and Theorem14 with its complete proof p.10.
As recorded in the pre-existing assessed source comparison, if f is in
N_kappa and at a real t has the real nontangential expansion

    f(z)=h_-1+sum_(j=0)^(2m) h_j(z-t)^(j+1)+o((z-t)^(2m+1)), m>=1,

then the real Hankel matrix (h_(i+j))_(i,j=0)^m has negative index at
most kappa. Membership includes the global half-plane meromorphic and
negative-square hypotheses; local real analyticity does not supply it.
Only this necessary implication is used, with membership left unproved.

L777's bound |beta_n|<=M_b(9/8)^(-n), with finite M_b supplied by L779,
makes h_3 holomorphic for |z|<9/8. Its real Taylor series at t=0 gives

    g_3(z)=-beta_4 z-beta_5 z^2-beta_6 z^3-beta_7 z^4-beta_8 z^5+O(z^6).

Thus m=2, h_-1=0 and h_j=-beta_(4+j), j=0..4, agree exactly with
the cited convention. The analytic remainder is o(z^5) also for
nontangential approach. This justifies the tested H; it does not invoke
the theorem's converse or assert such a converse.

**Complete coefficient input.** In the repaired certificate, array
index n-1 in `signed/beta_enclosures` contains beta_n. Its complex
`DFT_enclosures` enclose the full finite Fourier average. The complete
alias upper bound in `DFT_alias_errors` was added before extracting the
real enclosure. L779 proves that no negative mode aliases into indices
4..8, since the only negative Laurent indices are -2,-1 and L=2048.
Its absolute Laurent convergence, independent modular Fourier phases,
root/factor/evaluator uncertainty and directed arithmetic are retained.
The separate analytic audit in L779 pays those inherited obligations;
they are not rederived by the present finite computation.

For each n=4..8, the exact saved midpoint hat_beta_n and upward
epsilon_n obey |beta_n-hat_beta_n|<=epsilon_n. The present computation
checks, as exact rational inequalities, that the recorded rectangle
contains the real DFT interval widened by the full alias upper bound,
that the imaginary DFT interval so widened contains zero, and that
[hat_beta_n-epsilon_n,hat_beta_n+epsilon_n] contains the complete real
rectangle. It uses this latter, possibly wider, interval for every entry.
Full selected rectangles, complex DFT intervals, hats, errors and aliases
are saved under `selected_inputs` in the new certificate below. Their
complete values were inspected; no preview or floating eigenvalue is
used as mathematical evidence. For readability, the resulting H is
contained entrywise in the following outward rational decimal intervals:

| Entry | Lower endpoint | Upper endpoint |
|---|---:|---:|
| H00 | 371.8106327354 | 371.8106327355 |
| H01=H10 | -488.6274904775 | -488.6274904774 |
| H02=H20=H11 | 507.1828638127 | 507.1828638128 |
| H12=H21 | -401.1979637630 | -401.1979637629 |
| H22 | 186.4352758419 | 186.4352758420 |

The computation uses the complete input intervals, not these rounded
display bounds. Correlations among repeated beta_n do not invalidate
interval inclusion; the independent entry boxes enlarge the allowed set.

**Rational congruence certificate.** Write a=H00, b=H01, c=H02,
d=H11, e=H12, f=H22. Define exact quantities

    q11=d-b^2/a, q12=e-bc/a, q22=f-c^2/a,
    p0=a, p1=q11, p2=q22-q12^2/q11.

All endpoints are finite decimal rationals parsed as exact fractions.
Addition/subtraction use endpoint sums/differences, products use all four
endpoint products, and squaring includes zero if the interval meets zero.
Division is allowed only when the entire denominator interval avoids
zero; its reciprocal endpoints are reversed, including for negative
intervals. Apply these inclusion operations in the displayed order.
The full exact rational enclosures give these outward display bounds:

| Pivot | Lower endpoint | Upper endpoint |
|---|---:|---:|
| p0 | 371.8106327354 | 371.8106327355 |
| p1 | -134.9634424769 | -134.9634424768 |
| p2 | 16.2292275256 | 16.2292275257 |

In particular both pivot denominators avoid zero for every allowed
entry choice. Their respective distances from zero exceed 371, 134,
and 16, versus the required strict bound 0. No uncertainty can change
these signs. For the actual entries the standard LDL congruence is

    H=L diag(p0,p1,p2) L^T,
    L=[[1,0,0],[b/a,1,0],[c/a,q12/q11,1]].

L is invertible since it is unit lower triangular. Import Sylvester's
law of inertia for real symmetric matrices under invertible real
congruence. The signs +,-,+ therefore give exactly two positive
eigenvalues, one negative and no zero. This is an application of the
known law, not a reproof. In particular n_-(H)=1<2, so the cited
necessary N_1 bound is respected by this one finite test. Respecting
one necessary bound gives neither global membership nor any conclusion
about the separate projection-weighted/coupled matrix.

**Evidence and limits.** Implementation:
`scripts/actual-fredholm/taylor_index_444.py`.
Full certificate:
`scripts/actual-fredholm/taylor-index-certificate-444.json`.
Run `python3 scripts/actual-fredholm/taylor_index_444.py` at a fresh output
path (change OUTPUT first); it refuses to overwrite prior evidence.
It records the input SHA256, all five complete selected coefficient/error
records, every matrix/Schur/pivot rational interval, sign margins, exact
inertia, actual/required negative-index threshold, and an empty failure
list. The status NONDISCRIMINATING describes failure to obstruct N_1,
not a failure of arithmetic certification. No full certificate replay,
radius/order sweep or new general theorem was performed. Independent
review of this new finite certificate remains a possible future audit;
the old arithmetic contracts are not upgraded by its successful execution.
Global class membership, exact projection weighting, J-Q comparison,
growing orders/radii, complex/multiple grouping and all mixed signs
remain unresolved.

## Mathlib

Full matching coverage for this actual finite-data certificate and the
Song et al. specialization has not been checked; no absence is inferred.
The informal imports are the precisely cited Taylor-index theorem,
Sylvester's law of inertia, and elementary rational interval inclusion.
This is not a Lean or independently attested arithmetic verification.
