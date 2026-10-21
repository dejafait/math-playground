# Finite-witness replacement in the fixed rank squeeze — scope approved

TARGET: Certify rank E(Q)=ord_T f_X=ord_T L_7=2 and finite 7-primary Sha for E=[0,1,1,-2,0] using L004, L030, L033 and audited L099, without published rank, saturation or Sha premises.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready 2026-10-08-concrete-independent-point-certificate.md assessment and searched the exact local L004/L030/L033/L034/L099 inputs, normalization chain and recorded stops; directly retrieved Stein–Wuthrich Sections 3, 6 and 7 for the changed provenance comparison. No new discovery search or novelty claim.
SOURCE_EVIDENCE: Stein–Wuthrich, Math. Comp. 82 (2013), 1757–1792, Section 3 pp.1761–1763, Section 6 pp.1775–1776 and Theorem 6.1, Proposition 7.2 and Kato Theorems 7.3–7.4 p.1778, and Section 7.1 p.1779; exact primary statements inspected on 2026-10-21. Reuse foundations/03–05 and the prior assessment for the unchanged control, convergence and published-overlap coverage.
COMPARISON: L034 already proves the same fixed conclusion using a published basis; Section 7.1 already illustrates the point/coefficient method. The sole authorized difference is replacing L034's point premise by audited L099, while retaining L030/L033 and their existing source qualifications.
GAP: Coverage is ready for a separate L004 application; no new upper-bound theorem, finite arithmetic replay or squeeze is established in this literature turn. Arbitrary complex-order comparison, uniform certificate production and full Sha finiteness remain open.
REASON: The exact independent-point requirement matches audited L099, and the remaining arithmetic and primitive-series hypotheses are unchanged from the assessed and audited fixed application. Specialization is justified to document the replacement provenance, not to reprove the known theorems or claim a new fixed rank result.
LITERATURE_REASON: The target changed from rational independence to a cyclotomic upper-bound application and primary-Sha finiteness; the pending assessment required a separate theorem-level applicability and overlap review.
SCOPE: Only the exact TARGET on [0,1,1,-2,0] at p=7, with the classical cyclotomic dual and L033's unchanged primitive series; no complex analytic order, primary-Sha order, basis, saturation or larger-family conclusion.

## Main gap, intermediate target and decision test

The main target gap is rank/order equality for arbitrary E/Q of analytic
order at least two. The fixed intermediate target tests whether the finite
witnesses reach L004's matching threshold without a published rank input.
Its downstream use is a certificate assembly with independently supplied
lower and upper bounds. This is reproduction of a known fixed result,
not progress beyond the checked literature or a BSD candidate.

Continue with the separate application only while L099 supplies exactly
the rational independence required by L004 and L033 supplies the same
primitive coefficient. If either scope fails or an excluded global input
reenters, stop and identify that missing premise. Full Sha finiteness,
complex order and uniform production remain independent unresolved tasks.

## Primary theorem comparison

The primary text is Stein and Wuthrich, *Algorithms for the arithmetic of
elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013), 1757–1792,
DOI 10.1090/S0025-5718-2012-02649-4,
[author offprint](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf).
The retrieved version is the 36-page published offprint.

- Section 3 retains non-CM throughout. Pages 1762–1763 specify total real
  period, unit-root measure, trivial Teichmuller branch and the coordinate
  T=kappa(gamma)^(s-1)-1, with finite polynomials using 1+p.
- Section 6 defines the classical all-place Selmer dual. At good ordinary
  reduction it is finitely generated torsion. Theorem 6.1 states the
  characteristic-order lower bound and characterizes equality by finite
  primary Sha and nondegenerate height; these are conclusions of the
  equality criterion, not extra premises for the proposed application.
- Proposition 7.2 handles passage from residual to p-adic surjectivity
  for p>=5. Theorem 7.3 gives integral divisibility in the surjective
  semistable case; Theorem 7.4 permits a power of p in the other case.
  Foundations/05 already records the resulting inverted-p formulation.
- Section 7.1 uses independent points and a p-adic order upper bound
  in a worked example. This is existing methodological coverage.

Kato's original Theorem 17.4 is cited through this inspected published
elliptic-curve translation; no fresh original-proof reading is claimed.
The unchanged Mazur-control and Kummer coverage in foundations/03 and
L002/L003 is reused. No reverse main conjecture or conjectural p-adic
BSD formula is needed. No new theorem proof is attempted here.

## Exact local applicability and excluded premises

L004 requires independent images in E(Q) tensor Q, not a basis or
saturation. L099's completed separate audit supplies precisely those
images for P=(0,0), Q=(1,0). It uses L081/L096/L097 and the local
reduction/logarithm argument only; L096's reference to L083 cannot
import L083's global rank/Sha assembly. L099 explicitly justifies its
torsion removal and the identical R=Q-4P in the local and global tests.
L034 and L082 are comparison records, not premises of the replacement.

L030 supplies the exact minimal model, discriminant 389 and non-CM.
L033 supplies good ordinary p=7, trace -5 and the audited strict bound
v_7(a_2-13/256)>=1>v_7(13/256)=0. Its fixed coordinate has
kappa(gamma)=8; it retains the primitive ordinary series, trivial branch
and total minimal real period of foundations/05. Its all-level C=0
comes from audited L032's full-relative normalization, not sample values.
These are existing certified inputs, not calculations repeated here.

The normalization chain uses L031's independent twist ratio and published
optimality/Manin and denominator inputs. L031's model/optimality lookup
explicitly excludes its rank column. These source qualifications remain;
replacing the independence proof does not make all arithmetic provenance
independent of published computational results. None is a published rank,
saturation or Sha premise. L081's historical L034 point provenance is
also unnecessary for membership, which follows by substitution.

The future application should cite L004 rather than reprove Kato,
control, coefficient convergence or the independence criterion. Finiteness
of 7-primary Sha must remain distinct from its vanishing or known order,
and from full Sha finiteness. Lower-coefficient vanishing is a possible
conclusion, never a premise inferred from finite approximate zeros.
No mathematical application of the squeeze is made in this assessment.

## Duplicates, stops and coverage limits

The ready 2026-10-08 assessment and audited L034 establish the stronger
published-basis overlap; no novelty is inferred. L033's complete audit
is reused without rerunning its scripts. ATTEMPTS/043 concerns a different,
unavailable complex-to-cyclotomic production implication. ATTEMPTS/045
and its step-371 implementation stop remain untouched; neither is reopened
by this fixed certificate assembly. No new lemmas or scripts are written.

Full matching Mathlib coverage: not checked, as recorded in L004 and
L099. No library-absence or formal-verification claim is made. The next
turn may perform this exact known-method specialization under the present
assessment; any enlargement of target or hypotheses requires review.
