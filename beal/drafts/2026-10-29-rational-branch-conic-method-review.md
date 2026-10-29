# Rational-branch conic: constructive-method comparison

2026-10-29. One literature-only step; no point search, new theorem,
lemma change or mathematical script change. The governing assessment is
`drafts/literature/2026-10-29-rational-branch-conic-construction.md`.

## Gap and discriminating test

Residual Beal signatures and point control remain open. The sufficient
rank bound is one, whereas the current bound is at most four. The
intermediate target is an exact affine K-point with uv nonzero on L150's
mask-132102 rational-branch conic. This would supply one coordinate input
to Shukla's later pairing construction; it does not supply the M-point,
transported coordinates, cochains, pairing, rank improvement or points
on the original marked curve.

The review sought a concrete construction with finite work caps and exact
substitution verification. A cap is not a sufficient height bound. No
source inspected guarantees a point within the proposed cap. The chosen
continuation is therefore a bounded positive-certificate experiment,
not a complete soluble-conic solver.

## Inspected primary methods and qualifications

1. [Sage's number-field conic source](https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/schemes/plane_conics/con_number_field.py),
   develop version fetched 2026-10-29, `has_rational_point`, lines 259–303
   (also the [10.10 reference interface](https://doc.sagemath.org/html/en/reference/curves/sage/schemes/plane_conics/con_number_field.html)).
   Read the singular/zero-coefficient cases, both square-ratio cases,
   absolute-field transport, denominator scaling and relative-norm case.
   It handles number fields; `qfsolve` is explicitly restricted to Q.
   Its `local` branch cannot return a point. The general branch delegates
   arithmetic to `is_norm`; it is not an available pure-Python conic
   implementation. None of its square-ratio cases was tested here.

2. [PARI stable relative-field manual](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Relative_extensions_of_number_fields_and__backslashZ_K_minusmodules.html#rnfisnorm),
   `rnfisnorm` and `rnfisnorminit`, fetched 2026-10-29. The norm routine
   returns a decomposition into a norm times a residual factor. Its
   sufficient S-set contains ramified primes, class generators upstairs
   and target support. Galois status affects completeness; initialization
   flag 1 assumes it without checking. The [general-field warning](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html)
   requires certification for unconditional class/unit conclusions.
   L137's localized mod-two upper bound supplies neither these complete
   groups nor the groups of a new quadratic extension. A positive output
   could instead be accepted solely by exact norm and conic identities;
   unchecked negative output could not be accepted.

3. [Magma V2.29 handbook, 3 August 2026, Rational Points on Conics](https://magma.maths.usyd.edu.au/magma/handbook/text/1538),
   number-field algorithm description and `HasRationalPoint` contract.
   Number-field Lagrange reduction uses lattices and may fall back to a
   norm equation. The page gives no instance runtime or coefficient cap.
   Its bounded `RationalPoints` enumeration and Holzer bounds are stated
   over Q, not arbitrary number fields. They cannot certify exhaustion
   of this K-conic. The newer-looking `docs.magma-maths.org` search lead
   returned 404 on direct access; the cited official handbook was read.

4. Reused [Voight, author version 2019-05-21](https://jvoight.github.io/articles/quatalgs-051919.pdf),
   Algorithm 6.6, pp.25–26, and Theorem 6.11, p.27: local Hilbert-symbol
   computation and local-global existence do not extract global
   coordinates. No local test is repeated.

5. Reused the adequate Trager coverage in
   `drafts/literature/2026-10-28-surviving-witness-span-test.md` and
   reopened [Trager, SYMSAC 1976, pp.219–220](https://www.cecm.sfu.ca/~mmonagan/teaching/TopicsinCA11/TragerFactor.pdf),
   characteristic-zero setup and Theorem 2.2 with proof. Complete
   factorization requires complete rational factorization and a
   squarefree norm. Merely finding no proposed square root is not that
   algorithm. The selected continuation does not implement or invoke
   complete factorization and makes no nonsquare decisions.

Denis Simon's *Solving norm equations in relative number fields using
S-units*, Math. Comp. 71 (2002), 1287–1305, DOI
[10.1090/S0025-5718-02-01309-1](https://doi.org/10.1090/S0025-5718-02-01309-1),
remains an unread algorithm lead: the AMS PDF and CiteSeer mirror returned
403. His [author page](https://simond.users.lmno.cnrs.fr/) confirms the
publication and incorporation into PARI. The accessible 1998 thesis has
garbled extracted text; no theorem from it is claimed read. Search
snippets were used only for discovery. These sources are not essential
to the deliberately positive-only continuation below.

Narrow execution evidence: `command -v gp sage magma` found none on the
current PATH; system Python found no cypari2, Sage or SymPy. This does
not prove global unavailability. ATTEMPTS/045 and /052 preserve prior
backend blockers in different fields; they are relevant operational
evidence, not a ban on conic construction. No further availability sweep,
installation, remote computation or complete norm run is proposed.

## Chosen bounded construction interface

Use L150's displayed conic and full representative exactly. For a chosen
v, the quantity to submit to the existing square-root proposal routine
is `(q*v^2+9075-eta)/b`. This is the displayed conic rearranged for u²,
not a new conic-solubility criterion. The positive-output method reuses
L148/L149's implemented Decimal interpolation and rational reconstruction,
followed by exact arithmetic in Q[alpha]/A. No reconstruction bound is
asserted sufficient. Its availability is evidenced by the existing
standard-library implementations `branch_annihilator.py` and
`surviving_witness_span.py`, whose relevant routines were read here.

The proposed fixed domain is

    v=(a0+a1*alpha+a2*beta+a3*gamma)/d,
    ai in {-2,-1,0,1,2}, d in {1,2,3,5,6,10,15,30}, v!=0,

with L149's actual integral basis. At most 5000 tuples are submitted,
including duplicates before removal. Use at most 16 sign patterns per
tuple, hence at most 80000 interpolations of size 4 by 4. Cache the four
real-root proposals, each using at most 450 refinement steps; use
200-digit Decimal arithmetic and coefficient reconstruction denominators
at most 10^12, as in the existing proposal method. Cap all exact rational
numerator/denominator sizes at 8192 bits. These are explicit work caps,
not existence bounds. Decimal failures, singular numerical systems,
negative approximate evaluations and missing reconstructed roots are
unresolved candidates, never certified nonsquares. No precision or
domain enlargement is included.

An accepted positive certificate must contain exact power-basis u,v,
the full mask/product binding, nonzero u and v, and zero remainder for
`b*u^2-q*v^2+eta-9075` modulo A. Replay it using the actual maximal-order
basis and independent field arithmetic; retain full input hashes and
all actual/capped counts. A search failure cannot be an insolubility
certificate or an exhaustion statement about K-points. No complete
negative decision or guaranteed successful stopping bound is approved.

Continue to the independent replay only after an exact point is found.
If no point is accepted within this fixed domain/cap, preserve the
unfinished construction and park this direct-search experiment; another
turn needs materially new input or a different target, not a larger box.
This differs from ATTEMPTS/065's raw rational covering-model search and
does not reopen ATTEMPTS/066's epsilon pairing.

## Decision and remaining coverage

SPECIALIZE only for this bounded positive-certificate attempt. The
complete norm-solver route remains parked without an executable backend
and reviewed bounded execution plan. No new general theorem, novelty,
K-point, good-element coordinate certificate or Beal progress beyond
the checked sources is claimed. Mathlib coverage of this construction
was not checked; no absence claim follows.

This routine constructive continuation is not a creative mechanism.
No source-ready new central mechanism was identified in this focused
review; the remaining concrete bottleneck is still explicit coordinates.
The newly covered continuation requires the supervisor's separate
next-turn approval. This completed literature step runs no calculation.
