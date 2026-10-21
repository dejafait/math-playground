# Normal-closure repair — complete different/conductor source comparison

TARGET: Assess whether L092-L095 cover IV Theorem 1.10(ii)'s pre-ell different/conductor increment log(2^11*3^3*5^2)<=21 for C_o in place of G_o, extracting the exact all-place inequality and any missing hypotheses.
CHECKED: 2026-10-20
DECISION: IMPORT
SEARCH_EVIDENCE: Step382 reused step364's repair searches and ledger, step368's reduction coverage, L090's field/conjugate setting, L092/L094/L095's actual statements and ATTEMPTS/035; fresh exact repair/conductor queries found no adequate repair theorem, while a tame-compositum search located Conrad Theorem 2.1. Queries and inspected passages are specified below; no novelty inference.
SOURCE_EVIDENCE: Fresh reading of IV April 2020 reproduction Definition 1.9 pp.21-22, Theorem 1.10 opening/definitions pp.22-23 and proof (ii) p.24, Proposition 1.3(i)-(ii) with proof pp.11-12, Proposition 1.8(v)-(vii) with relevant proof cases pp.19-21; Milne ANT v3.08 7.50-7.52 pp.127-129; Conrad Tame ramification and composite fields, Theorem 2.1 p.2 and proof reduction/Lemma 3.1 pp.2-3. Direct links below. IV reproduction authentication is unresolved.
COMPARISON: The printed estimate compares normalized absolute different plus the reduced selected-bad-place divisor over F and F_tpd, not an arbitrary full Neron conductor; L094-L095 match only the small-prime absolute different inputs. Tameness and unramifiedness off the conductor support for the changed field, followed by the weighted assembly, are not established by L092-L095.
GAP: First missing field assertion is actual C_o/T tameness outside {2,3,5}, with unramifiedness on the potentially-good locus; matching the source's selected support to the remaining ramification locus and performing the complete normalized sum remain separate obligations.
REASON: Import the exact source inequality, normalization and support requirements without asserting a repair; this changes the next test from another local different audit to remaining-place ramification.
SCOPE: IMPORT concerns the source requirements and existing-result comparison only; it does not import the desired all-place theorem for C_o or approve it as proved.
LITERATURE_REASON: The target changes from L095's two local bounds to the complete pre-ell different/conductor estimate, including global normalization, support and primes outside {2,3,5}; the existing local audit scope does not cover those identifications.

## Completed source review — 2026-10-20, step382

The main gap is original finite B>=A. This review's intermediate target
is TARGET. Its downstream use is to determine whether replacing G_o
by C_o loses the numerical input, rather than just its original
relative-degree proof. Continue only with a finite list of testable
same-field hypotheses; stop an unconditional assembly if a necessary
support or ramification assertion is missing. Missing coverage is not
a counterexample. No new mathematical result is derived here.

### Exact inequality, bases and normalization

Source: Mochizuki, *IUT IV*, April 2020,
[inspected reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
Printed page numbers are used. Theorem 1.10 proof (ii), p.24, states

    log(d_F) + log(f_F)
      <= log(d_F_tpd) + log(f_F_tpd) + log(2^11*3^3*5^2)
      <= log(d_F_tpd) + log(f_F_tpd) + 21.

The pre-ell base is F_tpd, not F_mod and not K=F(E_F[ell]). The
subsequent K/F increment 2log(ell) is a different assertion. F_tpd=T
is justified for the present survivors by L090; substituting C_o for F
in this inequality is the proposed application, not a source theorem.

Definition 1.9(i), pp.21-22, takes divisor degree by assigning a finite
place v the value log(#k_v), then divides by [F':Q]. Definition
1.9(ii) instead normalizes the portion over a rational prime p by
the sum of the local degrees above p. Theorem 1.10's definitions,
p.23, use the former normalized degree for the global quantities.
In local notation, the contribution of an absolute different exponent
a_v is a_v f_v log(p)/[F':Q]. Its absolute different order is
d_p(F'_v)=a_v/e_v, as in L094-L095. Thus the local-degree weights
to retain when reading the global definition are
[F'_v:Q_p]/[F':Q]; the reduced conductor coefficient has local
absolute order 1/e_v on its support, and zero elsewhere. These are
translations of the source definitions, not a new weighted estimate.

The divisor f_F' on p.23 has coefficient one exactly on
V(F')^bad=V_mod^bad x_(V_mod) V(F'). This is the selected q-parameter
support. It is not automatically the full elliptic Artin conductor or
the set of all bad reductions. Archimedean coefficients of these two
divisors are zero. A changed-field comparison must retain one fixed
support in the base and its complete inverse image upstairs.

### What the cited proof uses, and what is not yet supplied

Proof (ii) cites Proposition 1.3(i) at p outside {2,3,5}, where F/F_tpd
is tame by 1.8(vi),(vii), and 1.3(ii) at the three small primes using
the torsion-group degree allowance. Proposition 1.3(i), pp.11-12,
gives equality in its different formula for tame extensions. Tameness
alone does not say that different plus the reduced support divisor is
unchanged: one must also handle ramified places outside that support.
The theorem starts with initial theta-data and its stated good-reduction
condition, p.22; these hypotheses are not available for C_o merely
because L094-L095 pass. In particular, selecting the singleton above
three from a different construction is not a substitute for the present
survivor's complete support. The source's (D0), pp.24-25, concerns K
and excludes 2,3,5,ell; it must not be silently cited as an all-prime
unramifiedness theorem for this C_o.

Existing L094 and L095 give the local different allowances 10,2,1
above d_p(T_v), each with the additional 1/e(T_v/Q_p), at every
actual extending place. These are the inputs corresponding to the
printed prime exponents before the final conductor/weight assembly.
They do not perform that assembly, control p outside {2,3,5}, or
specify the selected support. L092's degree slack cannot supply any
of these missing statements. The factor-four relative degree excess
is retained; it is not a reason to multiply the printed constant by
four without analysis.

The first independently testable missing assertion is the remaining
local ramification statement in the following assessment:
`drafts/literature/2026-10-20-normal-closure-remaining-prime-ramification.md`.
It tests tameness and unramifiedness on the integral-j locus, without
assuming the still-unverified native support choice. Passing it would
leave support identification and the full weighted assembly unresolved.

### Literature comparison and bounded continuation

IV 1.8(vi), pp.19-21, applies to an actual Legendre equation over an
odd-residue local field: it becomes semistable over an extension of
degree at most two; in the potentially-good case its proof supplies
good reduction already over the original field. IV 1.8(vii) applies
to torsion of level invertible in the valuation ring: good reduction
gives unramified torsion and multiplicative reduction gives a tame
torsion field with ramification index dividing the level. Its proof
cites *Neron Models*, 7.4 Theorems 5 and 6. Import these assertions;
there is no reason to reprove them in the continuation. Reuse the
already-inspected Silverman VII.5.5 potential-good/integral-j criterion
recorded in `2026-10-20-normal-closure-local-two-degree-scope.md`.

For the normal-closure passage, [Conrad, *Math 248A. Tame ramification
and composite fields*](https://math.stanford.edu/~conrad/154Page/handouts/tamecomp.pdf),
Theorem 2.1 p.2, covers composita of finite extensions of the fraction
field of a complete DVR: a tame factor remains tame after arbitrary
finite base change, and two tame factors have tame compositum. Read
the theorem, its reduction to totally tame extensions and Lemma 3.1
on pp.2-3; no exact ramification-index formula for our fields is
imported. The PDF carries no date/version identifier. The fixed
embeddings required in its introductory discussion must be retained.
[Milne ANT v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
7.50-7.52 pp.127-129, inspected with proof, supplies the unramified
compositum setting for complete fields with perfect residue field.
Finite extensions of Q_p satisfy these field hypotheses; the later
application must still identify every conjugate and actual completion.

Fresh queries were `Mochizuki "normal closure" "different" Legendre`,
`"Inter-universal" "conductor" "tamely" "1.10"`,
`site.stacks.math.columbia.edu "compositum" "tamely ramified"`, and
`site.jmilne.org "maximal tamely" extension`. Only the primary sources
specified above are used. Other search hits are uninspected leads;
no general repair theorem or novelty conclusion was obtained. The
step364 searches remain adequate for the unchanged repair context.
The scoped duplicate check read L092/L094/L095 and the repair ledger;
L093 is dyadic only. ATTEMPTS/035's authentication stop stays parked.

This is a completed source review, classified KNOWN_IMPORTED. It
imports exact requirements and supporting theorems, not the desired
normal-closure preservation result. No lemmas or mathematical scripts
were written. Mathlib full/supporting coverage remains unchecked.
STATUS remains IN_PROGRESS, with no complete-solution candidate.

## Invocation-start proposal — historical; completed above

The main gap remains original finite B>=A. The intermediate target is
the exact TARGET above. Its downstream use is to decide whether the
normal-closure repair loses a numerical input or only the original
relative-degree proof of that input. Neither conclusion would settle
exact generation, all initial theta-data or essentiality.

Use the existing source readings before any retrieval. The step364
ledger records the pre-ell increment and the use of tameness away
from 2,3,5. The next comparison must extract the exact mathematical
inequality, its bases and weights, and its good/multiplicative and
conductor assumptions. The ledger's short summary is not a proof
that the same assembly applies after the field change. If an essential
source case was not retained in sufficient detail, read only that
statement and proof case. ATTEMPTS/035's authentication/reapproval
mechanism remains parked.

Essential inputs are audited L090,L092,L093,L094,L095 with inherited
L089 data: unchanged original survivor E/Q, c,h,d_*,e_*, both fixed
domains, fixed closure, all six full-coordinate orderings,
T=Q(E[2])=Q(t_o), G_o=Q(t_o)(iota,E_o[15]) and C_o=G_o^nor over Q.
Retain every actual extending finite place and the absolute valuation
v_p(p)=1. C_0=46080 remains a comparison constant. The relative
excess is not removed by the passing local bounds. Do not assume
G_o=C_o, identify T with the source's ell-division field, substitute
prime seven for the height-selected prime or transfer initial-data
properties from another named curve. Keep d=6,epsilon_d=1 only in
the qualified source comparisons.

Continue to a separately approved mathematical target only if the
source comparison supplies an exact inequality and a finite list
of hypotheses that can be tested on these same fields. If L092-L095
do not cover an essential support or base-change assertion, name that
first missing assertion as the next independent test; do not call
missing coverage a refutation. Do not repeat the completed local
audits or multiply the printed constant by four without an argument.

Unresolved qualifications are the April reproduction's authentication
and current-version status, the def= boundary, exact generation and
alternative repairs, the height-selected prime, independent initial
data, native input/action/factorization/pilot and essentiality. Mathlib
coverage is unchecked. No all-place result or complete-solution
candidate is asserted here. This newly written proposal requires a
separate literature turn; step381 executed only the approved L095 audit.
