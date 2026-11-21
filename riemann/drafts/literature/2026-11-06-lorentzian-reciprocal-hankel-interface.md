# Lorentzian inequalities and reciprocal Hankel forms: completed comparison

TARGET: Assess whether Lorentzian or complete-log-concavity inequalities can supply a correctly oriented, degree-uniform bound for the actual reciprocal-node Hankel forms, using the 2-by-2 minor as a source-to-form discriminator.
CHECKED: 2026-11-06
DECISION: IMPORT
SEARCH_EVIDENCE: Step18 searched exact Lorentzian/Hankel/reciprocal, Lorentzian/Riemann-xi, complete-log-concavity/cumulants and dually-Lorentzian terminology; inspected primary Branden-Huh and Ross-Suss-Wannerer statements and relevant proof cases; compared local L025/L030/L033/L038 and the Gram/logarithm, Favard, generic-shape and finite-test stops. Queries and read limits below; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: Branden-Huh, Ann.Math.192(2020),821-891, DOI10.4007/annals.2020.192.3.4, Example2.3/Lemma2.5 pp829-830, Theorem2.10/proof p834, Example2.26 pp845-846, Theorem2.30/Proposition2.33 and proofs pp847-849; Ross-Suss-Wannerer arXiv:2304.08399v3(30May2023), Definitions4.1-4.2/Theorem4.4 and full proof pp7-8, Definition7.1/Theorem7.2 and proof pp14-15.
COMPARISON: Import only the known theorem signatures and source counterexample for this applicability decision. Normalized coefficient log-concavity has the reverse determinant orientation from the target; complete log-concavity is equivalent to Lorentzianity for homogeneous polynomials, not real stability. Duality is factorial-normalized coefficient reversal, not the actual logarithmic reciprocal-power transform. No actual-theta sufficient bound was located.
GAP: A theta-specific object, justified nonlinear transform and correctly oriented arbitrary-degree sign estimate remain missing. L038 already certifies H_1 positive definite under its arithmetic contracts; more finite signs or another generic counterexample would not supply the missing interface.
REASON: Informative source-scope negative: park the direct Lorentzian-to-reciprocal-Hankel import. Precise citations suffice for the source obstruction; no reproof, new lemma, specialization calculation or mathematical script is warranted. IMPORT approves these known comparisons only, not actual-Xi positivity or an unlisted continuation.
SCOPE: Completed literature-only applicability review. No theorem excluding every possible theta-specific Lorentzian construction is claimed; no mathematical continuation is approved by this assessment.
LITERATURE_REASON: The startup target was REVIEW_REQUIRED and lacked its essential primary theorem hypotheses, normalization and signature comparison; ready theta/Favard/shape coverage was reused.

## Completed comparison — 6 November 2026, step18

The main gap remains L030-L032/C032a: positivity of every actual
reciprocal-node form, in every degree. The intermediate target was a
source-to-form interface, not a new low-degree sign. Its possible use
was an arbitrary-degree inequality hierarchy. The continuation test was
an identified object, valid transform, compatible sign and nontrivial
bound; the direct import fails that test. No mathematical discovery or
claim of a solution is made.

### Primary results, imported without reproof

Petter Brändén and June Huh, [*Lorentzian polynomials*, Annals of
Mathematics 192 (2020), 821–891](https://annals.math.princeton.edu/wp-content/uploads/annals-v192-n3-p04-s.pdf),
Example2.3 and Example2.26: for a homogeneous bivariate polynomial
sum a_k x^k y^(d-k), nonnegative coefficients, no internal zeros and
log-concavity of a_k/binom(d,k) characterize Lorentzianity. Theorem2.30
identifies homogeneous complete/strong log-concavity with Lorentzianity.
Its nonnegative directional derivatives are zero or log-concave on the
positive orthant. Lemma2.5 gives reverse Cauchy-Schwarz for a positive
Lorentzian quadratic form; Proposition2.33 treats homogeneous degree
d>=2 (used here only at positive-orthant points with f(w)>0). Example2.3 explicitly separates Lorentzianity from
stability: 2x^3+12x^2y+18xy^2+theta*y^3 is Lorentzian for
0<=theta<=9 and stable only for 0<=theta<=8. Theorem2.10 preserves the
cone under nonnegative linear substitutions. Read its three substitution
cases, the complete Proposition2.33 perturbation/degeneracy argument and
both directions of Theorem2.30, not merely the abstract. No full-paper
proof audit is claimed.

Julius Ross, Hendrik Süss and Thomas Wannerer,
[*Dually Lorentzian Polynomials*, arXiv:2304.08399v3](https://arxiv.org/pdf/2304.08399v3),
Definitions4.1-4.2 and Theorem4.4, pp7-8: for homogeneous s of bounded
multidegree kappa, s^vee=N(x^kappa s(x^(-1))), where
N(x^alpha)=x^alpha/alpha!. The constant-coefficient operator s(partial)
preserves Lorentzianity exactly when s is dually Lorentzian. Read the
symbol argument for every gamma>=kappa and the converse monomial test.
Definition7.1/Theorem7.2, pp14-15, retain an open convex cone, directions
in it, and the one-positive-eigenvalue condition; their proof reduces to
the ordinary cone. These statements supply no general nonlinear
logarithm-preservation theorem. The journal repository led to an access
challenge; this comparison uses the explicitly read v3, not an assumed
identical final publication. No stronger version is asserted.

### Exact notebook applicability and qualifications

L019/L021 give the actual positive theta density K and moments
M_(2n)=integral_0^infinity u^(2n)K(u)du. The entire cosine expansion
uses (-1)^n M_(2n)/(2n)!, not those moments without factorials.
L024/L025 define S_k through the normalized analytic logarithm on a
zero-free disk, with -sum S_k z^(2k)/k=log(Xi(z)/M_0).
L030/C032a require the real algebraic-square forms with entries
S_(i+j+2); they do not assert positivity. All these facts are already
canonical; this turn derives no new transform.

The following are source-hypothesis comparisons, not new inequalities.
The required H_1 condition is S_2*S_4-S_3^2>=0. Source normalized
coefficient log-concavity instead places the square of the middle
coefficient above the product of its neighbors. Identifying those
three normalized coefficients with S_2,S_3,S_4 would therefore give the
opposite comparison. Different factorial/binomial conventions cannot
be silently dropped. Nor can that identification be assumed in the
first place: positive theta moments, factorial-normalized coefficients
and logarithmic reciprocal powers are three different objects.

There is a sharper local check requiring no new arithmetic. L038 already
certifies H_1 positive definite, subject to L037's explicit software
contracts. Identifying that very matrix as a Lorentzian quadratic
Hessian conflicts with the source signature requirement. This rejects
the direct matrix identification; it does not prove that no different
auxiliary polynomial or sign-changing transform could be useful.
Negating a log-Hessian concerns yet another matrix. No inspected theorem
identifies it with the reciprocal coefficient Hankel matrices in every
degree. Such an identification and its hypotheses remain obligations.

Likewise s^vee reverses a finite coefficient array and changes factorial
weights. It is not 1/s, a logarithm, or the power sums of reciprocal
zeros in L025. Neither preservation theorem establishes membership
for an actual-theta polynomial, carries this nonlinear transform, or
supplies uniform control as the degree grows. The source's explicit
Lorentzian/nonstable example rules out using cone membership alone as
a generic real-root certificate. No new node calculation is needed.
These are precise limits of the inspected theorems, not an impossibility
result for every use of Hodge theory or actual theta structure.

### Reused overlap and failed routes

The targeted local terminology search found no previous full Lorentzian
assessment; the October31 Stein assessment's ordinary log-concavity
mention is not coverage of these polynomial signatures. Reused
L796's common-Favard obstruction (statement only) and its recorded stop,
L738's admissible strictly-log-concave-kernel countermodel (statement
only), and L772's full conclusion plus source-scope discussion. None
states a Lorentzian-to-reciprocal theorem. They prevent replacing the
missing interface by common orthogonality, generic kernel shape or
iterated adjacent Turan signs. L772 is not asserted to be an actual
positive theta density or a Lorentzian counterexample for this target.

The September20 theta-logarithm relevance audit already separates
ordinary moment Gram positivity from the signed Newton transform and
records actual H_1/H_2 certificates. L057's full proof supplies its
precise finite-cutoff quantifiers; it is not one nonreal example passing
all degrees. These are genuine duplication warnings. We neither extend
finite tests nor infer novelty from the unsuccessful new searches.
The recorded reciprocal-determinant/Jacobi-Trudi stop also warns against
an algebraic coordinate change that returns the unpaid original sign.
The parameter-wide four-copy GHS assessment is SOURCE_BLOCKED and is
not imported as a sign theorem or reopened through this source review.

### Search record and read boundaries

Queries: `Branden Huh Lorentzian polynomials Theorem 2.30 complete log
concavity bivariate coefficients`; `Lorentzian polynomials Riemann xi
reciprocal zeros Hankel log concavity`; `"Lorentzian" "Hankel" moments
reciprocal`; `"Lorentzian" "Riemann" xi Branden Huh`;
`"complete log-concavity" "cumulants" moments`; and
`"Dually Lorentzian polynomials" Ross Suss Wannerer theorem`.
Only primary mathematical texts above are theorem evidence. Search
hits for cone extensions and recent xi positivity are leads, not new
inspected actual-Xi theorems. This bounded search establishes neither
novelty nor nonexistence of another useful theorem. The complete
relevant proof cases were read for the cited normalization/operations;
unneeded chapters and whole-paper audits were not undertaken.

Mathlib full-result coverage is not checked. No Mathlib result, external
zero-free region or cross-notebook theorem is an input here. No change
to the main argument or mathematical dependencies is made, so PROOF.md
and DAG.md remain unchanged. No lemma or mathematical script was written.

### Continuation boundary

Park direct Lorentzian import. A distinct nomination examines whether
connected-partition cancellations can exploit the exact theta law
before any cone comparison. The separate assessment is REVIEW_REQUIRED;
no such identity, cancellation, bound or creative proof is approved.
Its fixed H_2 discriminator must concern a sign-producing representation,
not another check of the already recorded finite determinant sign.
No creative mechanism is ready: a theta-specific signed cancellation,
rather than a re-expansion of the known logarithmic recurrence, is the
essential missing evidence. Existing failures remain in force in their
stated scopes; no historical stop is treated as a global ban.

## Startup nomination (preserved, superseded by the comparison above)

This is the sole nominated continuation, not work performed during the
L873 audit. Its purpose is to assess a possible mixed-derivative route
before spending a mathematical turn on it. The main gap is still
L030-L032/C032a, all finite actual reciprocal-node Hankel forms being
positive semidefinite. Use L019 and L025 for the actual theta integral
and its normalization, L024-L025 for reciprocal powers, and L030/C032a
for the exact form. Read only relevant ranges after the local overview.
None of the positivity or real-zero conclusions is an available input.

The bounded discriminator is the orientation and meaning of the
2-by-2 minor S2*S4-S3^2 of the matrix already defined in C032a. Compare
it with the primary theorem's actual mixed-derivative inequality before
claiming that a hierarchy of such inequalities could control the mixed
forms. Do not substitute ordinary positive theta moments for reciprocal
zero powers, or assume a logarithmic/coefficient transform preserves a
source cone. This is a source applicability test, not a claim that this
minor is new or sufficient for RH. Higher degrees and all centers, if
relevant to a proposed formulation, retain their own obligations.

Before approving work, check exact statements, stronger known results
and local duplicates using the actual candidate terminology. Reuse the
existing actual-theta moment/Favard and generic shape comparisons when
their hypotheses match; inspect only their relevant statements. The
completed modular-scale discovery and L874 contact-sign stop are
contrasts, not inputs or blanket prohibitions. Do not retry their
unspecified operators, the printed Dimitrov sign stopped by L875, or
the normal-convolution preservation shortcut audited in L873.

Continue only if a theorem comparison identifies a well-defined object,
a justified or separately testable actual-theta interface, a correctly
oriented nontrivial bound and a plausible use toward the mixed forms.
If a mismatch of hypotheses, signature, normalization or transformation
blocks that use, document the exact mismatch and park this interface.
Unsuccessful searches alone are not a mathematical obstruction. A useful
intermediate bound need not settle the independent all-degree sign gap.

No creative proof attempt is ready: the exact source-to-form map and
its hypotheses are missing. If the source review produces a genuinely
new bounded central mechanism, nominate proof_attempt/creative with its
precise obstruction and decisive test; do not relabel this preliminary
comparison creative. No mathematical exploration counter is reset by
this nomination. Mathlib coverage is unchecked; no cross-notebook input.
