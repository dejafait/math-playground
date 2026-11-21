# Real-radius information versus one-sided Li coefficient recovery

TARGET: Assess whether real-radius Abel bounds on cumulative ordinary Li coefficients can recover L984's one-sided coefficient bound without additional sign or complex-domain assumptions.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step417 completed bounded Tauber/Littlewood, signed power-series, Li/Tauberian, real-axis and continuation searches; checked local reviews207/235/245/279 and stops235/240/284 in their stated scopes. Exact queries, inspected primary passages and unread leads are recorded below; no novelty inference.
SOURCE_EVIDENCE: Estrada-Vindas arXiv1201.1408v1 (6Jan2012), introduction/(1.1)-(1.2), Theorem1.2 p3, Section3.4/Theorem3.3 and its proof pp7-8, definition2.3 p4 and Corollary4.4 p13; Flajolet-Sedgewick Complex Asymptotics (8May2004), TheoremsVI.10/VI.11 pp156-158 and IV.6 p29, statements and essential proof cases inspected at the primary URLs below. Reuse L984's Voros germ and Pringsheim contracts without reapproval.
COMPARISON: Inspected signed Littlewood results require genuine Abel convergence throughout the open unit disk and independent coefficient or Cesaro lower control; HLK additionally assumes nonnegative coefficients; Darboux requires holomorphy and full-circle smoothness. L984 supplies a meromorphic continuation of a local germ, allowing interior off-axis poles, not any of these missing hypotheses. No inspected theorem recovers its bound from radial estimates alone.
GAP: No actual-Li coefficient lower envelope or independently paid unit-disk convergence/sign condition is available. The source comparison rejects these direct theorem applications, not every conceivable real-axis method. A separately nominated symmetric-quartic pole-model test remains unperformed.
REASON: Essential primary hypotheses are now inspected and expose an actionable source-scope obstruction. Park the direct Tauberian import; prepare one explicit bounded rational-model test with the same cumulative observable, preserving reality, reflection, normalization and integer zero orders. No mathematics is derived in this literature turn.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lacked an inspected signed Tauberian theorem and a convergence-versus-continuation comparison; this turn fills that essential gap rather than repeating ready L984 or Perron coverage.
SCOPE: L984's ordinary Li coefficients, c_n=sum_(k=2)^n lambda_k, n>=2, and the exact meromorphic continuation of its local germ. No positivity of c_n, RH, radius-one Taylor convergence, simple zeros or absence of off-axis poles may be assumed.

## Exact test and plausible use

Use L984's already established local identity, without deriving another
generating formula:

    H(z)=2 xi(1/(1-z)),
    F(z)=[z H'(z)/H(z)-lambda_1 z]/(1-z)
        =sum_(n>=2) c_n z^n locally at0.

The desired coefficient threshold is the existing L984(1): for every
epsilon>0, c_n>=-D_epsilon exp(epsilon n), with finite D_epsilon and
all n>=2. Its relation to the arithmetic premise (H) and the RH
implication remain exactly as qualified in L984; no new equivalence is
claimed. A legitimate source-backed recovery principle could identify a
direct analytic route to that sufficient bound and bypass the synthetic
band bridge. A theorem whose missing assumptions already exclude the
relevant off-axis poles would instead give a concrete rejection test.

First compare primary Abelian/Tauberian statements for signed Taylor
coefficients and real-axis bounds, and recorded Pringsheim/Darboux
conditions. Retrieve exact hypotheses and essential proof cases before
reading large extracts. In particular distinguish a convergent Abel sum
from evaluating a meromorphic continuation along (0,1). If an off-axis
pole truncates the Taylor radius, values beyond that radius are not
automatically Abel sums. Check whether one-sided coefficient control or
holomorphy on a larger complex region is already an assumption of the
proposed theorem. Do not import a positive-coefficient theorem for the
unknown signed c_n. No numerical zeta experiment is proposed.

Continue only with an inspected theorem whose additional hypotheses are
independently checkable, or nominate a separately assessed bounded
pole-model obstruction test that retains the actual germ's relevant
reality/pole qualifications. Abandon this recovery principle if its
coefficient conclusion requires the unpaid sign/domain information.
Generic radial smoothness or a formal degree damping identity is not
evidence. No countermodel or coefficient estimate is derived in this
nomination; newly ready mathematics needs separate next-turn approval.

## Recovery comparison and limits

Three mechanisms were compared for continuation, without a second
mathematical attempt: (i) fixed continuum ridge/Radau parameters are now
decisively and independently parked by C999e; (ii) fixed-order signed
bulk formulas retain stop410's inadequate capped absolute-error budget;
(iii) direct real-radius-to-coefficient recovery for the actual Li germ
is selected for this source gate. The third changes the observable and
the proposed information transfer; it does not tune the old penalty or
repeat moving-band Perron construction. Prior source scopes are reusable
only where their exact hypotheses match. The duplicate comparison is
bounded and does not assert exhaustive absence of an earlier theorem.

A creative central proof attempt is not ready: no signed recovery
hypothesis or valid complex-domain control is supplied. Source comparison
must first expose that obstruction rather than label routine verification
creative. If it yields an independently testable new mechanism, prepare
its explicit bounded test and creative escalation then. All actual-Xi
positivity, arithmetic output, complements/regulators, and signed forcing
gaps remain open. Essential local input is L984 only for this nomination;
no sibling-notebook theorem is used. Matching Mathlib coverage unchecked.

## Completed source comparison — step417, 11 November 2026

This turn reviews the exact TARGET above. The main gap remains actual-Xi
positivity L030-L032/C032a and unpaid forcing/arithmetic, including
L984(H). Recovery of L984(1) from real-radius information could bypass
the capped band bridge, but its hypotheses must not already exclude
the possible poles. No actual radial estimate is proved or imported.

### Search, duplicate and failure checks

Queries included `Tauber original 1897 Abel power series theorem signed
coefficients n an o 1 Littlewood Tauberian theorem`, `site.algo.inria.fr
Flajolet Sedgewick Tauberian theorem VI.13 signed coefficients`,
`"Li coefficients" "Tauberian"`, `"power series" "real axis"
"meromorphic" "Tauberian" signed coefficients`, `"Li coefficients"
"real axis" "growth"`, `"Li coefficients" "polynomial"
"counterexample" symmetry`, and `"Abel" "meromorphic continuation"
"radius" "Tauberian"`. The theorem numbers below are those actually
found in the 2004 source, not the initially queried number.

The search located Estrada-Vindas's primary research paper and the
author-hosted Flajolet-Sedgewick chapters. Encyclopedia and Wikipedia
results only located references. Powell's arXiv1910.07926 finitization
paper and the original 1897/1911 papers are unread leads; none is
reported as inspected. Unreviewed claimed RH proofs, the DumbPrime
adaptive-coefficient discussion, search snippets and the model-written
OpenMaths page supply no theorem evidence. Search failure establishes
neither novelty nor a universal impossibility.

Read canonical L984 including its audit and Mathlib qualification.
Reused review279's exact scope and read stops235/240/284: none pays
a signed estimate or permits Taylor summation through an interior pole.
Scoped searches of November10-11 Li/germ assessments and attempts
found Pringsheim and quartet comparisons, not ready radial recovery.
Review245's quartet diagnostic concerns a moving prime-band response;
the next nomination concerns the complete cumulative germ's real
radius, not quartet dominance in actual primes. No cross-notebook input.

### Primary contracts and essential cases inspected

R. Estrada and J. Vindas, *Distributional versions of Littlewood's
Tauberian theorem*, [arXiv1201.1408v1](https://arxiv.org/pdf/1201.1408v1),
6 January 2012, introduction pp1-2, Theorem1.2 p3,
Section3.4/Theorem3.3 pp7-8 and Corollary4.4 p13.
Abel summability includes Taylor radius at least one. For real u_n,
Theorem1.2 requires sum u_n exp(-ny) convergent for every y>0,
sum u_n exp(-ny)=a+b log(1/y)+o(1) as y decreases to zero,
and n*u_n bounded below. It concludes
sum_(n=0)^N u_n=a+b*EulerGamma+b log N+o(1).
Corollary4.4 retains unit-disk convergence, replacing the lower bound
by a Cesaro-order-m lower bound, with a Cesaro conclusion.
Theorem3.3 assumes local bounded variation, support in [0,infinity),
condition (2.2), and eventual monotonicity of s(x)+A log x.
Its proof uses positivity to compare second Riesz means with Laplace
integrals. Definition2.3 requires exponentially damped distributions
to be tempered for every positive damping. Thus distributional
language also retains a transformability premise. These hypotheses
and positivity-dependent proof cases were read; no reproof or new
specialization is asserted.

P. Flajolet and R. Sedgewick, *Analytic Combinatorics — Complex
Asymptotics*, zeroth edition, 8 May 2004,
[primary chapters](https://algo.inria.fr/flajolet/Publications/ch4567.pdf).
TheoremVI.10, p156/PDF164, assumes Taylor radius one,
nonnegative coefficients and radial asymptotic
f(r)~(1-r)^(-alpha)*L(1/(1-r)), alpha>=0, L slowly varying;
its conclusion is a partial-sum asymptotic.
TheoremVI.11, pp157-158/PDF165-166, concerns a function holomorphic
inside the disk, continuous on its closure, with k continuous angular
derivatives on its circle; coefficients are o(n^(-k)). Its proof uses
the full-circle Fourier integral, Riemann-Lebesgue for k=0 and
integration by parts for k>0.
TheoremIV.6, p29/PDF37, extracts rational-function coefficients
by partial fractions, with exponential-polynomial contributions
from each pole. Retain the polynomial part for an improper rational
function: its finitely many coefficients cannot be dropped. The proof
explicitly reduces to the proper case. These are inspected tools,
not new results. The full-book URL exceeded the browser size limit;
the author-hosted chapter file supplied every required passage.

### Applicability and route decision

Use u_n in the source statements to avoid confusing its notation
with the notebook's cumulative c_n. Applying Littlewood directly
to c_n requires its convergence and lower-bound premises; applying
it to lambda_n requires separate premises for that different sequence.
Neither set is proved in L984. Formal normalization or subtraction
of a radial main term does not establish those premises.

The exact issue is already explicit in L984(9)-(12): if RH fails,
the cumulative Taylor radius is R<1, while its meromorphic quotient
is regular on the positive real interval below one. A value of that
quotient at r>R is not the sum of its Taylor series and hence is not
an Abel sum in the inspected sense. Postulating radius at least one
would exclude the interior poles L984 detects; this cannot be treated
as routine regularity. This compares an existing audited result,
without deriving a new theorem.

Nonnegativity for HLK, a coefficient/Cesaro condition for Littlewood,
or complex-circle regularity for Darboux remains independently unpaid.
Pringsheim likewise consumes positivity after L984's correction;
it does not supply that positivity. No inspected theorem permits the
proposed direct import. Other real-axis methods remain open if they
bring materially different, independently checkable zeta-specific input.
No abstract impossibility theorem is claimed.

The [symmetric quartic nomination](2026-11-11-symmetric-quartic-radial-test-review-417.md)
asks whether a specified polynomial completion separates weak radial
growth from the one-sided coefficient threshold. It repeats neither
a prime-band quartet calculation nor a claim about actual zeros.
Both target properties are unproved here. This newly written
assessment receives separate next-turn approval before invocation.

Outcome NEGATIVE: inspected hypotheses rule out the direct theorem
applications under available assumptions and change the route. This
is source-scope evidence, not new mathematics beyond the sources,
a coefficient estimate or RH progress. Mathematical exploration
usage is zero. Full matching Mathlib coverage remains unchecked and
unknown. No lemma, mathematical script, DAG or PROOF change is needed.
