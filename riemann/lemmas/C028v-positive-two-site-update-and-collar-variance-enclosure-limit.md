# Corollary C028v: positive two-site update and collar variance enclosure limit

## Hypotheses

Use C028t's full even theta probability mu_0, the two positive unit atoms
at a,b, and the degree-four monic orthogonal polynomial of
(mu_0+delta_a+delta_b)/3. Its empirical centered root moments V,T,Q
divide by4. Set g=T/V^(3/2), k=Q/V^2. Use C028u's actual target
(gamma,k_actual), including b_j=j!*I_(2j)/((2j)!*I_0), j=1,...,4.
Do not assume actual-root reality. Fix exactly

    B=[-1/4,1/4] x [3/4,5/4], x0=(0,1), e=+1,-1.

Assume L917/audit197's containment of the unchanged complete panel0
I_0,I_2,I_4,I_6,I_8 under L037's Decimal-library contracts. The panel
is the closed interval [0,1/5120], containing lambda=0. Library
correctness remains assumed. Subsequent finite arithmetic is rational
and outward, with no source refinement. Reference probability moments
omit factorials; actual coefficients retain them.

## Conclusion

For the degree-three base kernel, put

    K_3(s,t)=sum_(j=0)^3 p_j(s)*p_j(t)/h_j,
    M=I_2+(K_3(c_i,c_j))_(i,j=1,2), c=(a,b), Delta=det M.

The specified single whole-collar positive-update evaluation certifies

    573.530616 < Delta < 73569.449116 on B.              (1)

All four base norms and all executed interval divisors have positive lower bounds.
Thus this representation pays the update divisor that C028u's Cramer
enclosure could not pay. It does not finish the nonlinear test: its
subsequent Newton-sum variance enclosure [V_lo,V_hi] satisfies

    -22369.279057 < V_lo < 0 < V_hi < 34276.881561.      (2)

These are bounds on the enclosure endpoints, not negative values of
the actual reference variance. The exact variance is positive by
C028t's reference zero theorem. Both orientations stop before normalized
collar residuals, normalized Jacobians or Krawczyk evaluation. Neither
matching nor nonmatching is proved. This is finite specialization of
known methods and an informative implementation failure, not a new
Uvarov theorem, hyperbolicity result or RH advance. The separate
proof/code/evidence audit1930 below accepts this conditional finite claim.

## Proof

### Imported formula and applicability

Import A. M. Delgado, L. Fernandez, T. E. Perez and M. A. Pinar,
*Multivariate Orthogonal Polynomials and Modified Moment Functionals*,
SIGMA12(2016),090, DOI10.3842/SIGMA.2016.090,
[Theorem3.1, (3.1)-(3.14), printed pp8-10](https://www.emis.de/journals/SIGMA/2016/090/sigma16-090.pdf).
The original and modified functionals must be quasi-definite. L019/L021
give all moments and strictly positive squared norm for every nonzero
polynomial of the base; adding positive atoms preserves this. Hence both
are positive definite, and the theorem applies. Normalization by3 changes
no monic polynomial. In the source's row-vector convention its formula is

    q_4(x)=p_4(x)-(p_4(a),p_4(b))*M^(-1)
                         *(K_3(a,x),K_3(b,x))^t.       (3)

This theorem is imported without reproof; source-notes1926 assesses the
complete statement/proof and matrix convention. The base moment
construction is Gautschi, *Orthogonal Polynomials: Computation and
Approximation*, OUP2004, Section2.1.1, Theorem2.1,
[(2.1.1)-(2.1.3), printed pp52-54](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf),
already assessed in source-notes1920. Only finite even-base formulas
and the enclosure implementation are specialized here.

Write u=I_2/I_0, v=I_4/I_0, w=I_6/I_0. With all odd base moments0,
the required monic polynomials and squared norms are

    p_0=1,                         h_0=1,
    p_1=x,                         h_1=u,
    p_2=x^2-u,                     h_2=v-u^2,
    p_3=x^3-(v/u)*x,               h_3=w-v^2/u,
    p_4=x^4-A*x^2+B_0,
    A=(w-u*v)/(v-u^2), B_0=(u*w-v^2)/(v-u^2).          (4)

For completeness, evenness handles the odd orthogonality equations.
For p_2 the remaining equation is u-u=0. For p_3 it is
v-(v/u)*u=0. For p_4 they are v-A*u+B_0=0 and
w-A*v+B_0*u=0, which (4) satisfies. Direct squared integration gives
h_0,...,h_3 as stated. Uniqueness in the imported construction therefore
identifies these with the base polynomials. This finite check is needed
to connect the implemented coefficients/norm divisions to (3); it is not
a reproof of the general construction. No reference h_4 or eighth moment
is needed; the actual target alone still uses I_8.

### Positive determinant and full differentiation

Put A_j=p_j(a), B_j=p_j(b). The standard two-row Gram/Cauchy--Binet
identity, or expansion and pairing terms with j<l, gives

    Delta=1+sum_j (A_j^2+B_j^2)/h_j
             +sum_(j<l) (A_j*B_l-A_l*B_j)^2/(h_j*h_l), (5)

where j,l range from0 through3. Indeed the last sum equals
K_3(a,a)*K_3(b,b)-K_3(a,b)^2: diagonal terms cancel and each
off-diagonal pair is the displayed square. Thus (5) is exactly det M,
not an added positive surrogate. The j=0 terms alone give Delta>=3.
The numerical evaluation retains the nonnegative range of every square;
it does not subtract two large enclosing determinant terms.

Let kaa=K_3(a,a), kab=K_3(a,b), kbb=K_3(b,b). The weights in (3) are

    W_a=((1+kbb)*p_4(a)-kab*p_4(b))/Delta,
    W_b=((1+kaa)*p_4(b)-kab*p_4(a))/Delta.

For k=0,...,3, the coefficient of x^k in q_4 is the coefficient in
p_4 minus W_a times that in K_3(a,x) minus W_b times that in K_3(b,x).
These expressions include every nonzero coefficient of p_0,...,p_3.

Each computed object carries a triple (value,partial_a,partial_b).
Input moments/norms have zero site derivatives. The sites carry
(a,1,0),(b,0,1). Horner evaluation differentiates every base polynomial
at both sites. Product propagation uses (XY)_s=X_s*Y+X*Y_s;
squares use (X^2)_s=2X*X_s; and each quotient uses
(X/Y)_s=(X_s-(X/Y)*Y_s)/Y. These rules retain both kernel arguments,
all six minors, the full Delta derivatives and the weight derivatives.
No kernel or normalization derivative is silently dropped.

Apply C028t's Newton formulas to the four monic coefficients, with
empirical division4 and every centering term. In particular

    P_1=-c_3, P_2=-(c_3*P_1+2*c_2),
    V=P_2/4-(P_1/4)^2.

This prescribed evaluation and its two derivatives are saved before
any variance reciprocal. Since its lower bound is negative, (g,k) and
their derivatives cannot be certified numerically in this implementation.
Exact reference-root reality does not supply a quantitative reciprocal
of this failed interval.

### Complete finite certificate and verification

Run from this notebook:

```text
python3 scripts/heat/two-site-positive-update-1928.py
python3 scripts/heat/two-site-positive-update-check-1928.py
```

Full certificates have the same stems with .json. The producer verifies
all accepted audit197 input hashes and exact equality of all five full
raw moment records to that audit and attempt1925. It also verifies
the prior producer/checker hashes and passed checker status. The complete
selected inputs, base coefficients/norms, site values, kernel entries,
six minor terms, update weights, four coefficients, their two derivatives,
variance and derivatives, and all expression endpoints are retained.
The point is evaluated once at (0,1); the collar is evaluated once on B.
There is no subdivision, solver, changed domain, site/mass sweep or
moment refinement.

The reused audited1921 arithmetic uses Fraction endpoints with outward
rounding to the grid10^(-50). Addition and four-corner multiplication
enclose the exact operations; a reciprocal rejects zero and uses
[1/upper,1/lower]. Integer powers use the exact endpoint range, including0
for an even power crossing0. Square roots use verified integer squared
inequalities. Induction over this expression graph proves inclusion.
The square value range in (5) and its propagated derivative ranges need
not be independent or simultaneously attained; enclosing each separately
is valid. No result intersections are used to narrow the evidence.

The base intervals satisfy the weaker rational bounds

    h_0=1,
    0.046209 < h_1 < 0.046212,
    0.003824 < h_2 < 0.003825,
    0.000436 < h_3 < 0.000437.

All99 executed reciprocal divisions have strictly positive input lower
endpoints, including the point's normalized quantities and both update
divisors. The full collar update value is

    [57353061649999427835432132832043829802624813700995013/10^50,
     7356944911507680245224346931478959249122343572937320367/10^50].

It proves (1). The complete collar variance value is

    [-1118463952817667705569661925865477998273697991324198801/(5*10^49),
      137107526243041901040766657432250636331662276054171621/(4*10^48)].

It proves (2). The complete value/derivative records, not previews,
were inspected. The same failed variance is required by both signs,
so neither residual range nor nonlinear sufficient test was evaluated.
Rump, *Verification methods*, Acta Numerica19(2010),
[Theorem13.3, corrected PDF pp87-89](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
as assessed in source-notes1924, would require the full normalized
box-Jacobian and strict inclusion in the chosen radius1/4 box. Its
hypotheses cannot be certified by this evaluation; no theorem conclusion
is invoked. No correctness of the unexecuted Krawczyk branch is needed.

The independent checker imports no1928 producer code. It replays all3560
expression nodes/endpoints, all99 divisor records and every result copy.
It checks complete cleared-denominator base orthogonality/norm identities,
the Gram identity in eight independent formal entries and both adjugate
row identities. It checks the quoted rational bounds and both honest
stop statuses. Point coefficient/derivative and actual-target overlaps
with1925 are consistency checks only, never narrowing operations. All
11019 checks pass, with an empty arithmetic/algebra failure list. This
is finite verification, not independent Decimal validation or the later
separate proof audit. The failed numerical positivity requirement remains
explicit despite the empty implementation-check failure list.

The conclusion is a paid update divisor followed by an unpaid variance
enclosure. C028t's local rank remains valid; C028u's earlier failed
Cramer bound is preserved. Outside-collar feasibility, other degrees,
full costs and H_d=o(d) remain open. Two failed natural whole-box
representations warrant parking this implementation route pending a
materially different, separately assessed mechanism, not another sweep.

### Separate proof/code/evidence audit1930

20 November 2026. Assessment review1928, separately approved1929, covers
exactly this audit. The conditional claim passes. This establishes safe
local reuse of the completed finite specialization, not new mathematics
beyond the imported sources and not an actual matching result. The
reported recovery issue does not occur in the supplied checkpoint: its
Next action equals the assessment's TARGET exactly. No source gate was
changed during this research step.

**Imported hypotheses and finite algebra.** Reuse the full primary
statement/proof assessments in source-notes1908/1920/1924/1926. L019's
strictly positive density and decay give every absolute moment and
positive norm for every nonzero polynomial. The two positive atoms
preserve this, verifying both quasi-definiteness hypotheses in Delgado
et al Theorem3.1. The even normalization gives exactly I_(2j)/I_0;
division of the modified measure by3 changes no monic polynomial.
The stated mixed-measure zero theorem applies only to the reference.
Gautschi's construction and the orthogonality checks in(4) identify
p_0,...,p_4 uniquely. The kernel uses h_0,...,h_3 only. The checker's
cleared p_3 is u*p_3; its squared norm is u*(u*w-v^2), giving exactly
h_3=w-v^2/u after division by u^2. No missing h_4 or numerical base
moment of order8 is needed. Actual b_4 still requires I_8 and its
factorial conversion. No actual-root reality is assumed.

The matrix is symmetric, so the displayed two weights agree with the
source's row convention. Expanding the product of its two diagonal
kernel sums and pairing indices j<l gives exactly the six squared
minors in(5). The checker's eight-variable identity uses
X_j=p_j(a)/sqrt(h_j), Y_j=p_j(b)/sqrt(h_j); hence its polynomial
identity proves the weighted identity actually used. The two independent
adjugate row identities check both weights, not merely det M>0.

**Complete differentiation and observable semantics.** The entire
producer and executed helper code were inspected. The site seeds are
(a,1,0),(b,0,1); base moments and coefficients have zero site derivatives.
Horner evaluation therefore gives, in order, p_j' equal to
0,1,2x,3x^2-v/u,4x^3-2Ax. In particular
partial_a kaa=2 sum_j p_j(a)p_j'(a)/h_j,
partial_a kab=sum_j p_j'(a)p_j(b)/h_j, and the analogous b derivatives
retain the second kernel argument. Each minor's two derivatives follow
the product rule. Its sharply enclosed square carries derivative
2*minor*partial_s minor. Thus Delta and both numerators retain every
site derivative. Reusing the same enclosed quotient in
W_s=(N_s-W*Delta_s)/Delta is valid inclusion; it imposes no false
independence or correlation between those quantities.

For each k=0,...,3, the coefficient of x^k in K_3(a,x) is precisely
sum_(j=k)^3 p_j(a)*(coefficient of x^k in p_j)/h_j.
The coefficient extraction includes all such terms and both derivatives
of W_a*K_3(a,x)+W_b*K_3(b,x). The monic leading coefficient is1.
Newton sums use all four coefficients, empirical division4, and both
centering derivatives. In particular
partial_s V=partial_s P_2/4-2*(P_1/4)*(partial_s P_1/4),
where partial_s P_2=-(partial_s c_3*P_1+c_3*partial_s P_1+2*partial_s c_2).
At the point, the executed helper also retains every T,Q and variance
normalization derivative. At the collar it returns immediately after
the failed V bound; no normalized collar observable is evaluated.

**Complete inclusion and preserved evidence.** Run
`python3 scripts/heat/two-site-positive-update-audit-1930.py`.
The wrapper preserves every original1925/1928 certificate and writes
the complete producer reproduction to
`scripts/heat/two-site-positive-update-replay-1930.json`, its independent
checker reproduction to
`scripts/heat/two-site-positive-update-check-replay-1930.json`, and the
inherited1925 checker replay to
`scripts/heat/two-site-actual-collar-check-replay-1930.json`.
The producer is byte-for-byte identical to1928. Every checker field
agrees; only the1928 checker's certificate path changes, with the same
certificate hash. The1925 checker reproduces in full, including its
19685 checks of all6530 trace nodes and symbolic components. Its point
overlaps are consistency tests only, not proof by overlapping intervals
and not a narrowing operation.

Every selected raw moment record, including complete I_8 endpoints,
equals the unchanged source, accepted audit197 and1925 records. All
input registers and original checker hashes were checked. The closed
panel contains lambda=0. This reuses L917's accepted analytic containment
under L037 and does not reverify quadrature or the Decimal library.
The inspected Fraction operations, signed four-corner products,
floor/ceiling, integer-power ranges and squared-endpoint square-root
checks prove inclusion by induction over the full executed graph.
The positive square range and its derivative enclosures may be attained
at different sites; separate inclusion remains valid. Ordinary repeated
multiplication, used elsewhere for powers, may overestimate but remains
enclosing. No midpoint moments or intersections replace an input.

The independent replay checks every one of3560 nodes,99 divisors and
all saved value/derivative copies, together with the full algebraic
identities. All11019 checks reproduce without failures. The executed
reciprocals split into8 base,5 actual-target,46 point and40 collar
divisions. The base uses four divisions by I_0, two by u and two by h_2;
the actual target uses three constant and two normalization divisions.
Each reference evaluation uses12 kernel,6 minor,2 weight and20 kernel
coefficient divisions; the point additionally uses6 normalized-observable
and Jacobian divisions. All full input intervals have positive lower
endpoints. No reciprocal of the failed collar variance was executed.

The wrapper certificate
`scripts/heat/two-site-positive-update-audit-1930.json` records47 passing
audit checks, every full divisor, source/output hashes and actual/required
bounds. Exact Fraction comparisons verify all four quoted norm bounds,
both printed complete Delta and V endpoints, and strict inequalities
(1)-(2). The trace ends at V's second site derivative, and both sign
records explicitly omit residual-range and Krawczyk evaluation. The
mathematical threshold failure, V_lo<=0, is retained separately from
the empty arithmetic/algebra failure list. Exact V>0 supplies no lower
bound that licenses this interval's reciprocal. No theorem about
nonmatching, global feasibility, other degrees, full costs or H_d=o(d)
follows. C028t's accepted rank and C028u's earlier stop survive. The
existing DAG inputs capture the mathematical uses and are unchanged.

## Mathlib

Full matching coverage is unchecked. Supporting finite matrix and
polynomial identities do not constitute a formalization of these
conditional numerical bounds. No absence claim or Lean verification
is made. Reference: https://leanprover-community.github.io/mathlib4_docs/.
