# Unconditional analytic certification — completed source comparison

TARGET: Assess whether unconditional analytic class-number and regulator bounds can certify complete class/unit data for L96 without Minkowski-cutoff enumeration or smaller-field norm relations.
CHECKED: 2026-10-11
DECISION: IMPORT
SEARCH_EVIDENCE: Searched unconditional class/unit verification, effective Dedekind-zeta residue errors and regulator bounds; followed Elsenhans–Voight's GL22 reference to Garcia–Lee v4, Sunley's original Theorem 2 and Louboutin's original Theorem 1; compared saved FNS certificate-scope/nonnormal assessments and ATTEMPTS/018-023. No unconditional L96 class/unit certificate was inspected.
SOURCE_EVIDENCE: Garcia–Lee arXiv:2007.10313v4, March 12, 2021, Theorem 1/Remark 4 pp.2-3, Theorem 5 with range discussion p.5, Section 2.6 pp.14-15 and Section 3/Remark 13 pp.16-17; Sunley Bull. AMS 78 (1972), Theorem 2(1) p.75; Louboutin JNT 85 (2000), Theorem 1 p.263 and proof pp.270-271 in author-uploaded published text; Belabas–Friedman arXiv:1305.0035v1 Introduction p.1; Elsenhans–Voight October 2, 2025 Sections 4-5 and 7 pp.4,7-9,13; reused FNS Section 7.2/Lemma 7.7 coverage.
COMPARISON: Unconditional effective analytic bounds exist, but the inspected factor-two class/regulator certificate requires a generating factor base; Magma's exact missing-generator check still covers primes to Minkowski. These sources supply no independent ambient generation for L96. The ideal-counting bound offers a separate error-feasibility test; no field-specific error was evaluated.
GAP: No unconditional generating-factor-base certificate, complete relations/units or L96 residue enclosure is supplied. The Euler-product tail proof's change from prime-ideal norm to underlying-prime cutoff needs clarification; the independent continuation uses only Sunley's counting bound and Louboutin's upper bound.
REASON: Import precise known bounds and completeness prerequisites; decline approval of an analytic-only complete class/unit certificate and isolate a bounded residue-error feasibility test for separate continuation approval.
LITERATURE_REASON: Changed mechanism and essential unread unconditional analytic theorem, error bounds and class/unit index implications; the ready finite-group audit assessment does not cover them.
SCOPE: Source statements and qualifications only; no L96 arithmetic, new lemma, mathematical script or unconditional class/unit/Selmer certificate is produced or approved.

The original proposal below is preserved as context. No new analytic lemma
or calculation is supplied. Preserve L051–L056, ATTEMPTS/018–023,
and the smaller-Jacobian-factor assessment's source/interface blocker.
Do not repeat the already rejected inference that unit saturation alone
certifies all ambient ideal classes, or that a GRH residue estimate is
unconditional. A large sufficient Minkowski bound is not a lower bound
for all possible certification methods.

Main gap: unconditional emptiness of L032's retained 96a1 disk. Possible
downstream use: a certified complete class/unit input to the existing
square-class and full-disk comparison obligations. Essential inputs are
L051's exact field and degree, L032's disk, the existing FNS certificate
scope, and L052/L056 as route obstructions only. No cross-notebook input.
Maximal order, class relations, ambient generation, units, regulator,
torsion lifts, support/norm maps and disk disjointness remain unverified.

Continue only if inspected primary results give an unconditional,
effectively checkable completeness criterion and a concrete bounded
field-specific feasibility test, keeping unknown arithmetic as unknown.
If the inspected result assumes GRH, presupposes the missing ambient
class coverage, or merely returns the parked enumeration, record that
specific obstruction and park this version. Failed search alone proves
neither novelty nor absence. This source review spends no mathematical
exploration budget and cannot derive or approve a new lemma in the same
turn. Mathlib coverage is not checked.

## Inspected inputs and exact qualifications

Belabas–Friedman, *Computing the residue of the Dedekind zeta function*,
Math. Comp. **84** (2015), 357-369,
[v1, April 30, 2013](https://arxiv.org/pdf/1305.0035v1), Introduction,
p.1, specifies two independent inputs: a factor base generating the
whole class group and a rigorous log(hR) estimate. Under surjectivity,
the tentative class number and regulator are integer multiples of the
actual quantities, and h_hat R_hat < 2hR is the stated halting test.
Its analytic approximation requires GRH, as already assessed. Replacing
only that approximation does not discharge the generating-base premise.
This is an import of the source criterion with its hypothesis, not a
new theorem about arbitrary nongenerating factor bases.

Elsenhans–Voight,
[*Computing class groups and unit groups in Magma*](https://jvoight.github.io/articles/clgpunitgp-magma-02Oct25.pdf),
October 2, 2025, equations (4.1)-(4.4), pp.4-5, separates surjectivity
from relation/unit saturation. Section 7, p.13, checks missing generators
by covering all remaining primes below Minkowski. Section 5, pp.7-9,
describes possible general L-series evaluation with O(sqrt(|Delta|))
complexity, but says its error analysis is unfinished and no formalizable
analytic implementation is available in that version. Theorem 5.2
gives unconditional Euler-product convergence; Example 5.3 already
uses X=exp(10^34) for its reported Q(i) error. Neither this example
nor convergence gives an L96 certificate or necessary complexity bound.

Garcia–Lee, *Unconditional explicit Mertens' theorems for number fields
and Dedekind zeta residue bounds*, Ramanujan J. **57** (2022),
1169-1191, [DOI](https://doi.org/10.1007/s11139-021-00435-6),
[inspected v4, March 12, 2021](https://arxiv.org/pdf/2007.10313v4),
Theorem 5, p.5, restates the unconditional ideal-counting estimate for
any number field K of degree n>=2 and every X>0:

    |I_K(X)-kappa_K X| <= Lambda_K X^(1-2/(n+1)),
    Lambda_K = exp(28.2 n+5)(n+1)^(5(n+1)/2)
               |Delta_K|^(1/(n+1))(log |Delta_K|)^n.

I_K counts all nonzero integral ideals of the maximal order of norm
at most X; kappa_K is the residue at one. The discussion checks the
small-X range from Sunley's thesis and refers to its complex-analytic
argument for the larger range. The thesis proof was not independently
read or reverified; this is a named-theorem import, not a reproof.

Judith E. Sunley, *On the class numbers of totally imaginary quadratic
extensions of totally real fields*, Bull. AMS **78** (1972), 74-76,
[DOI](https://doi.org/10.1090/S0002-9904-1972-12859-3),
[inspected published-paper mirror](https://scispace.com/pdf/on-the-class-numbers-of-totally-imaginary-quadratic-8849my12mw.pdf),
Theorem 2(1), p.75, gives the same estimate for arbitrary degree n>=2.
Its CM restriction belongs to Theorem 1, not this counting statement.
The announcement supplies neither a full proof nor an explicit X-range;
retain Garcia–Lee's range clarification. Publisher access failed; the
original three-page paper was read through the mirror.

Stephane Louboutin, *Explicit bounds for residues of Dedekind zeta
functions, values of L-functions at s=1, and relative class numbers*,
J. Number Theory **85** (2000), 263-282,
[DOI](https://doi.org/10.1006/jnth.2000.2545),
[inspected author-uploaded published text](https://www.researchgate.net/publication/222631087_Explicit_Bounds_for_Residues_of_Dedekind_Zeta_Functions_Values_of_L-Functions_at_s1_and_Relative_Class_Numbers),
Theorem 1, p.263, gives for every number field of degree n>1

    kappa_K <= (e log |Delta_K|/(2(n-1)))^(n-1).

The proof, pp.270-271, treats general signatures using Hecke's integral
representation, zeta_K(s)<=zeta(s)^n and the endpoint bound from
Lemmas 9-10; the separately treated imaginary-quadratic case is outside
degree 36. No normality, GRH or CM assumption is used. The statement
and full concluding cases were inspected; supporting gamma-function
inequalities are imported, not independently reverified.

Both bounds apply to L051's degree-36 field without knowing its actual
signature or assuming normality. They require the maximal-field
discriminant: L051-L052 bound it above and below, but do not determine
it. No bound was numerically specialized in this literature turn.

## Euler-product and regulator qualifications

Garcia–Lee Theorem 1, pp.2-3, gives explicit Mertens errors. Section
2.6, p.14, proof of (20), changes a sum over N(p)>X to one over the
underlying rational primes p>X. Its displayed justification does not
address p<=X<N(p) when the residue degree exceeds one. This is an
unaddressed proof case, not a proved counterexample to the final bound.
No repair, new counterexample or theorem-level rejection is derived
here. The final published PDF at the NSF repository returned 502 twice;
whether it corrects that passage is unknown. Park that tail passage;
the separate ideal-counting test does not use it.

Section 3, equation (22), p.16, records the coarse unconditional bound
kappa_K>=0.36232/sqrt(|Delta_K|) using Friedman's regulator bound
R_K/w_K>=0.09058, Invent. Math. **98** (1989), Theorem B. Friedman's
original paper was not inspected, and no unit group is certified from
this estimate. Remark 13, p.17, qualifies the proposed stronger Stark
constant c8=pi/6; do not treat it as an unqualified effective constant.
No normal tower or absence of quadratic subfields of L96 is presumed.

## Decision, failures and bounded continuation

NEGATIVE for the proposed complete-certificate interface: none of the
inspected guarantees both replaces ambient generation and supplies
complete unconditional class/unit data under the requested restrictions.
This changes routing but proves no impossibility of another analytic
method. Preserve ATTEMPTS/018-023 and the original FNS certificate
obligations; unconditional residue bounds do not reopen enumeration
or smaller auxiliaries inside MN. Search failure establishes no novelty.

An independent continuation tests the cited counting-error radius
against a factor-two residue interval at X<=10^6 using L051-L052 and
Louboutin's upper bound. It needs no ideal enumeration or class data
and avoids the disputed tail passage. Its width implication and all
numerical comparisons remain unproved. The newly written SPECIALIZE
assessment receives separate supervisor approval next turn. Even a
favorable test leaves maximal order, ambient generation, complete
relations/units, support/norm maps, torsion lifts and the entire L032
disk comparison open. Mathlib coverage is not checked. No mathematical
script, lemma, DAG or proof assembly was changed.

Queries included `unconditional verification class group regulator
number field analytic class number formula residue Dedekind zeta
Buchmann`; `unconditional computing residue Dedekind zeta function
class number regulator explicit error bounds`; `Garcia Lee unconditional
explicit Mertens Dedekind zeta residue bounds pdf`; `Friedman computing
class groups regulator unconditional analytic class number formula
factor base generates`; `Sunley class numbers totally imaginary
quadratic extensions totally real fields 1972 theorem 2 e 28.2`;
`Garcia Lee 2007.10313 correction equation 20 prime ideals Mertens`;
`Louboutin Explicit bounds for residues 85 263 pdf`. The 2025/2026
conditional-residue papers and modern ideal-counting papers surfaced
as unread leads, not approved inputs. Author-uploaded Louboutin text
supplied the essential theorem after publisher/Kyoto access failed.
