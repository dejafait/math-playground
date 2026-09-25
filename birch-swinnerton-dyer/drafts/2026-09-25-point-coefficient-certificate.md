# Point and p-adic coefficient certificate: focused test

Date: 2026-09-25. This save records unfinished reasoning before the source
check; no new mathematical conclusion is claimed at this point.

## Gap, intermediate target, and downstream use

The main target remains rank E(Q) = m(E) for every E/Q. The Clay page and
Wiles statement were rechecked today; the rank assertion and stronger
coefficient refinement retain the scope in the existing foundations.
For the ordinary cyclotomic route, L002 gives characteristic order
h = r + s + delta with two nonnegative defects. L003 removes them only
under finite p-primary Sha and nonzero cyclotomic regulator.

Test instead an independent lower bound from n rational points and an
upper bound from the T^n coefficient of the ordinary analytic p-adic
L-function. If the coefficient is rigorously nonzero and Kato's theorem
gives f_X dividing that L-function after inverting p, the proposed chain is
n <= r <= h <= ord_T L_p <= n. It would certify r = n and remove both
defects without assuming finite Sha or a nonzero regulator beforehand.
Producing the certificates for arbitrary curves, and proving n = m(E),
would still be unresolved. No analytic p-adic BSD formula is an input.

## Redundancy and prior failures

The finite Selmer obstruction in ATTEMPTS/001 does not include marked
independent rational points. ATTEMPTS/002 shows that characteristic data
and control alone leave a specialization defect. The proposed lower bound
adds arithmetic information absent from both countermodels. L003 supplies
a different conditional route; this test must not use its arithmetic
hypotheses as premises. The idea is a standard Iwasawa rank-certificate
mechanism, not a claim of novelty. Existing files and inactive branches
are preserved.

## Discriminating test

Check Kato's exact theorem, its divisibility direction, the classical
Selmer group, prime/reduction restrictions, and any representation or
non-CM assumptions. Use the primitive ordinary p-adic L-function and
record its normalization; a power of p is irrelevant to order at (T).
A certified enclosure excluding zero is enough for a coefficient; no
finite approximation alone proves that a coefficient is zero.

Continue this intermediate certificate if the checked theorem really
supplies h <= ord_T L_p and the inequalities close at n. Abandon that
inference if it uses the reverse divisibility, mismatched Selmer groups,
or a conjectural equality. A successful conditional certificate would
be an arithmetic input only; uniform production and the complex analytic
comparison must remain explicit.

## Completed test

The [source audit](../foundations/05-kato-divisibility.md) verifies the
upper-bound direction. In the retained non-CM scope, take p >= 5 good
ordinary. Theorem 7.3 covers surjective p-adic representation;
Proposition 7.2 supplies that hypothesis from residual surjectivity.
Theorem 7.4 covers residual nonsurjectivity up to an unspecified power
of p. Both give the same order inequality after inverting p. The
restriction p >= 5 makes this checked case split exhaustive without an
extra assertion at p = 3. The Selmer module and gamma conventions match.
The large original Kato PDF could not be retrieved; the exact elliptic
statements were read in the published Stein--Wuthrich paper.

The source's Section 7.1 already illustrates the certificate. This is
therefore a standard input newly connected to the notebook's defects,
not a new general theorem. [L004](../lemmas/L004-point-coefficient-rank-certificate.md)
proves the requested implication and the finite-precision nonvanishing
test. Its slightly more general form keeps k independent points and a
nonzero degree-n coefficient separate, so that an unmatched gap n-k
does not disappear in the conclusion.

The test succeeds at the exact arithmetic threshold k = n. Finite
p-primary Sha and nondegenerate height follow after the bounds close;
they are not premises. No computation on a particular curve was needed
for this theorem-and-deduction step. Producing certificates for every
curve and proving n = m(E) remain open in this notebook. The lower bound
is the part that can plausibly be supplied by a genuinely arithmetic
point construction, motivating the next direction recorded in PROGRESS.
