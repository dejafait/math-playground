# 96a1 two-adic whole-fiber feasibility — source assessment

TARGET: Determine whether the 96a1 entire fiber algebra over Q2 is realized by any scalar with common primitive fourth-power witnesses satisfying L032's two-adic conditions.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact 96a1/fourth-power, 96a1/2-adic/fiber, 96a1/fiber/11/Fermat and ordered cube/fourth/eleventh terms; inspected primary FNS rather than unrelated search hits. Narrow duplicate/failure checks covered L032, L034, ATTEMPTS/013,014,016 and history/131; no completed matching 96a1 test was located. Search failure does not establish novelty.
SOURCE_EVIDENCE: Inspected FNS final June 10, 2019 manuscript Section 7.2 pp.24-28, Table 5's exact 96a1 polynomial, Lemmas 7.3,7.5,7.6 and the global nature of Lemma 7.7; inspected Lemma 5.2's full statement/proof and ensuing local-twist passage pp.17-19. Reused the ready Clark/Milne whole-algebra and Hensel assessments named below.
COMPARISON: FNS supplies canonical entire-fiber transport, disk constancy and a local torsion-module comparison, but does not state this strengthened fourth-power existence result. Lemma 7.7 removes the disk through GRH-dependent global Selmer information, not a local algebra obstruction. General lifting theory covers a bounded specialization; no reproof of those theorems is needed.
GAP: Construct one common primitive witness and justify its entire-fiber identification, or certify a disk-uniform algebra mismatch. No factorization, witness, feasibility answer or unconditional integer exclusion is obtained in this review.
REASON: Essential changed-field and local-proof coverage is now inspected; the exact existing target is ready for one research attempt, while the independent global gaps remain.
SCOPE: The exact variable-scalar Q2 existence question below; full twelve-dimensional algebras, all factors, primitive common fourth-power witnesses, and L032's retained two-adic row. No GRH, global class computation, rank, Sha or Selmer/point equality is admitted.
LITERATURE_REASON: The changed 96a1 field and local cases were outside the prior ready 54a1 coverage; this turn supplies those missing essential comparisons.

## Exact proposed test

Let K_96 denote the degree-twelve field of the entire canonical fiber
at j(96a1) in FNS Section 7.2/Table 5, with its data and scope inspected below. Set A_2,96=K_96 tensor_Q Q2. Use L034's complete
projective modular map j on E0, whose structural definition does not
depend on the choice of twist. For finite s in Q2 outside {0,1728},
let B_s be the coordinate algebra of its entire scheme-theoretic fiber.

The proposed question is existence of one Q2-algebra isomorphism
B_s -> A_2,96 and one common nonzero a,b,c in Z2 with

    a^3+b^4=c^11,    s*c^11=1728*a^3,
    min(v2(a),v2(b),v2(c))=0,
    a=2 modulo 8,    b and c odd,
    s in -512+2048 Z2.

These are the two-adic conditions recorded in L032's 96a1 row and
scalar restriction. Conditions at three and real positivity are not
conditions on a Q2 witness. The scalar s is variable; it is not required
to equal the canonical j(96a1). No equivalence with the original
integer problem or the full modular twist is claimed.

## Relevance and stopping test

Main gap: unconditional emptiness of residual signatures, including
the five twists in ordered (3,4,11). A proof of emptiness of this
necessary local set could exclude 96a1 only after verifying its
original-solution transport; one exact whole-fiber realization would
retire that local-nonexistence test and supply a starting point for a
separately assessed descent comparison. A scalar residue or one point
on one factor is insufficient. The independent global gaps remain.

The next research turn may make one bounded feasibility attempt under
the inspected coverage below. A complete realization retires this
local-nonexistence test. A certified invariant mismatch uniform on the
retained disk decides emptiness; failed finite searches do not. If neither
threshold is reached, save the exact unresolved factor or lifting bound.
No answer to the feasibility question is derived in this source review.

Continuation inputs: L032's exact 96a1 row and scalar domain; L034's
complete map; FNS's exact 96a1 field and entire-fiber transport (inspected below); assessed local lifting inputs as applicable.
L033's 54a1 field is not K_96. No cross-notebook input is proposed.
Unresolved obligations are the specialized whole-algebra identification
and simultaneous witness construction under the strengthened fourth-power condition. No class
table, GRH, rank, Sha, Selmer/point equality or integer witness is
available. Mathlib coverage is not checked.

ATTEMPTS/013's failed polynomial boxes and missing certified class
data remain parked. ATTEMPTS/014 and /016 stop comparisons for the
54a1 algebra, not every twist. The new target does not reopen those
comparisons or renew the exploration budget. Its coverage is now SPECIALIZE;
no new lemma, witness or mathematical feasibility conclusion is recorded here.

## Primary source evidence and reusable inputs

FNS, *The generalized Fermat equation with exponents 2, 3, n*,
Compositio Math. 156 (2020), 77-113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[final manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
internally June 10, 2019; printed pages used throughout.
Section 7.2, p.24, identifies the canonical fiber through the Galois
set of all twelve cyclic order-eleven subgroups. Table 5, p.26, gives

    m96(X)=X^12-4X^11-264X^7+66X^6-132X^5-2112X^4
           -1320X^3-660X^2-6240X-8007.

Use Q[X]/(m96) as K96; its generator is not the modular x-coordinate.
Equation (7.2), p.25, asserts whole-fiber constancy on each listed disk.
Lemma 7.6, pp.27-28, assumes finite K/Q2 with no rational two-torsion
on X0(11), excludes the cusp domain, and starts with an existing point;
its non-near-1728 proof covers every root and reconstructs y uniquely.
It does not prove existence.
Lemma 5.2, pp.17-18, for prime p with (2/p)=-1, compares the full
G_Q2 modules up to an unramified quadratic twist, retaining the i2=5
symplectic case. The subsequent passage identifies the modular twists
up to quadratic twist. A specialization must verify the chosen row
and show that scalar twists preserve cyclic-subgroup Galois sets.
Lemma 7.7, pp.28-29, uses the global Selmer image under GRH.

The full Lemma 5.2 proof was read, including extension from inertia
through the maximal unramified subfield and the residual quadratic
ambiguity. It is imported as a named published result, with no
independent rerun of its source computations. Using its full local
module assertion is a possible alternative to explicit factor matching;
an inertia-only comparison or a single factor is insufficient. The
local version of canonical-fiber transport still needs its Galois-set
applicability argument in the research proof. This is the identified
specialization, not an established answer in this assessment.

Reuse [the ready complete-algebra assessment](2026-10-08-full-fiber-at-one-local-algebra.md)
for Clark ANT II Theorems 2.38 and 2.41 (pp.80-82), Milne ANT v3.08
Theorem 7.33 and Proposition 7.50 (pp.121-123,127-128), and Hensel
criteria. These cover characteristic-zero separable local algebras,
coprime factor lifting and unramified classification. Matching e,f
pairs alone does not identify ramified fields. Clark's coefficient
stability theorem has an existential neighborhood, not a supplied
precision cutoff. An explicit comparison must certify all twelve
dimensions and every factorwise isomorphism.

Reuse foundation 17: Clark ANT II Theorem 1.79, p.58, requires a
complete valued field, integral polynomial and approximation with
|f(alpha)|<|f'(alpha)|^2. Unit cube/eleventh equations at two may use
it after verification; fourth-root surjectivity is not an input.
The ready two-adic assessment also records Clark's Eisenstein and
integer-ring criteria if needed. These inputs retain the same
hypotheses when the explicit field changes. Do not apply foundation
17's odd-prime unit-product formula as written to p=2.

The LMFDB 96a1 page failed to load and is not used. No canonical
j-number, local factor list or new root is inferred from that failure.
Search leads on exponent 25 and slides are outside the target and
were not used. Mathlib coverage of this full target and supporting
local torsion/fiber theorems is not checked.

## Bounded research permission and stopping threshold

Keep the exact TARGET unchanged. First try the inspected local
module-to-entire-fiber mechanism together with standard lifting of
one common witness; verify all row, primitivity and scalar identities.
If that mechanism cannot establish full transport, a complete certified
local factor comparison within the same feasibility question is covered
by the reused inputs. This is one attempt, not an invitation to iterate
search boxes. A new target or hypothesis outside this scope needs a
separate review. Save unresolved work before any lengthy computation.

A positive certificate needs one exact scalar, the same a,b,c for both
identities, all required residues, and an isomorphism of entire algebras.
A negative answer needs an obstruction for every scalar in the disk;
(7.2)'s constancy may be cited with its precise scope, but failing one
witness construction is insufficient. No connecting-image comparison
or global exclusion follows automatically. The approved continuation
uses L032 and the structural part of L034, not L033's 54a1 field.
