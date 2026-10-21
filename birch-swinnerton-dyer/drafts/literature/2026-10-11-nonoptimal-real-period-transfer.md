# Nonoptimal real-period transfer — primary-source comparison

TARGET: Assess whether a supplied rational isogeny and minimal-differential pullback give an exact total-real-period ratio that transfers a certified optimal curve's normalized symbols to a nonoptimal minimal curve.
CHECKED: 2026-10-11
DECISION: IMPORT
SEARCH_EVIDENCE: Searched isogeny/real-period/kernel-cokernel/differential terminology; checked local nonoptimal exclusions and prior production-stop context; retrieved the primary period identity, all real prime-degree cases and the cited degree-two proof; compared Wuthrich's nonoptimal conventions.
SOURCE_EVIDENCE: Dokchitser--Dokchitser, Local invariants of isogenous elliptic curves, Trans. AMS 367 (2015), 4339--4358, arXiv:1208.5519v4 (28 October 2013), Notation 7.1, Definition 7.2, Remark 7.3, Lemma 7.4 with complete proof and Proposition 7.6, pp.15--16; cited degree-two proof in Parity of ranks for elliptic curves with a cyclic isogeny, JNT 128 (2008), 662--679, Section 7.1 p.11 of retrieved arXiv PDF; Wuthrich arXiv:1608.06423v2, Section 2 pp.2--3 and Section 2.1 pp.4--5.
COMPARISON: The exact ratio is published for prime-degree isogenies, including disconnected real loci; independent differential and real-map data suffice for a restricted conditional transfer. No new period theorem or reproof is needed.
GAP: No specified nonoptimal instance or verified isogeny data were supplied here. The inspected theorem has prime-degree hypotheses; arbitrary composite degree remains outside approval. Normalization supplies neither coefficient nonvanishing nor rational points.
REASON: Primary coverage removes the unassessed prime-degree period input; restrict the continuation to inspected hypotheses rather than silently generalize them.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes optimality hypotheses and requires previously unread real-isogeny and disconnected-locus statements.
SCOPE: Supplied Q-rational prime-degree isogeny E0 -> E between specified global minimal models, independently identified semistable optimal E0 with audited full-relative normalization, exact nonzero minimal-differential pullback scalar and independent real kernel/cokernel information; degree two and both component types included. Isogeny production/verification and arbitrary composite degree excluded.
COVERED_TARGET: Import the total-real-period and full-relative symbol transfer for a supplied prime-degree rational isogeny, retaining exact minimal-differential and real-kernel/cokernel data.

## Gap, relevance and discriminating test

The main gap is rank E(Q)=m(E) for arbitrary analytic order m(E)>=2.
The intermediate target is exact normalization on a nonoptimal minimal
model using a supplied isogeny from an independently identified optimal
model. Its downstream use is extending L027's normalization input beyond
optimal examples. Independent coefficient production, rational point
realization and complex-order comparison remain missing.

Continue only with exact equations, map direction and prime degree,
an independently certified nonzero differential pullback, and real-map
data meeting the cited cases. A database isogeny-class label, assumption
that all kernel points are rational, or desired symbol scale is insufficient.
If a witness is missing, park the instance application. A conditional
import can leave witness production unresolved. No witness is produced here.

## Primary period statement

[T. and V. Dokchitser, Local invariants of isogenous elliptic curves,
arXiv:1208.5519v4, pp.15--16](https://arxiv.org/pdf/1208.5519v4#page=15)
fixes prime degree. Definition 7.2 and Remark 7.3 use the entire real locus.
For phi:E0 -> E and phi*omega_E=d omega_0, Lemma 7.4 states

    Omega(E0)/Omega(E) = (#ker phi_R / #coker phi_R) / |d|.

Its complete proof integrates over the image using the kernel-sized
unramified cover and divides by the image index. Proposition 7.6 gives
the kernel/cokernel quotient: for odd degree ell, ell if the whole kernel
is real, otherwise one. For degree two, write the source
y^2=x^3+a x^2+b x with kernel point (0,0). The quotient is one when
b>0 and (a<0 or 4b>a^2), and two otherwise. Use the minimal
differentials for d, irrespective of this auxiliary equation.

The stronger semistable odd-degree Theorem 8.7 was inspected but is
unneeded. No arbitrary-degree extension is inferred from the general-looking
proof. No BSD input is needed for Lemma 7.4.

[The authors' errata page](https://people.maths.bris.ac.uk/~matyd/)
lists a ramification correction to Theorem A.5; that theorem is unused.

## Essential disconnected-locus proof and qualifications

The cited [Dokchitser--Dokchitser, Parity of ranks for elliptic curves
with a cyclic isogeny, Section 7.1, p.11](https://arxiv.org/pdf/math/0604149#page=11)
was read in full. It separates connected target, connected source with
disconnected target, and both disconnected. In the last case surjectivity
depends on the kernel's component, determined by whether zero is the
rightmost cubic root. Component counts alone are inadequate.
Its local setup assumes a!=0. For the full degree-two statement, cite
Proposition 7.6 of the later paper; do not extend the earlier Hilbert-symbol
proof to a=0. A future instance must justify its auxiliary coordinate change.

## Normalized-symbol applicability and local comparison

[Wuthrich, Numerical modular symbols for elliptic curves,
arXiv:1608.06423v2, Section 2](https://arxiv.org/pdf/1608.06423v2#page=3)
uses the newform associated to the isogeny class and retains period ratios
for nonoptimal models. Its symbols use the least positive period Omega+,
whereas L028 uses the total real period. Section 2.1's Proposition 2 and
degree-two discussion were inspected as comparison, not an independent
ratio-production algorithm: they already use period-ratio data.
No nonoptimal Manin constant is set to one. Previously assessed semistable
optimal Manin results apply only at E0.

The prospective elementary applicability argument must identify the same
normalized newform, keep the oriented full-relative numerator, and use the
positive total-period ratio on every integral generator, accounting for
all resulting rational denominators. This is an import specialization,
not grounds to reprove the period theorem. No rescaling is performed here.

Inputs: L028 total-period/integral-generator conventions, L029 full-relative
line where needed, audited L043/L044 optimal normalization, and independently
supplied prime-degree map and differential/real-map data. No cross-notebook
input. Local nonoptimal searches found no canonical duplicate transfer;
existing optimal assessments expressly exclude it. ATTEMPTS/023--024 and
uniform twist retrieval retain their production stops; this changes the
scale input rather than repeating their conditional audits.

Queries included `Dokchitser Dokchitser isogenies elliptic curves real
periods cokernel kernel differential period ratio lemma` and `isogeny
elliptic curves real periods Omega differential kernel cokernel local real
ratio`. Primary statements and proof cases above were actually read.
Mathlib matching coverage is unchecked, not known absent. No lemmas or
mathematical scripts were written. The newly covered continuation requires
separate supervisor approval next turn before mathematical invocation.
