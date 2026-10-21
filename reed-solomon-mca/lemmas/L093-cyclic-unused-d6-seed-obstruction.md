# L093 — An unused cyclic gate gives a linear residual and a seed obstruction

## Hypotheses

Use L089's F=F_(97^20), order-sixteen subgroup H of F_97^*, arbitrary
bijection h:Z/16Z -> H, unshifted moment columns, blocks
B_t={t,t+1,t+4,t+6}, and full alternating kernel K. All indices are
modulo sixteen. Use L090's necessary determinants D_t and L092's
seven seeds {0,1,2,3,5,7,9} and quadratic reconstruction. No actual
errors, original chart, error weights or locators are assumed.

Normalize the labels by exactly L092's projectivity sending h(0),h(7),
h(5) to infinity,0,1. In the following all symbols denote transformed
labels, not elements of H without that transformation:

    c=h(1), d=h(2), e=h(3), g=h(9), j=h(10), k=h(14),
    X=h(8), Y=h(15), m=h(12), n=h(11), z=h(6).

Thus c,d,e,g,j,k are finite and mutually distinct, and avoid 0,1.
The deductions D_1,D_10 force

    j=c(1-g)/(1-c),
    k=(de+gj-d(g+j))/(e-d).

Reject a deduction violating transformed H-membership or distinctness.
Define L092's nonzero quantities and genuine quadratic by

    alpha=e(k-1), beta=k-e, gamma=k(e-1),
    C=(j-g)(k-d)/((j-c)(j-d)(k-g)),
    t=jC, u=j(1-t), Y(X)=tX+u,
    Q(X)=q_2 X^2+q_1 X+q_0,
    q_2=beta t, q_1=beta u+gamma t-alpha, q_0=gamma u.

All these denominators and q_2 are nonzero. The possibility u=0 is
retained. L090–L092 passed their separate critical audits.

## Conclusion

The following explicit rational functions of the normalized seeds
give an additional necessary restriction for K!=0. Put ell=c-k and
define polynomials in X:

    M=k(c-X),
    N=de(g ell-M),
    O=g((d+e)ell-M)-de ell,
    A=c+d-X-j, B=Xj-cd, C_2=cd(X+j)-Xj(c+d),
    Z=-BN-C_2 O, W=AN+BO,
    U=ell(j-k+(1-j)Y)+(k-1)M,
    V=jY(M+ell(k-1))+kM(1-j-Y),
    E=ZU+WV.

Every admitted reconstructed labeling has O(X)W(X)!=0, and D_6 is
equivalent to E(X)=0 there. Write E=sum_(i=0)^4 e_i X^i, padding
zero coefficients, and put a=-q_1/q_2, b=-q_0/q_2. Its remainder
modulo Q is rho_0+rho_1 X, where

    rho_0=e_0+b e_2+ab e_3+(a^2 b+b^2)e_4,
    rho_1=e_1+a e_2+(a^2+b)e_3+(a^3+2ab)e_4.

Consequently every labeling with K!=0 must have

    Delta=q_2 rho_0^2-q_1 rho_0 rho_1+q_0 rho_1^2=0.

If rho_1!=0, there is at most one extending labeling: its quadratic
root must be X=-rho_0/rho_1. If rho_1=0 but rho_0!=0, there is no
extension. If both vanish, this gate does not reduce L092's bound two.
All original membership, collision, pole, unused-gate and full-rank
checks are still necessary, including after Delta=0.

The rational functions rho and Delta are not identically zero after
the displayed D_1,D_10 substitutions, as witnessed below. This is a
nonidentity on the rational seed parameter space. It does NOT prove
nonvanishing at any admissible transformed H-seed assignment, exclude
the exceptional branch there, exhibit a surviving labeling, or prove
uniform zero kernel. The target rank R>=3, actual-error application,
arbitrary families and the global 11/q–16/q interval remain unresolved.
This local result passed the separate step-246 audit below.

## Proof

### Scope and conventions

This is the saved D_6 test on the unchanged EXPLORE target in
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
Audited L089 supplies the circuit gates. L090 supplies the equivalent
involution determinants, and L092 supplies Q, its nonzero leading
coefficient, its pole exclusion and the unique completion from X,Y.
The general division and specialization machinery is cited in the
separate audit below; no general theorem is reproved. The algebra here
is necessary to specialize those gates, not a coverage or originality
claim. The stopped sampling and single-label methods are not used.

For normalized projective labels use the homogeneous pair row

    row(x,y)=(xy,x+y,1), row(infinity,y)=(y,1,0).

The zero determinant condition is projectively invariant by L090's
involution interpretation, also when a normalized pair contains
infinity. D_1 has pairs (infinity,c),(1,j),(0,g); expanding their
determinant gives (c-1)j+c(1-g)=0, exactly the stated j formula.
D_10 has pairs (g,j),(k,e),(infinity,d); its determinant gives
k(e-d)=de+gj-d(g+j). The denominators 1-c,e-d are nonzero by
distinctness. These deductions do not assert an extending labeling.

### Three intermediate rational reconstructions with all poles retained

D_8 has pairs (0,X),(k,infinity),(m,c). The involution exchanging
0 with X and infinity with k is v -> k(v-X)/(v-k), with determinant
k(X-k)!=0. Hence

    m=M/ell=k(c-X)/(c-k).

Here ell!=0. D_3 has pairs (d,e),(0,m),(g,n). Its involution,
written without dividing by d+e-m, is

    v -> de(v-m)/((d+e-m)v-de).

Its determinant is -de(d-m)(e-m), nonzero at admitted labels. The
formula includes d+e-m=0, with no discarded affine branch. Therefore

    n=N/O.

At an admitted labeling g!=m, so N=de ell(g-m)!=0. If O=0 the
involution sends g to infinity, inadmissible since infinity is already
the label at index zero. Thus O!=0 is an essential gate.

D_2 has pairs (c,d),(X,j),(z,n). L090's coefficients for its first
two pairs are exactly A,B,C_2 above. They give the involution
v -> (-Bv-C_2)/(Av+B). Its matrix is invertible because the pairs
are disjoint at an admitted labeling. Substituting n=N/O gives

    z=Z/W.

N,O cannot both vanish, and invertibility implies Z,W cannot both
vanish. If W=0, z=infinity, again inadmissible. Thus W!=0; no
denominator-zero case can provide a finite bijective extension.
Every recovered m,n,z must additionally be in the transformed H,
avoid all assigned labels and avoid each other. These conditions are
not consequences of the rational formulas.

### The exact cleared determinant

D_6 has pairs (1,z),(j,Y),(m,k). Expanding its determinant gives

    z[j-k+(1-j)Y+(k-1)m]
      +jY(m+k-1)+mk(1-j-Y).

Substitute m=M/ell,z=Z/W and multiply by the nonzero ell W.
The result is exactly E=ZU+WV with U,V as above. Equivalently,
even without division it is the determinant of the three rows

    (Z,Z+W,W), (jY,j+Y,1), (kM,M+k ell,ell).

Hence E=0 and D_6=0 are equivalent on the admitted domain, rather
than after silently dropping a denominator. M,N,O,A,B,C_2,U have
degree at most one, Z,W,V at most two, so E has degree at most four.

In F_97[X]/(Q), X^2=aX+b. Multiplication gives

    X^3=(a^2+b)X+ab,
    X^4=(a^3+2ab)X+(a^2b+b^2).

These identities use only q_2!=0. Substituting them in E proves the
two displayed remainder formulas, including every degree drop in E
and every zero coefficient of Q other than q_2. At a common root of
Q,E, rho_0+rho_1X=0. If rho_1!=0, substitute X=-rho_0/rho_1 into Q
and multiply by rho_1^2 to obtain Delta=0. If rho_1=0, existence of a
root forces rho_0=0, giving Delta=0 as well. If rho_1=0,rho_0!=0,
Delta=q_2 rho_0^2!=0. This proves the stated necessary obstruction
and all residual branches. L092's unique completion gives the at-most-
one labeling conclusion in the rho_1!=0 branch. No sufficiency follows.

### Exact nonidentity witness and diagnostic limits

For this paragraph only, evaluate the rational seed formulas at
c=2,d=3,e=4,g=6 in F_97. This is not asserted to be a transformed
H-labeling. It verifies only nonidentity of rational functions after
D_1,D_10. All assigned finite labels are distinct and avoid 0,1:
j=10,k=24. Every seed denominator is nonzero, with

    ell=75, t=17, u=34, alpha=92, beta=20, gamma=72,
    Q=23+66X+49X^2,
    M=48+73X, N=71+94X, O=22+47X,
    Z=76+39X+61X^2, W=95+76X+85X^2,
    U=93+X, V=93+62X+86X^2,
    E=92+74X+18X^2+33X^3+35X^4.

Direct coefficient multiplication in F_97 gives the full identity

    E=(37+41X+70X^2)Q+17+84X.

Thus rho_0=17,rho_1=84, and

    Delta=49*17^2-66*17*84+23*84^2=42 (mod 97),

which is nonzero. This proves that E is not a multiple of Q over
the rational seed parameter field: a zero remainder there would
specialize to zero at every point where its denominators are nonzero.
It gives no count, root or nonvanishing claim on the actual finite
set of subgroup seeds. The earlier reconstruction denominators O,W
are polynomials here; the nonidentity argument does not assume they
are nonzero at an arbitrary root, nor use an inadmissible root as a
labeling. The unconditional algebraic obstruction retains their gates.

The displayed short polynomial identity and modular Delta calculation
can be verified directly and do not require an enumeration. A supporting
diagnostic is reproduced with

    python3 scripts/cyclic-shared-gates/d6_residual.py

It writes the complete certificate
`scripts/cyclic-shared-gates/d6-residual-certificate.json`. It checks
the remainder by a separate long-division computation, D_1,D_10, and
the division-free determinant identity at all 97 scalar values. Where
O W!=0 it also checks D_8,D_3,D_2 by direct three-by-three determinants.
All checks pass, the actual remainder degree is one against required
at most one, and there are zero H-assignments and zero rank tests.
These are checks of one algebraic specialization, not an H-label sweep,
independent full-kernel verification, uniform finite census or audit.
The complete load-bearing coefficient values are displayed above.

### Separate critical audit — October 16, 2026, step 246

The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-16-cyclic-unused-d6-critical-audit.md`
covers exactly this saved-proof audit. Full L093 and the relevant
audited L089/L090/L092 statements, normalization and gate conventions
were checked. No mathematical defect was found. This accepts the
existing necessary restriction and its limited nonidentity statement;
it adds neither a bound nor a claim about admitted H seeds.

**Inputs and standard machinery.** L089 supplies the necessary gates
in the unshifted convention; L090 supplies their involution determinant,
including projective invariance and unique recovery; L092 supplies the
genuine Q and at-most-one completion per admitted root. L091 is used
through L092's S_8 reduction. L010/L087/L088 remain inputs through these
audited results. No L094/L095 conclusion, actual error, rank sample,
nonzero slope or sufficient-gate assumption is used. The direct inputs
in the canonical DAG remain unchanged.

For polynomial division and the smaller-degree remainder import
J. S. Milne, [*Fields and Galois Theory*](https://www.jmilne.org/math/CourseNotes/FT.pdf),
v5.10, September 2022, Section 1.6, printed p. 10. This field theorem
applies to F_97, F_(97^20), and the rational seed function field in
characteristic 97. It requires only a nonzero divisor polynomial;
no squarefree or separability hypothesis is needed. For specialization
import the [Stacks Project, Proposition 10.9.3, tag 00CP](https://stacks.math.columbia.edu/tag/00CP),
statement and proof inspected October 16, 2026. A ring map extends to
the localization when every inverted element maps to a unit. Apply it
to the polynomial seed ring with precisely the displayed rational
denominators inverted. This justifies evaluation at the saved witness;
it does not define evaluation of every element of the whole rational
function field. Neither source proves the cyclic formulas; their
specialization is checked explicitly below.

**Indices, reconstruction and all poles.** The D_t template has pairs
(t-1,t), (t+4,t+9), (t+6,t+8). Thus the six used rows are exactly

    D_1:  (infinity,c), (1,j), (0,g);
    D_10: (g,j), (k,e), (infinity,d);
    D_8:  (0,X), (m,c), (k,infinity);
    D_3:  (d,e), (0,m), (g,n);
    D_2:  (c,d), (z,n), (X,j);
    D_6:  (1,z), (j,Y), (m,k).

The harmless row permutations in D_8/D_2 change at most determinant
sign, not their zero conditions. Infinity is the unique transformed
label at index zero; all other values are finite and distinct in T(H).
The D_1/D_10 determinants give exactly the stated j,k formulas, with
1-c and e-d nonzero. The denominator of C is a product of the three
nonzero differences j-c,j-d,k-g; its numerator and j are nonzero.
Also beta=k-e!=0, so q_2=beta t!=0, even if u=0. Ell=c-k!=0.

The D_8 map has determinant k(X-k), nonzero because k!=0 and X!=k.
The D_3 matrix [[de,-de m],[d+e-m,-de]] has determinant
-de(d-m)(e-m), nonzero at an admitted labeling. Its formula remains
valid when d+e-m=0: the denominator at g is then -de, nonzero.
In general N=de ell(g-m)!=0. O=0 would give the well-defined image
infinity, incompatible with n's index eleven. The two known D_2 pairs
(c,d),(X,j) are disjoint, so L090 gives an invertible matrix
[[-B,-C_2],[A,B]]. Applied to the nonzero homogeneous vector (N,O),
it produces (Z,W)!= (0,0). W=0 likewise forces the inadmissible label
infinity at index six. Thus no simultaneous-zero or finite pole branch
was lost by n=N/O or z=Z/W. Transformed membership, inverse-projectivity
and collision tests still apply; the formulas do not imply them.

**Clearing and reduction.** The coefficient of z in the expanded D_6
determinant is j-k+(1-j)Y+(k-1)m; the constant term is
jY(m+k-1)+mk(1-j-Y). Multiplication by ell W, nonzero on the admitted
domain, gives respectively ZU and WV, with exactly the displayed U,V.
The division-free three-row determinant is the same expansion. U has
degree at most one, V,Z,W at most two, hence deg E<=4; no assertion of
degree exactly four is needed.

Modulo Q the equality X^2=aX+b gives X^3=(a^2+b)X+ab and
X^4=(a^3+2ab)X+a^2b+b^2. Substitution in every coefficient e_0,...,e_4
gives exactly rho_0,rho_1. This uses only q_2!=0 and remains valid
when u=q_0=0, q_1=0, E drops degree, Q has a repeated root, or either
remainder coefficient vanishes. At a Q root, E equals that remainder.
For rho_1!=0 its only possible common root is -rho_0/rho_1; evaluating
Q there and multiplying by rho_1^2 gives precisely Delta. This includes
rho_0=0 and roots subsequently rejected by membership or collision gates.
L092 then supplies at most one entire extension. For rho_1=0,rho_0!=0
there is no common root and Delta=q_2 rho_0^2!=0. For both zero,
Delta=0 automatically and this gate adds no restriction to the previous
bound two. These exhaust the slope branches. Delta=0 alone is never
used as an existence or sufficiency statement.

**Complete nonidentity evidence.** At the displayed specialization,
1-c,e-d,j-c,j-d,k-g,ell,q_2 are respectively
96,1,8,7,18,75,49 in F_97, all nonzero. Thus j,k,C,t,u and both
remainder formulas can be evaluated in the required localization.
The complete convolution of (37,41,70) with (23,66,49), with
(17,84) added, is (92,74,18,33,35), as asserted. The Delta calculation
is 42. A zero rational remainder or Delta would specialize to zero
on this denominator domain, contradicting these values. O and W are
not inverted in E or its remainder, so a pole at a particular X is
irrelevant to this seed-space argument. No witness root is asserted.

The full supporting diagnostic was replayed, producing a byte-identical
`scripts/cyclic-shared-gates/d6-residual-certificate.json`. An additional
check reads every coefficient and all 97 complete rows, verifies the
displayed quotient identity independently, and evaluates determinants
by permutation expansion. At every O W!=0 scalar it checks D_8,D_3,D_2
and the unscaled D_6 multiplied by ell W; at every scalar, including
poles, it checks the division-free determinant against E. Reproduce with

    python3 scripts/cyclic-shared-gates/audit_d6_residual.py

Full audit evidence is `scripts/cyclic-shared-gates/d6-critical-audit.json`.
All 97 rows pass; actual remainder degree one meets required maximum
one; failures are empty, Delta=42, and H assignments and rank tests
are both zero. These are complete checks of the one saved specialization,
supporting the analytic proof rather than replacing its uniform branch
arguments. No new residual, elimination, label census or enlarged field
witness is computed. The stopped routes ATTEMPTS/033–034 remain stopped.

## Mathlib

Matching coverage for this cyclic residual and rational seed obstruction
has not been checked. No absence or formal-verification claim is made.
The inputs are the separately audited L089/L090/L092 specializations;
the pole-aware reconstruction, determinant expansion and degree-four
reduction needed for this specialization are proved here and passed
the separate step-246 audit. The cited standard inputs are informal;
no full matching Mathlib theorem or formal verification is asserted.
