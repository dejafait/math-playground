# L101 audit: separate source comparison

2026-10-21, step 395. Literature only; source coverage approval, not a
critical mathematical audit or a new proof. Reuse the exact-target
search record in `2026-10-21-complex-derivative-sources.md` in this folder.
Additional literature reason: the new L101 specialization requires the
separate audit-scope approval requested by the startup gate; no changed
mathematical target, discovery search or installed-backend claim.

The main gap remains rank equality for arbitrary analytic order >=2.
The intermediate target is the unchanged critical audit of L101 at
M=Y=128, without derivative evaluation. A successful later audit could
support a finite complex upper-bound certificate alongside L099's
rational lower bound. It would reproduce a known fixed case already
covered by L035, changing provenance rather than solving a new BSD case.

## Inspected primary coverage

Reopened Cremona, *Algorithms for Modular Elliptic Curves*, corrected
second edition (1997), Section 2.13, printed pp.42–43, the Mellin proof,
integration-by-parts passage and Proposition 2.13.1
([primary chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=36)).
The proposition assumes a weight-two newform, analytic order at least r
and Fricke eigenvalue (-1)^(r-1). It supplies the 2r! identity and its
G_r kernel, not a fixed numerical tail bound. Its preceding completed-L
argument explains why lower vanishing matters. Audit exact applicability
against L030/L031/L099 and foundations/02; do not reprove the identity.

Reopened Wuthrich, *Numerical modular symbols for elliptic curves*,
arXiv:1608.06423v2, PDF dated 24 March 2017, Lemma 4 and full geometric
remainder proof, printed pp.6–7; Section 4.1, printed p.8
([primary version](https://arxiv.org/pdf/1608.06423v2#page=9)).
The proof explicitly uses |a_n|<=n for the elliptic newform; the sign
passage applies here at the single semistable prime. Do not extrapolate
its sign sentence to a general product of bad primes. The cited Section
4.1 page in L101/prior notes is off by one: printed p.8 is PDF page 9.
The source does not certify logarithm-weighted derivative remainders.

Reopened NIST DLMF version 1.2.8, released 2026-09-15, equation 4.5.4
([primary equation](https://dlmf.nist.gov/4.5.E4)), with positive-real
hypothesis. It supplies the logarithm inequality, not L101's constants.
Reopened Wiles's official description, printed p.4
([primary statement](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=4)):
the rank theorem has analytic order zero or one as hypothesis. It does
not assert a rank-two converse. Its use with L099 is an audit obligation.

Reopened Johansson, arXiv:1802.07942v1 (22 February 2018), Section 2
and 2.1, printed pp.2–3, including the complete four-step algorithm,
analytic-domain test, quadrature error case and tolerance qualifications
([primary paper](https://arxiv.org/pdf/1802.07942v1#page=2)).
Reopened the official FLINT source documentation, callback, integration
and accuracy sections, lines 13–58 and 89–169
([official source](https://raw.githubusercontent.com/flintlib/flint/main/doc/source/acb_calc.rst)).
The path must be finite and its integrand bounded; order-one callbacks
must enclose the function on the whole requested domain and certify
holomorphy, returning nonfinite values otherwise. Improper tails are
external. Accuracy settings are guidelines, so actual returned radii
must be checked. Johansson's branch-cut case explicitly includes log.
These are general finite-integration inputs, not a ready kernel backend
or guarantee that specified output widths will be attained. FLINT main
is mutable, accessed today, with no installed-version compatibility claim.

## Coverage decision and remaining test

SPECIALIZE approves a REPRODUCTION audit of the unchanged TARGET.
The canonical L101 was read completely to match its claims with these
inputs, without independently verifying its inequalities this turn.
No essential source is blocked. The unsuccessful screenshot retrieval
for Wuthrich's sign page is superseded by the inspected complete text
passage; the coefficient proof and exact single-prime case were read.
No additional unread lead is needed for this proof-only scope.

The independent audit must check every rational comparison in both full
remainders against the claimed <2^-43 radius and original 2^-30 goal,
all parameter-domain and lower-vanishing hypotheses, the |S'|<200 bound,
and B=2^-43+200*delta+4*sum(|a_n|/n)e_n+eta. Check radii versus widths,
signed arithmetic, callback branches and conditional-output wording.
These are recorded claims awaiting audit, not results re-established here.
Continue only if all pass; otherwise preserve L101 and identify a precise
repair or obstruction before proposing any finite replay. No cutoff
change, implementation or derivative calculation is authorized.

Compared local duplicate/failure evidence: L035 already imports the fixed
complex order; L031's unweighted twist tail is not this derivative budget.
ATTEMPTS/043 stops a general complex-to-p-adic import, and ATTEMPTS/045
stops a different order-table implementation. Both remain unchanged and
supply no obstruction to this independent proof audit. No source settles
uniform input production, the arbitrary-curve rank gap, full Sha finiteness
or the refined formula. Mathlib matching/supporting coverage is not checked.
