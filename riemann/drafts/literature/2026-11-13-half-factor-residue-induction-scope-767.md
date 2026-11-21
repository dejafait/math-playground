# Degree-dependent half-factor interlacing: completed source comparison

TARGET: Assess whether degree-dependent interlacing of L795's centered formal additive half-factors can be tested through the two residues of Q_3/Q_2 in L825's fixed coordinates.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step768 searched rational interlacing, partial fractions, residues and finite-free theta factors; inspected Fisk Lemma1.20(3) and Holtz-Tyaglov Theorem3.4. Narrow local searches and L795/L796/L805/L825 comparisons found no matching adjacent-half-factor test in the inspected records; no novelty claim.
SOURCE_EVIDENCE: Fisk math/0612833v2 Section1.3 pp12-14 Lemma1.20(3), its proof and Lemma1.8 proof; Holtz-Tyaglov0912.4703v3 Definition3.1/Remark3.2/Theorem3.4 pp44-49, especially (3.6)-(3.7) and condition6, inspected. Reuse step764's finite inversion/forward-convolution assessment; no actual residues computed.
COMPARISON: Known rational-interlacing criteria cover this simple-real-pole, degree-difference-one diagnostic without assuming cubic roots. They supply no theta-specific residue signs or degree propagation. L825's common-symbol, L796's original-P_d common-measure and L795/L805's reference-mixture stops concern different premises.
GAP: The two actual residues, their separation from zero and any independent degree-uniform sign mechanism remain unpaid. The finite test can refute strict adjacent interlacing in these coordinates, but passing it cannot prove uniform factors or actual-Xi mixed positivity.
REASON: Essential primary coverage is now available for a distinct necessary-condition test. Nominate only Q_3/Q_2 for separately approved finite specialization; do not calculate or derive new polynomial identities in this literature turn.
SCOPE: Source comparison for the existing centered monic formal factors in their original coordinates; Q_3/Q_2 is the only proposed finite pair. No degree sweep, re-centering, independent dilation, larger Hermite block or higher asymptotic order.

The central gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. A degree-dependent interlacing induction, if independently
proved, could provide the missing full-factor real roots needed by a
forward additive-convolution realization. Its base case, uniform residue
signs and all shifted/mixed/global transfers would still need proof.
No implication from the known proper-block positivity is available.

The precise candidate diagnostic is whether the rational function
Q_3/Q_2 has two strictly negative residues at the two real simple roots
of Q_2, using the actual fixed-coordinate coefficients of L825. No sign,
residue identity or new polynomial is derived here. The role of those
residues in a strict interlacing induction must first be compared with
primary real-rational interlacing or Hermite--Biehler results, including
the degree difference, leading signs, simple poles, common roots and
zero-residue cases. Those are unread source leads, not imported theorems.
Do not use real-rootedness of Q_3 as a substitute for the residue test.

Reuse [the uniform half-power comparison](2026-11-13-uniform-theta-additive-half-power-scope-763.md)
for formal inversion and the distinction from common-symbol preservation.
Search the exact new statement and terminology before detailed derivation;
compare the relevant L825/L796 stops and check for duplicates. The
step767 nomination search read only the named stop/assessment passages,
not a new complete mathematical input audit. L825's full coefficient
evidence and its inherited L778/L791 analytic/evaluator contracts must
be inspected before a later actual-coefficient calculation; L823 may
supply relevant finite normalization, without importing a new root claim.

Continue to a separately approved bounded residue test only if source
comparison confirms a distinct, useful necessary condition and explains
what independently verifiable uniform sign structure it could probe.
A wrong-sign residue would stop this strict-interlacing route in the
specified coordinates; exact zero requires the source's degeneracy case.
If the condition merely restates unpaid all-degree real roots, duplicates
a recorded obstruction or supplies no discriminating target, park it.
A positive two-pole test alone must not trigger a degree sweep.

No justified creative proof attempt is approved here: the independent
uniform residue mechanism is missing. This source comparison prioritizes
testing its viability, without relabelling routine finite specialization
as creative. Full-factor signs, degree-uniform propagation, finite
exceptions and shifted/mixed assembly remain open. Full matching Mathlib
coverage is unchecked. No cross-notebook input is proposed.

## Completed comparison — 13 November 2026, step768

The preceding paragraphs preserve the nomination and its admission test.
Their statements that primary coverage is unpaid are superseded by this
review. This turn is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION: it
establishes source scope and a discriminating continuation, not a residue
sign, a new mathematical lemma or progress beyond the checked sources.

### Search and local comparison

Queries included `interlacing polynomials partial fraction residues f g
derivative strict interlacing theorem`; `rational function interlacing
negative residues monic polynomials degree n n+1 theorem`; `Tyaglov Holtz
structured matrices continued fractions root localization R function
Theorem 3.4 residues`; `Fisk polynomials roots interlacing theorem partial
fractions negative residues 2006`; `Fisk g/f negative interlacing partial
fractions`; and `finite free theta interlacing factors` / `finite free
convolution residues interlacing`. Search hits were leads only. No searched
theta-specific uniform-factor theorem was identified; this is not a
novelty or nonexistence claim. Other free-convolution/interlacing hits were
not read as theorem inputs.

Reused step764's assessment, rather than repeating its inversion, LP and
fractional-power literature campaign. Read L795's full definition and
full-support stop; L825's coefficient construction, arithmetic and audit;
L796's statement; L805's statement; L823's definition, normalization and
step763 audit passages; and the L778 complex-disk error and L791 step478
normalization/error-contract passages. Read the common-symbol and
common-Favard stop records. Searched only the relevant theta/half-factor
assessments, stops, named recent history and L79*/L82* files for the
quotient and adjacent-factor residue terminology. None of these reads
is a new certificate verification.

L795 and L805 concern common interlacers of same-degree reference
polynomials before averaging. L796 concerns orthogonality of the original
monic P_d for one measure. Its Q_n notation is not L825's half-factor
notation. L825 concerns one common constant-coefficient lowering symbol.
None supplies or disproves adjacent interlacing of L825's degree-dependent
factors. L823's audited cubic real roots alone do not locate them relative
to the quadratic. C795a's retired within-degree detector is a contrast,
not an input. Historical stop evidence is retained.

### Primary statements and essential cases

[Steve Fisk, *Polynomials, roots, and interlacing*, arXiv:math/0612833v2](https://arxiv.org/pdf/math/0612833v2),
Section1.3, printed pp12-14 (PDF pages24-26), Lemma1.20(3), treats a
real polynomial f of degree n with distinct real roots a_i and positive
leading coefficient, and real g of degree n+1 with positive leading
coefficient. In the expansion

    g(x) = (d x+c) f(x) + sum_i c_i f(x)/(x-a_i),

d is positive and strict interlacing with g's two outside roots holds
exactly when every c_i is negative. The basis paragraph supplies the
distinct-root assumption; evaluation gives c_i=g(a_i)/f'(a_i).
Read all three degree cases of Lemma1.20 and its proof, and the endpoint
proof used from Lemma1.8. No prior real-root premise on g is imposed.
The delivered PDF has the v2 arXiv header dated 11 March2008 and a
title-page typesetting date 26 November2024; this identifies the text read.

Source qualification: Lemma1.8's displayed endpoint conditions print
f(alpha), f(beta), which vanish at the named roots; its proof instead
uses g(beta), and its interior-root count also has a one-unit typo.
Do not import those displayed conditions literally. Lemma1.20(3)'s
residue statement is independently covered by the following source;
no corrected new theorem or reproof is being introduced here.

[Olga Holtz and Mikhail Tyaglov, *Structured matrices, continued fractions,
and root localization of polynomials*, arXiv:0912.4703v3](https://arxiv.org/pdf/0912.4703v3),
9 March2011, Definition3.1/Remark3.2 and Theorem3.4, printed pp44-49
(PDF pages43-48), use real coprime p,q with degree difference at most
one. Theorem3.4 equates negative-type R=q/p with (3.6)-(3.7): a linear
part -alpha z+beta, alpha>=0, real simple poles and strictly positive
residues q(omega)/p'(omega). Condition6 equates this with simple real
interlacing plus the specified negative Wronskian orientation. Remark3.2
permits multiplication by -1. For the proposed monic degree3/2 quotient,
the comparison uses p=Q_2, q=-Q_3, retaining its linear term; it does not
apply a proper-fraction theorem to an improper quotient. This is a
source-applicability comparison, not evaluation of any actual residue.

Read the theorem's complete hypotheses and equivalences, the nonreal and
multiple-pole exclusions and residue-orientation cases in 1=>2, the
degree-plus-one infinity case in 2=>3, the continued-fraction/sign chain
3=>4=>5=>6, and the interlacing/orientation cases 6=>7=>8=>1.
The unrelated Hankel-minor equivalence is not needed. These standard
criteria are imported by citation; neither is reproved.

Strictly nonzero residues at every simple denominator root exclude common
roots, as required by the coprimality hypothesis. Exact zero is cancellation
of that denominator root and falls outside the strict theorem. A numerical
interval meeting zero proves neither cancellation nor a sign. No weak
interlacing conclusion is imported for that case, and no simplicity or
root count of the unreduced numerator follows from removing a pole alone.

### Applicability, limits and continuation

L825 already fixes real monic centered Q_2,Q_3, their coordinates and full
coefficient evidence. Its established u_2 enclosure supplies a possible
simple-real-denominator input; verify its complete evidence before use.
L019/L021 provide positivity and normalization; L778/L791's analytic and
software contracts remain explicit assumptions. No fitted Jacobi roots,
new quadrature, independently dilated degree, or cubic-root premise is
needed. Derive and check only the identified coefficient-to-residue
specialization in a later research turn, with exact error bounds and
full certificates; do not reprove the general source theorem.

This gives a genuinely discriminating necessary condition: a certified
positive residue excludes strict adjacent interlacing in these fixed
coordinates, whereas two strictly negative residues certify this pair
only. This can test whether an induction on adjacent factors survives its
first nontrivial pair. It supplies no independent all-degree estimate.
Passing the pair retires the finite diagnostic unless a new uniform
mechanism is justified; it authorizes no degree sweep. Uniform factors,
base/exception management, shifted/mixed transfer and global assembly
remain unresolved. No creative central proof target is justified yet;
the missing uniform mechanism is the blocker, not a routing quota.

Full matching Mathlib coverage was not checked. There is no assertion
of absence. No cross-notebook input, new residue identity, sign,
mathematical script or canonical-lemma change occurred.

The exact proposed finite continuation is in
[the specialization assessment](2026-11-13-half-factor-two-residue-test-768.md).
It is newly ready and requires separate supervisor approval next turn;
this completed source review is not a mathematical invocation of it.
