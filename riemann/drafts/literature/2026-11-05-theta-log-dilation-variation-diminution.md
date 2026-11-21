# Logarithmic theta dilation: finite-order variation diminution source gate

TARGET: Assess whether finite-order variation diminution for H(v)=e^v K(e^v)/m_0 can give a noncircular theta-weighted Laguerre sign estimate without full-support common interlacing.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step502 completed bounded exact/standard-terminology searches for Schoenberg finite-order convolution variation diminution and logarithmic theta total positivity; compared step385/484/499 assessments and L795. Queries and inspected primary passages below. No adequate unconditional sign-transfer theorem was found in this scope; no novelty inference.
SOURCE_EVIDENCE: Schoenberg, Acta Sci. Math.12 (1950),97–106, Theorem1 pp.98–99, direct proof pp.99–100 and continuous-density converse pp.100–103, https://acta.bibl.u-szeged.hu/13626/1/math_012_pars_b_097-106.pdf ; Choudhury–Yadav arXiv:2307.11822v3 Definition1.1/TheoremC pp.2–4 and forward/equality proof p.11, https://arxiv.org/pdf/2307.11822v3 ; Khare arXiv:2008.05121v2 definitions pp.2–3, Lemma6.1/full proof pp.20–21 and TheoremD statement p.7, https://arxiv.org/pdf/2008.05121v2 . No integral application to H is imported.
COMPARISON: Checked variation-diminishing conclusions bound sign changes above; the finite-matrix endpoint rule requires count equality. Neither supplies missing lower oscillation or theta-dependent signs. Positivity of H does not verify translation minors; ordinary theta, inverse-Xi densities and coefficient sequences are different kernels.
GAP: Translation-minor hypotheses, a justified logarithmic integral interface for the unbounded Laguerre input, independent lower oscillation/sign data and degree-uniform transfer remain unproved. The sources checked do not close these gaps.
REASON: Informative source-scope NEGATIVE: park automatic H-based sign transfer because its checked conclusions and hypotheses do not provide the needed signs. This does not disprove finite-order positivity of H or exclude a later application with independent signed data.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; prior averaging/LP/coefficient assessments did not cover logarithmic translation kernels or the direction and equality hypotheses of variation diminution.
SCOPE: Completed source comparison only. No approval for H-minor computations, new convolution identities, root calculations or an RH-equivalent all-order assumption. The distinct continuation has a separate REVIEW_REQUIRED assessment.

## Original nomination and acceptance test

This is one bounded literature-only continuation, not approval of a
calculation. Its main gap is actual-Xi all-degree mixed positivity.
The candidate intermediate mechanism is a finite-order
variation-diminishing theorem for the logarithmic dilation kernel;
H above is a proposed definition for review, not a proved transfer
identity or a claim of total positivity. A useful result would supply
a theta-specific condition with a concrete finite-order sign/minor
test, potentially supporting actual weighted compensation where
support-wide interlacing fails. No such result is currently available.

Read exact primary hypotheses and essential proof cases before importing
anything. Check the direction of the zero-count conclusion: an upper
bound alone does not supply the desired full root count. Identify any
independent boundary-sign or oscillation premise needed. Distinguish
finite-order kernel positivity from all-order LP or PF assumptions;
do not obtain a purported proof by assuming an equivalent criterion.
Retain the complete theta law and explain any coordinate or support
change. Do not presume independence of the shared scalar.

Compare the precise discovered statement with L795 and the completed
step385/484/499 assessments before opening additional proof files.
Use L019/L021 and L795 as the essential local inputs; L776 is needed
only if converting to its coefficient convention. No cross-notebook
input is nominated. Unresolved assumptions are the kernel condition,
any lower oscillation/sign transfer, effective degree dependence and
all-degree actual signs. Mathlib coverage of this new interface has
not been checked.

Continuation test: nominate a later mathematical attempt only if a
primary theorem yields a noncircular sufficient condition and a
discriminating finite-order test using the actual theta data. If its
hypotheses require unproved LP/all-degree positivity, its zero-count
direction is inadequate without new signs, or it repeats an exhausted
universal-preserver assertion, record that exact obstruction and park
this mechanism. No lemma, mathematical script, new identity or sign
calculation is authorized during the source gate. A genuinely new
central proof attempt may be nominated creative only after its precise
obstruction and bounded test are supported; no creative label is
claimed by this nomination.

## Completed source comparison — step502, 5 November 2026

The main gap is actual-Xi all-degree mixed positivity. The reviewed
intermediate target was a noncircular finite-order variation-diminishing
condition for the logarithmic theta law, useful for weighted compensation
after L795's full-support common-interlacing stop. The acceptance test
required both an applicable hypothesis and a useful sign/zero-count
direction. It is not met by the sources checked. No new identity or
mathematical specialization was derived during this literature turn.

### Primary statements and essential proof cases

I. J. Schoenberg, *On Polya frequency functions II: Variation-diminishing
integral operators of the convolution type*, Acta Sci. Math.12 (1950),
97–106, [Theorem1, pp.98–99](https://acta.bibl.u-szeged.hu/13626/1/math_012_pars_b_097-106.pdf).
For nonzero real bounded-variation L, normalized by L(-infinity)=0 and
midpoint values at jumps, its Stieltjes convolution on bounded continuous
real f is variation diminishing precisely when L is, up to sign, a
cumulative integrable Polya-frequency density or has one jump. Here
Polya frequency requires all ordered translation minors nonnegative,
not merely pointwise positivity. The conclusion is v(g)<=v(f).
The direct proof, pp.99–100, also covers bounded measurable f: finite
output alternation survives truncation and Stieltjes-sum approximation,
then matrix variation diminution gives the upper bound. The
continuous-density converse, pp.100–103, uses localized step inputs,
rank/minor sign constraints and distant near-diagonal minors.
It does not assert preservation of the full number of roots. No general
Stieltjes converse or LP product is reproved or used for the theta law.

P. N. Choudhury and S. Yadav, *Sign regular matrices and variation
diminution: single-vector tests and characterizations, following
Schoenberg, Gantmacher–Krein, and Motzkin*,
[arXiv:2307.11822v3](https://arxiv.org/pdf/2307.11822v3), 30 July 2024,
Definition1.1 and TheoremC, pp.2–4. For a finite real m-by-n matrix,
SR(epsilon), epsilon_r in {-1,1}, prescribes each order's weak minor
sign. It is equivalent to S^-(Ax)<=S^-(x) for every real x, with the
endpoint rule when Ax!=0 and S^-(Ax)=S^-(x)=r<=min(m,n)-1: the first
and last nonzero output signs equal epsilon_r epsilon_(r+1) times the
corresponding input signs. S^- discards zero entries; S^+ maximizes
over their signs. The forward/equality proof, p.11, approximates by
strictly sign-regular matrices and uses semicontinuity of these counts;
the equality hypothesis forces stable nonzero sign patterns. Thus that
endpoint conclusion is conditional on equality, rather than a source
of equality. This is a finite-matrix theorem; no unproved finite-order
integral extension, quadrature limit or multiplicity-count statement is
imported here.

A. Khare, *Multiply positive functions, critical exponent phenomena,
and the Jain–Karlin–Schoenberg kernel*,
[arXiv:2008.05121v2](https://arxiv.org/pdf/2008.05121v2), 12 April 2021,
definitions pp.2–3: TN_p requires all ordered minors of sizes 1 through
p nonnegative; TP_p is strict. Lemma6.1, pp.20–21, characterizes TN_2
translation kernels on J-by-J, J an interval containing zero in its
interior, for measurable densities on J-J: the positive locus is an
interval and its logarithm is concave (apart from degenerate support).
Read both proof directions, including the zero-support cases, midpoint
inequalities and measurable-to-continuous step. TheoremD, p.7: take
0<rho<=rho_tilde<=infinity, rho finite, 0<epsilon<=rho_tilde-rho/2,
integer p>=2. A real integrable density on (-rho_tilde,rho_tilde),
positive on (-rho/2,rho/2), zero outside [-rho/2,rho/2], and TN_p on
[0,epsilon)-by-(-rho/2,rho/2+epsilon), has transform zero-free for
|Im(s)|<p*pi/rho. This statement alone was screened; no proof or
application is imported. Its compact-support hypothesis is not supplied
for H. TheoremE and Karlin's monograph remain unused leads.

### Applicability and the exact obstruction

L019/L021 give the original positive theta density and all its even
moments. L795 supplies the actual finite weighted-polynomial identity
and the robust support-wide interlacing obstruction. These are the
essential local inputs; L776 is unnecessary without coefficient
conversion. No cross-notebook input is used.

The definition H(v)=e^v K(e^v)/m_0 refers to v in R and u=e^v>0.
It must retain the whole positive u support; this is not the even kernel
K(|v|), a reciprocal-Xi density or a coefficient-Toeplitz kernel. No
new change-of-variables identity is asserted here. A translation-kernel
application would still have to specify its input function, orientation
and domain, prove convergence and identify its output with the desired
polynomial or signed quantity. In particular L795's reference is
polynomial in u and is not bounded as u grows at positive degree and
nonzero argument. Schoenberg's bounded-input theorem does not
automatically authorize its use after a logarithmic substitution.
Truncation would require a separate justified limit and would still
not provide a lower oscillation count.

Even granting such an interface and the relevant minors, the checked
variation-diminishing conclusions provide an upper bound. A claim of
d real roots for a degree-d polynomial needs a lower count or equivalent
independent signs. The finite endpoint rule cannot supply that missing
count because it assumes equality. Sign changes also do not count
even-multiplicity roots. Thus neither a finite matrix approximation nor
all-order PF terminology supplies the missing theta-weighted signs.
This is a limitation of the proposed automatic import, not a theorem
that every theta-specific use of variation diminution must fail.

Step385's coefficient-Toeplitz comparison, step484's LP/finite-preserver
restrictions and step499's correlated averaging comparison were reused
at their unchanged scopes. L795 remains the canonical interlacing stop;
none of those stops proves or disproves TN_p for H. Sra's
[version page](https://suvrit.github.io/papers/riem-xi/) was screened:
its stated inverse-Xi densities are different objects. That page is not
a primary-theorem verification or an input for H. Ordinary theta PF
search leads were likewise not treated as results about H.

### Search record, route and continuation

Queries included “Schoenberg 1951 Polya frequency functions variation
diminishing finite order theorem sign changes translation kernel”,
“theta kernel logarithmic dilation total positivity finite order
variation diminishing Riemann xi”, “finite order variation diminishing
kernel theorem sign changes r”, “e^v theta total positivity logarithm
kernel”, and “Schoenberg 1955 multiply positive functions variation
diminishing order r sign changes theorem”. Primary statements above,
not search snippets, support the decision. The bounded search did not
establish novelty or an impossibility theorem.

Park the automatic logarithmic-variation sign route. Reopening requires
an explicit, independently controlled signed or lower-oscillation input
and an exact applicable interface; a minor check alone would not resolve
the present direction gap. No H-minor sweep is nominated.

A distinct candidate is a positive Jacobi/Favard realization of the
actual averaged polynomial sequence itself, rather than a universal
preserver or a reference-family interlacer. A narrow local search for
Favard, Brenke, orthogonal Jensen and three-term recurrence found no
matching assessed actual-P_d test. The existing shift-zero Jacobi
assessment concerns coefficient matching to a separate model. L530
concerns outward Pollaczek flow; L565 concerns a diagonal Hermite CD
cone. Their hypotheses/conclusions were inspected for duplicate
triage only, not imported or re-audited. The new proposal would test a
common sequence recurrence; its theorem-level coverage is absent.
It is therefore nominated only in
[a separate REVIEW_REQUIRED gate](2026-11-05-theta-average-favard-interface.md).
No recurrence, moment relation or feasibility value was derived.

An independently controlled signed theta mechanism is still missing,
so no creative proof attempt is justified by this review. Missing
essential source coverage explains the next literature nomination
despite the preferred mathematical-turn balance. Mathematical
EXPLORATION usage is zero for this turn; no counters are reset. Full
matching Mathlib coverage is unchecked. No lemma, mathematical script,
assembly argument, DAG edge or supervisor state is changed.

