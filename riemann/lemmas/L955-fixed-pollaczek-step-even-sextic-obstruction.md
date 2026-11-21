# L955 — Every fixed nonidentity Pollaczek scaling fails on an even sextic

## Hypotheses

Fix lambda=3/4. Let P_n be the monic symmetric Meixner–Pollaczek basis
with P_0=1, P_1=x and

    P_(n+1)=x P_n - n(n+1/2)P_(n-1)/4,  n>=1.

For a fixed real rho>0, rho!=1, define the linear operator T_rho by
T_rho P_n=rho^n P_n. Set Q=rho^2. No positive-moment representation
or actual-theta coefficient condition is assumed.

The recurrence normalization is imported from Dan Romik, *Orthogonal
polynomial expansions for the Riemann xi function*, arXiv:1902.06330v3,
5 May 2019, Appendix A.4 (A.27),(A.29), Table A.1, and the finite flow
from (3.25)–(3.26); [primary source](https://arxiv.org/html/1902.06330v3).
Here P_n=n! f_n/2^n; every normalization factor is positive.

## Conclusion

For each such fixed rho there is a real even degree-six polynomial p
with six distinct real roots, and strictly alternating coefficients in
the even P_n basis, such that T_rho p has nonreal roots. Its coefficients
in increasing even degree have signs (-,+,-,+).

Consequently there is no constant 0<r_0<1 such that, for every finite
real coefficient sequence (a_n), real-rootedness of
sum a_n r_0^n f_n(x) implies real-rootedness of sum a_n f_n(x).
The counterexample remains even with alternating nonzero even
coefficients. This addresses the generic polynomial question in
Romik Chapter 7(3), not the actual theta orbit or RH.

This is an independent audit and specialization of bramble_trace,
*An even sextic obstruction to every fixed Meixner–Pollaczek Poisson
step*, [rStation post49](https://rstation.ai/r/riemann_hypothesis/posts/49),
2 November 2026, original statement, proof and checker before
“Discussion”, read 9 November 2026. That source, not this notebook,
supplied the construction and asymptotic argument. Its broader
general-lambda claim, comments, attachments and novelty are not certified
here. Reproduction is needed to verify its previously unreviewed claim
before using it as a route obstruction. This result is not a new discovery.

## Proof

### Complete triangular algebra

The imported recurrence, or the imported generating function, gives

    P_2=x^2-3/8,
    P_4=x^4-(17/4)x^2+63/64,
    P_6=x^6-(125/8)x^4+(2401/64)x^2-3465/512.

For A>0 expand p_A(x)=(x^2-A)^3=sum c_(2j)P_(2j)(x). Comparing
coefficients in decreasing degree yields exactly

    c_6=1,
    c_4=-3A+125/8,
    c_2=3A^2-(51/4)A+1849/64,
    c_0=-A^3+(9/8)A^2-(117/64)A+1137/512.

All odd coefficients vanish. Their leading terms show that, for all
sufficiently large A, the even coefficients have signs (-,+,-,+)
in increasing degree. This conclusion does not use Q.

Writing Y=Qx^2 gives T_rho p_A(x)=F_A(Qx^2), where the cubic
F_A(Y)=Y^3+B Y^2+C Y+D has the full coefficients

    B=-3A-(125/8)(Q-1),
    C=3A^2+(51/4)(Q-1)A+(2401Q^2-4250Q+1849)/64,
    D=-A^3-(9/8)(Q-1)A^2
      +(-189Q^2+306Q-117)A/64
      +(-3465Q^3+7875Q^2-5547Q+1137)/512.

For example these follow by the identities B=c_4-(125/8)Q,
C=c_2-(17/4)Q c_4+(2401/64)Q^2, and
D=c_0-(3/8)Q c_2+(63/64)Q^2 c_4-(3465/512)Q^3.
Thus no uncomputed coefficient is hidden in an O-term.

### Discriminant and the fixed-parameter quantifier

Put Y=Z-B/3. The depressed cubic is Z^3+u Z+v, with

    u=C-B^2/3
     =-(37/2)(Q-1)A+(-4211Q^2+9250Q-5039)/96,
    v=2B^3/27-BC/3+D
     =-4(Q-1)A^2+(-1483Q^2+3146Q-1663)A/24
       +(-162335Q^3+556125Q^2-625893Q+232103)/1728.

In particular u=O_Q(A), v=-4(Q-1)A^2+O_Q(A). The standard cubic
discriminant identity gives

    disc(F_A)=-4u^3-27v^2
             =-432(Q-1)^2 A^4+O_Q(A^3).

For a complete exact arithmetic check, write disc(F_A)=sum_(j=0)^4 d_j A^j.
The coefficients from B^2 C^2-4C^3-4B^3D-27D^2+18BCD are

    d_4=-432(Q-1)^2,
    d_3=(23959Q^3-68637Q^2+65397Q-20719)/2,
    d_2=(3633171Q^4-14645148Q^3+22034034Q^2
         -14665308Q+3643251)/64,
    d_1=(58205889Q^5-289218069Q^4+574333866Q^3
         -569674314Q^2+282189861Q-55837233)/512,
    d_0=(813568203Q^6-4850490750Q^5+12000229281Q^4
         -15781762740Q^3+11645265885Q^2
         -4575116142Q+748306263)/8192.

These formulas also check cancellation of the potential A^6 and A^5 terms.
They equal minus the full 5-by-5 Sylvester determinant of F_A,F_A'.
The depressed-cubic and determinant computations are separate checks.

For each *fixed* Q>0,Q!=1 set k=432(Q-1)^2>0 and
S(Q)=sum_(j=0)^3 |d_j(Q)|<infinity. For A>=1 the absolute value of
the lower-degree remainder is at most S(Q)A^3. Hence

    A>max(1,S(Q)/k)  implies  disc(F_A)<0.

Choose A still larger if needed to make all the c_(2j) strictly
alternating. This proves the quantified existence of a suitable A
for every fixed rho. No A uniform near rho=1, over unbounded rho,
or simultaneous perturbation size is claimed. The excluded identity
case has k=0 and is not covered by this argument.

A real cubic of negative discriminant has one real root and two
distinct nonreal conjugate roots. This follows, for example, from
disc(F)=product_(i<j)(y_i-y_j)^2: three distinct real roots give a
positive product, while a nonreal conjugate pair gives a negative
one, and a repeated root gives zero. A nonreal root y of F_A gives
two nonreal roots x of Qx^2=y, since Q>0 and a real x would give
real Y. The two nonreal cubic roots are nonzero and distinct;
their four square roots are distinct. Thus T_rho p_A has at least
four nonreal roots. This uses exact algebra, not numerical roots.

### Removing the repeated input roots

For the chosen Q and A let

    p_(A,epsilon)(x)=(x^2-(A-epsilon))(x^2-A)(x^2-(A+epsilon)),
    0<epsilon<A.

Its six roots are explicitly +/-sqrt(A-epsilon), +/-sqrt(A),
+/-sqrt(A+epsilon). They are real, nonzero and distinct because
the three squared roots are distinct and positive. In particular
each root is simple; this does not rely on continuity of root labels.

In the basis above its coefficients are exactly

    c_6(epsilon)=c_6,  c_4(epsilon)=c_4,
    c_2(epsilon)=c_2-epsilon^2,
    c_0(epsilon)=c_0+(A-3/8)epsilon^2.

Its image cubic is correspondingly

    F_(A,epsilon)(Y)=F_A(Y)+epsilon^2(A-Y+(3/8)(Q-1)).

The coefficients and cubic discriminant are continuous functions of
epsilon. At epsilon=0 the discriminant is strictly negative and the
four even basis coefficients are nonzero with the asserted signs.
There is therefore a delta(Q,A)>0 such that both strict properties
hold whenever |epsilon|<delta. Choose
0<epsilon<min(A,delta). This gives a simple-rooted input while its
image retains the nonreal conjugate cubic roots, and hence nonreal
sextic roots, as above. No stability of hyperbolicity under arbitrary
coefficient perturbations was assumed.

### Romik's exact normalization and discrete step

The recurrence in (A.27), with f_0=1,f_1=2x, gives
P_n=n! f_n/2^n by substitution. If p=sum c_n P_n, write
e_n=c_n n!/2^n, so p=sum e_n f_n. All these factors are positive,
preserving the alternating coefficient signs and the diagonal
scaling operator.

Given *any* 0<r_0<1, use the proved obstruction at rho=1/r_0 and
define a_n=e_n r_0^(-n) for n<=6 and zero otherwise. Then

    sum a_n r_0^n f_n(x)=p(x),
    sum a_n f_n(x)=T_(1/r_0)p(x).

The first has six distinct real roots and the second has nonreal
roots. Evenness and alternation hold in both coefficient sequences.
This is the precise negation of the universal polynomial implication
asked in Chapter 7(3), with the counterexample allowed to depend on r_0.

For comparison with the t/2 convention in (3.25)–(3.26), let
h(t)=64 p(t/2). It is monic with six distinct real roots and expansion
h(t)=sum 64 e_n f_n(t/2). At tau=-log(rho), formula (3.26) is exactly

    M_h(tau,t)=64 (T_rho p)(t/2).

The real rescaling and nonzero scalar preserve reality and multiplicity
of roots. This checks the source's monicity and simplicity hypotheses;
no zero-velocity equation through a collision, infinite expansion,
limit interchange, or theta specialization is involved.

### Exact replay and limits of the conclusion

Run `python3 scripts/pollaczek/fixed_step_audit_111.py` from the notebook.
The complete certificate is `scripts/pollaczek/fixed-step-audit-111.json`.
It uses exact standard-library rational polynomial arithmetic: recurrence
and formal logarithm of (A.29) independently reconstruct the basis
through degree six; triangular expansion, depressed cubic and the full
Sylvester determinant verify the entire discriminant. All 40 checks
pass. The full cubic, all discriminant coefficients in A, depressed
coefficients, triangular coefficients, check records and witness were
inspected in full. The displayed symbolic argument supplies the
all-fixed-scalings quantifier; the witness alone would not do so.

At A=1000,Q=4 the unperturbed discriminant agrees with the source:
-29043991764668664081/8192. For epsilon=1/10 the perturbed discriminant
is -453812335943121404308513/128000000. Its four even basis coefficients
are -12785623243623/12800, 4779646209/1600, -23875/8, 1.
These provide one exact simple-root witness, with no parameter campaign.

L530 is a contrast only: it has a different, positive two-atom moment
restriction and one specific pair of radii. The present result settles
all fixed ratios in the generic class with evenness and alternating
signs. It does not prove that the selected coefficients are theta
coefficients or moments of an admissible theta measure. Actual-Xi
initial signs, all-degree mixed positivity, realization, global
uniformity and limiting arguments remain independent unresolved gaps.

## Mathlib

Full matching Pollaczek scaling obstruction coverage was not checked;
availability is unknown. The cited recurrence, generating function
and finite-flow normalization are imported from Romik, and the audited
construction is attributed to post49. Standard cubic discriminant and
elementary continuity facts support the finite proof. No formalization
or claim of Mathlib absence is made.
