# Fixed complex derivative: inspected sources and remaining specialization

2026-10-21, step 392. Literature only. No new error estimate, numerical
enclosure, lemma or mathematical program is established here.

The main gap is arbitrary-curve rational rank equals complex analytic
order when that order is at least two. The immediate validation target
remains a finite outward enclosure excluding zero for the second
derivative of the conductor-389 curve. Its plausible use is independently
replayable complex upper-bound evidence alongside L099's rational lower
bound. L035 already covers the known fixed analytic order by citation;
this would change evidence provenance, not resolve another BSD case.

## Primary formula and exact applicability obligations

Read J. E. Cremona, *Algorithms for Modular Elliptic Curves*, corrected
online second edition (CUP, 1997), Section 2.13, printed pp.42–44,
including the Mellin-integral proof and Proposition 2.13.1 on p.43
([primary chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=36)).
Its hypotheses are a weight-two newform of level N, Fricke eigenvalue
epsilon=(-1)^(r-1), and analytic order at least r. Its conclusion is

\[
 L^{(r)}(f,1)=2r!\sum_{n\ge1}\frac{a_n}{n}
 G_r(2\pi n/\sqrt N),\qquad
 G_r(x)=\frac1{(r-1)!}\int_1^\infty e^{-xy}(\log y)^{r-1}\frac{dy}{y}.
\]

The proof distinguishes the completed function from L itself and uses
lower vanishing when removing its archimedean factor. Page 44 gives a
power series for G_r, including its r=2 polynomial, and distinguishes
exact vanishing from sufficiently accurate derivative nonvanishing.
Neither that series nor its suggested evaluation is an outward certificate
without finite-error control. The reviewed proof covers the required
formula; no reproof or new differentiation under an integral is needed.

For a later application, match r=2 and N=389 using L030. Use audited
L099 and the named analytic-rank-zero/one theorem in foundations/02 for
the lower-vanishing hypothesis; perform this applicability argument in
research, retaining holomorphy and the nonzero Dirichlet series. Do not
substitute L100's p-adic order or L035's published analytic order.

Read C. Wuthrich, *Numerical modular symbols for elliptic curves*,
arXiv:1608.06423v2 (PDF dated 24 March 2017; submission 23 March),
Lemma 4 and its proof, printed pp.6–7, and Section 4.1, printed p.9
([primary version](https://arxiv.org/pdf/1608.06423v2#page=7)).
The proof uses the all-n elliptic coefficient bound |a_n|<=n and bounds
the unweighted integrated Fourier tail by its full geometric series.
The sign convention in Section 4.1 is epsilon_Q=-a_Q for the present
single semistable prime. L031 has already certified a_389=1 on the
exact minimal model. Only its count/sign component is relevant here,
not its twist-five value or period normalization. This source is not
a theorem bounding a logarithm-weighted derivative remainder.

Read NIST DLMF Section 4.5(i), specifically equation 4.5.4,
log x<=x-1 for x>0
([equation and hypotheses](https://dlmf.nist.gov/4.5.E4)).
This is a standard comparison input for the proposed positive kernel
tail. Combining it with the two preceding sources is the identified
specialization still to be proved, not a new estimate proved here.

## Certified finite arithmetic and stronger algorithm comparison

Read FLINT's *acb_calc.h*, documentation headed 3.7.0-dev, the callback
contract, `acb_calc_integrate`, its accuracy qualifications and resource
options, and the local Gauss–Legendre error statement
([primary documentation](https://flintlib.org/doc/acb_calc.html)).
It gives rigorous enclosures on finite straight segments for bounded
integrands. An order-one callback must certify holomorphy on the supplied
complex domain and return a nonfinite enclosure when it cannot. A log
callback must handle its branch cut. Improper tails belong to the user;
accuracy goals and evaluation limits are not certified final widths or
hard execution limits. Inspect the resulting enclosure itself.

Read F. Johansson, *Numerical integration in arbitrary-precision ball
arithmetic*, arXiv:1802.07942v1 (22 February 2018), Section 2, printed
pp.2–4, for the primary algorithm, its analytic-domain test and finite
interval error guarantee
([primary paper](https://arxiv.org/pdf/1802.07942#page=2)).
The current documentation, rather than the older 2.9.0-git Taylor API
also encountered, controls a prospective implementation. No installed
integration backend was established: `python3` cannot find `flint` in
this environment. This is not an essential source blocker for a proof
of the error budget; it forbids assuming an executable replay is ready.

The general rigorous integrator is stronger numerical machinery than
uncertified point approximations of G_2. It does not remove the need for
the curve-specific formula, all coefficients, both infinite remainders,
parameter enclosures and signed sum. No full elliptic second-derivative
certificate API was inspected or imported. The Sage L-series page was
searched for derivative/rigor coverage but its returned text supplied
no usable theorem; no absence claim follows. DLMF Section 8.19 was an
inspected comparison lead about E_p, not an identification of G_2.

## Prospective bounded proof test, without numerical execution

Keep M=128 Fourier terms and truncate every positive kernel integral at
Y=128. These are proposed cutoffs, not certified adequate cutoffs.
Seek explicit rationally evaluable bounds for (i) the complete n>M
series and (ii) the y>Y portions of every retained term, with their sum
at most 2^-30. Prove their validity uniformly on a stated positive
outward enclosure of c=2*pi/sqrt(389). Keep all signs in the finite sum;
only remainders may be replaced by absolute majorants. Specify how
finite kernel, c, coefficient and summation errors would enter a final
enclosure, including failure or nonfinite output from integration.

This is one analytic specialization attempt. It may write the resulting
proof in a canonical lemma only if successful. It may not implement or
run derivative evaluation. Continue toward a separately approved finite
replay only if the full proposed analytic bound meets 2^-30 and all
finite-arithmetic obligations are explicit. If either bound fails, retain
the actual bound and park this schedule; no enlargement is authorized.
No computed derivative or expectation of successful exclusion is used.

## Duplicate checks, qualifications and search record

Reused the two 2026-10-08 fixed-order assessments, L035's relevant
convention/lower-vanishing discussion and history/094. The published
order import and its audit are complete and should not repeat. L031's
unweighted twist tail covers neither derivative kernel nor its weighted
remainder. ATTEMPTS/043 concerns a different, general complex-to-p-adic
comparison; ATTEMPTS/045's order-table source-adaptation stop remains
intact. Neither is a ban on this independent analytic error test.

Queries included “rigorous elliptic curve L function derivatives interval
arithmetic Arb second derivative Cremona G_r”; “G_2(x) Cremona bound”;
“G_r(x) L-functions tail”; “Numerical modular symbols Wuthrich Lemma 4”;
and targeted FLINT integration and DLMF logarithm-inequality searches.
These found established formula/evaluation methods, not evidence of
novelty. The formula and general numerical methods are known. The
identified difference is their complete, explicit finite-certificate
error budget at these fixed cutoffs. No original mathematics is claimed.

The proof test supplies neither an actual outward derivative interval nor
a nonvanishing theorem until a later calculation succeeds. Even that
fixed replay would not give uniform certificate production, arbitrary
analytic-order/rank comparison, full Sha finiteness or the refined BSD
formula. Mathlib matching and supporting coverage remain not checked.

## Step 393: separate source-link approval

2026-10-21. Reused the comparison above for the unchanged fixed-cutoff
proof target; no new discovery search was needed. Direct source URLs
were inserted into its assessment's SOURCE_EVIDENCE field. Reopened
Cremona's Proposition 2.13.1 and preceding Mellin cases, Wuthrich's
coefficient/geometric-tail passage, DLMF 4.5.4 and Johansson Section 2.
The rendered FLINT URL returned HTTP 403 on this retrieval. Its
[official repository documentation](https://raw.githubusercontent.com/flintlib/flint/main/doc/source/acb_calc.rst)
was read instead: callback requirements and the integration/accuracy
sections support the previously recorded contract. This mutable `main`
source was accessed on this date; no release pin or backend availability
is inferred. The inaccessible rendering is not an essential source
blocker for the proof-only target. No new estimates were derived.
