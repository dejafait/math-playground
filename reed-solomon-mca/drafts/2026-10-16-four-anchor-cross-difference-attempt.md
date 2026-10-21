# Four-anchor coefficient-cross-difference attempt

STEP_ID: 2026-10-16-mca-254-four-anchor-cross-differences

The unchanged EXPLORE assessment is
`literature/2026-10-16-triangle-four-linear-isolated-anchors.md`.
The target is coexistence of four full isolated disjoint-P recoveries
with distinct scalars and pairwise support intersections at most one,
under L057's fixed-H gated triangle hypotheses. The main local gap is
the uniform twelve-additional-recovery bound. L066's four-anchor
necessity and L086's equality linearity explain the possible downstream
use; no assembly or complete challenge solution is assumed.

This is one analytic test of L067 (1)--(3) before antipodality. Reuse
the supplied primary-source comparison and the audited L064 pair test.
The duplicate L068/L080 label assignment and ATTEMPTS/025,026,029
remain excluded as fresh tests. No sampling or certificate replay is
planned. Continue only for a restriction beyond the existing recovery
equations or a fully verified quartet; stop this mechanism if the pass
produces only their cross-multiplied forms and degree capacities.

## Initial working checkpoint

For each proposed anchor write f_i for its monic support quartic,
mu_i for its eligible isolated scalar, and B_i=T_Z,i-mu_i T_Y,i.
L067 gives deg B_i<=4 and evaluations B_i=-mu_i f_i on Y,
B_i=f_i on Z, and B_i=0 on W, without division by singleton
evaluations. At (a,b,c) the evaluations are respectively
[1-(1+mu_i)p]f_i(a), -mu_i q f_i(b), and r f_i(c).
Thus D_ij=B_i f_j-B_j f_i has degree at most eight, vanishes on
Z union W union {c}, and equals (mu_j-mu_i)p f_i(a)f_j(a) at a.
The latter is nonzero by the gates. The remaining task is to check
the residual cubic, every forced root multiplicity, and the four-row
couplings before deciding whether anything beyond L064 survives.

No result or continuation is approved by this working checkpoint.

## Completed analytic pass

All calculations use the rational label data of L067 (1)--(3).
An isolated disjoint-P row forces p,q,r into F_97 without changing
the original chart over F_(97^20). The four full supports and their
distinct eligible scalars are hypothetical inputs, not asserted to
exist. No source theorem is reproved.

Write F_Z(X)=product_(z in Z)(X-z), F_W(X)=product_(w in W)(X-w),
and G(X)=F_Z(X)F_W(X)(X-c), of degree five. For i<j put
delta_ij=mu_j-mu_i!=0. The singleton evaluations and restored weights give:

| Evaluation label x | D_ij(x) |
| --- | --- |
| x in Y | delta_ij f_i(x)f_j(x) |
| x in Z or W | 0 |
| a | delta_ij p f_i(a)f_j(a) |
| b | delta_ij q f_i(b)f_j(b) |
| c | 0 |

For example B_i(a)/f_i(a)=1-(1+mu_i)p, whose difference from
the j expression is delta_ij p. All divisions at P are valid
because K_i avoids P. Singleton entries instead use direct polynomial
evaluation, including zero f_i(x). The five distinct roots in
Z union W union {c} prove G divides D_ij. The value at a is
nonzero by the gates, so D_ij is nonzero. This resolves the
zero-cross-difference branch from the actual hypotheses, not genericity.
Consequently the exact polynomial

    C_ij = D_ij/(delta_ij G)

is nonzero and has degree at most three. Its values at a,b are
p f_i(a)f_j(a)/G(a) and q f_i(b)f_j(b)/G(b), both nonzero.
At y in Y its value is f_i(y)f_j(y)/G(y). All these G values
are nonzero by label distinctness. No exact degree three, invertible
leading coefficient, or nonzero singleton evaluation is assumed.

### Root-count test

Every y in Y intersect (K_i union K_j) forces a root of C_ij.
If y belongs to both supports, f_i,B_i,f_j,B_j all vanish there,
so both terms of D_ij vanish to order at least two. This gives an
extra multiplicity at a common Y root. If a common support root is
in Z or W, the same argument gives order at least two in D_ij;
division by the simple factor in G leaves one residual root. A common
root outside Y union Z union W is outside P also; both f_i,f_j
vanish, so D_ij, and hence C_ij, vanish there. No value of B_i or
derivative is divided out in these arguments.

The guaranteed residual multiplicities total

    |Y intersect (K_i union K_j)| + |K_i intersect K_j| <= 2+1=3.

The second summand is an additional occurrence for a common Y root,
and a new root otherwise. Thus this test never forces the four zeros
needed to contradict a nonzero cubic. Actual coefficients may force
more zeros or a smaller degree; neither possibility is discarded or
asserted compatible. In the saturated case the three factors determine
C_ij up to scale, but this is still a constraint on the same pair.
No uniform saturation hypothesis for a quartet's six pairs is supplied.

### Four-row coupling and exact reverse check

The six cross-differences satisfy

    D_12 D_34 - D_13 D_24 + D_14 D_23 = 0.

Substitute D_ij=B_i f_j-B_j f_i. Each term with two B indices
and the other two f indices occurs twice with opposite signs; the six
choices exhaust the expansion. Thus this is an identity for arbitrary
eight polynomials f_i,B_i, not an extra recovery condition. Dividing
by the nonzero polynomial G^2 gives

    delta_12 delta_34 C_12 C_34
      - delta_13 delta_24 C_13 C_24
      + delta_14 delta_23 C_14 C_23 = 0.

It remains automatic with the actual singleton-derived coefficients.
Likewise f_i D_jk-f_j D_ik+f_k D_ij=0, and the same expression
with B in place of f, cancel term by term. No nonzero residual or
resultant follows merely from these identities.

Fix row 1 and its gated p,q,r. For each j impose the displayed
D_1j evaluations at a,b,c. Dividing only by f_1(x)f_j(x)!=0
for x in P recovers exactly

    B_j(a)/f_j(a) = 1-(1+mu_j)p,
    B_j(b)/f_j(b) = -mu_j q,
    B_j(c)/f_j(c) = r.

Conversely these restored equations give those D_1j evaluations.
The three comparisons with row 1 therefore say exactly that all four
restored weight triples agree. Comparisons among rows 2,3,4 follow
by subtraction. Singleton evaluations already hold by construction.
This is L064's isolated-row compatibility expressed polynomially;
the tested four-row identity does not strengthen it. This is not a
claim that every possible coefficient argument must fail.

### Gates and outcome

Each row still requires u_Y,i u_Z,i!=0, mu_i!=0,-1, all base-weight
gates, E_i=rho-(1-rho)mu_i!=0, and all four numerator weights from
L057 (13) nonzero. The cross-difference identities do not imply these
last two tests. Distinct eligible scalars give distinct original finite
parameters through L057's map. No candidate quartet or moment
certificate has been produced. Both-zero rows are outside this target,
not eliminated from the main count.

Outcome: EXPLORATION / RESEARCH / POTENTIALLY_NEW; actual task type
proof_attempt. The classification reflects the preapproved uncovered
joint target, not novelty of these algebraic rewritings. The achieved
test gives a nonzero residual of degree at most three and at most three
forced zeros; the required fourth zero or incompatible coefficient
condition was not obtained. There is no new canonical lemma or progress
beyond the checked sources. The 11/q--16/q interval is unchanged.

Stop this cross-difference/root-count and automatic-minor mechanism
under the approved abandonment test. Reopening needs a specific further
coefficient restriction with all exceptional branches and source scope,
not another formal resultant or label sample. Preserve the derivations
as failed-attempt evidence. One mathematical EXPLORATION turn has been
used since the carried zero. Mathlib coverage was not checked and is
not asserted absent. No mathematical script was needed.

An independent critical audit of L097 is proposed for separate coverage
approval. This neither resumes its sparse-transfer search nor assumes
a surviving cyclic plane. The exact action is in PROGRESS.md and the
matching pending assessment; no audit was performed in this step.
