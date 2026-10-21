# L174 — Complete action-Hessian coefficient and actual-probe signs

## Hypotheses

Keep precisely L173's SU(2) action-Hessian branch T_i, i=3,6,
all-face relative box D=(-4,4)^4, a=8/N through admitted even meshes,
straight direction-1 lower-rooted forest, complete L008 compact
divergence-free displacement u, actual L010 probes and tau=1/16.
The bare expansion is taken at fixed mesh before refinement.
Import L173(2),(8)'s established limit K_(i,T), including its -6,
four endpoint pairs, displacement/exterior/slope terms and both
Q subtractions. No new mesh limit is taken here.

Let G(n) be L153(2)'s infinite three-dimensional scalar Green function,
X=G(000)-G(110), Y=G(110)-G(111). Import L153's one-color kernel
h_(mu nu)=H_(i,mu nu)(x,x), j_(mu nu;r)=partial_(x_r)
H_(i,mu nu)(x,y)|_(y=x), and its six physical forms T_(i,A),...,T_(i,F).
All physical component sums are transverse, 2,3,4, and d=x_1+4.
L154(3) matches this kernel exactly to L173(6) and the coefficients
of L132's P_(i,D),P_(i,A),P_(i,X),P_(i,C) and L145's B_(i,R).
L154(5)-(6)'s integration identities and L153's absolute heat bounds
are imported with their hypotheses verified below.

For signs, import L133's full-spectrum intervals and L154 section 3's
exact rational full-cell Green intervals. L133's heat premises retain
L039's stated IEEE addition/multiplication/FMA, no-overflow and underflow
qualifications. They are informal computer-assisted inclusions, not
formal processor or BLAS verification. The new row contraction and
interval recombination use only integers and rational arithmetic.

## Conclusion

The complete action-Hessian coefficient is

    K_(i,T)=(17-90X+15Y)P_(i,D)
           +(-10+78X-9Y)P_(i,A)
           +(-3/2+6X+3Y)P_(i,X)
           +(12-60X-30Y)P_(i,C).                         (1)

Equivalently, with L154's complete quartic coefficient Lambda_i,

    K_(i,T)=-2 Lambda_i+(28-144X+12Y)B_(i,R).             (2)

No additional color or outside factor three occurs. Under the imported
heat qualifications the strict actual-probe bounds are

    84000 < K_(3,T) < 100000,
   -47000 < K_(6,T) < -38000.                            (3)

Thus this branch has a nonzero cubic coefficient for both actual probes.
The complete cubic residual/action response remains undecided: L159's
smooth-action branch V_i still lacks a scaled limit. With L172's
E,E coefficient -6K_(i,R), vanishing requires an independently justified
limit lim a^3 V_i=6K_(i,R)-K_(i,T). An O(a^-3) bound does not supply it.
Other response jets, full compensation, finer powers/logarithm, finite
matching, interacting reflected error <=c_box/2, continuum axioms and
infrared finite positive mass remain open. No candidate exists.
This is local standard-method REPRODUCTION, without a novelty claim.

## Proof

### 1. Match physical normalization before contracting

L173(6) uses b_(i,kl)=q_i(f_k/sqrt(lambda_k),f_l/sqrt(lambda_l))
and ell_k equal to the transverse forest lift V_k. L154(3) establishes
exactly this equality for L152/L153's kernel. Hence all three uses have

    H_(i,mu nu)(x,y)=sum_(k,l) c_(i;kl)
                                  V_(k,mu)(x)V_(l,nu)(y),
    c_(i;kl)=exp[-(lambda_k+lambda_l)/16]q_i(A_k,A_l).

There is one covariance normalization in q_i and one in each V.
The scalar entry h is one color, and the -6 in L173 already includes
the three-color contraction. The symmetry of c gives h_(mu nu)=h_(nu mu)
and partial_r h_(mu nu)=j_(mu nu;r)+j_(nu mu;r). Axial exterior
components vanish on every supported row. Restricting the two exterior
indices to transverse components thus deletes no surviving term.
The constant axial mode in V, its actual lower primitive, both probe
sectors and all heat modes remain.

### 2. Enumerate the full finite row, including the adjoint and Q_6

Here are finite formulas specifying the entire computation. Use lattice
tails z in Z^4 and positive links (z,mu), directions 1,...,4. For rho!=nu
write the curl row

    D_(rho nu,z) x=x_(z+e_rho,nu)-x_(z,nu)
                            -x_(z+e_nu,rho)+x_(z,rho).

Its clover at vertex v is

    C_(rho nu,v)=(1/4) sum_(a,b in {0,-1})
                                  D_(rho nu,v+a e_rho+b e_nu).

This is antisymmetric in rho,nu. For edge e=(0,mu) set c_e=e_mu/2,
and let k[v] denote the finite matrix

    k[v]_(bf)=(1/2) sum_(z in endpoints b) sum_rho
                                  v_rho(z) C_(rho,dir(b),z)(f).

The endpoint factor is 1/2, not 1/4. L is the ordinary unscaled
curl-square matrix. Thus

    A^gen[v]_(ef)=(1/2) sum_b
                           [L_(eb) k[v]_(bf)+k[v]_(be)L_(bf)].     (4)

Both terms in (4) use v at the original endpoints of b. In the
second term the coefficient is not frozen at e before transposition.
For displacement component rho define alpha^rho by v_sigma=delta_(sigma rho)
and beta^(rho j) by v_sigma(z)=delta_(sigma rho)(z_j-c_(e,j)), followed
by subtraction of the constant-strain row Q^(rho j).

For this row Q_3 is D^T W D, with plane weight w_a+w_b and
w_a=delta_(a rho)delta_(j rho). Its constant coefficient keeps the
average of plaquette squares. Q_6 is the row of the polarized form

    (1/2) sum_(v,a<b,eta) s_(ab)
       [C_(a eta,v)(e) C_(b eta,v)(f)
                       +C_(b eta,v)(e) C_(a eta,v)(f)],            (5)

where s_(ab)=delta_(a j)delta_(b rho)+delta_(b j)delta_(a rho).
These are precisely L008's forms and L028's compositions. Formula (5)
keeps the cross-entry halves and both clovers. Replacing Q_3 by a
clover square would change this computation.

For each row use L173's four-endpoint W and S. If f has direction nu,
let r_f be its midpoint minus c_e. The three contributions, before
the outside -6, have coefficient arrays

    C_(mu nu;rho j)=sum_(f:dir(f)=nu) beta^(rho j)_(mu f) W_(mu f),
    D_(mu nu;rho j)=sum_(f:dir(f)=nu) alpha^rho_(mu f) W_(mu f) r_(f,j),
    E_(mu nu;rho)=sum_(f:dir(f)=nu) alpha^rho_(mu f) S_(mu f).      (6)

All sums (4)-(6) are finite rational combinations of G(n). The vertex
arguments in W are actual endpoints, not edge midpoints. In S subtract
c_(e,1) from (v_1+w_1)/2; this keeps the axial slope in L173(5).

Insert (6) in L173(8), and integrate the C term by parts:

    integral d (partial_j u_rho) h_(nu mu)
       =-integral d u_rho [j_(nu mu;j)+j_(mu nu;j)]
                          -delta_(j1) integral u_rho h_(nu mu).  (7)

No boundary term remains because u has compact support. Equation (7)
must retain the derivative of d. It is applied only after all affine
rows and both subtractions have been collected. Now sum all ordered
mu,nu, using symmetry of h. Direct evaluation of the finite formulas
(4)-(7), retaining -6, gives exactly the six forms of L153(3), with
the following coefficients. Put g0=G000, g1=G100, g2=G200,
g11=G110, g21=G210, g111=G111 and g211=G211; coordinate signs and
permutations do not affect G.

| Form | Complete coefficient before Green recurrences |
| --- | --- |
| T_A | -36g0-12g1-12g2+48g11+12g21 |
| T_B | -18g0-6g1-6g2+24g11+6g21 |
| T_C | -84g0+12g1-12g2+96g11-12g21 |
| T_D | -30g0-12g1+6g2+18g11-12g21+24g111+6g211 |
| T_E | 3g0+6g1+9g2-9g11+6g21-12g111-3g211 |
| T_F | 3g0-3g2-3g11+3g211 |

For completeness, the table represents all remaining tensor entries:
T_A has u_1 j_(rr;1) for each r; T_B has u_1 h_(rr);
T_C has u_r j_(rr;r); T_D has u_r j_(kk;r), k!=r;
T_E has u_r j_(rk;k), k!=r; and T_F has u_r j_(kr;k), k!=r.
Each derivative term has weight d, and the unequal-index sums are
ordered. All unlisted entries vanish. There are 27 nonzero collected
entries, not six selected entries with the others assumed zero.

The table is also provided as a reproducible exact finite certificate.
`scripts/combined-ward-response/contract_action_hessian_limit.py`
implements the displayed incidence/clover, endpoint, adjoint, insertion
and endpoint-Green formulas with Fraction arithmetic. It saves all 60
principal/affine rows, separate affine generator and insertion rows,
324 pre-IBP coefficient records, all assembled entries and checks in
`scripts/combined-ward-response/action-hessian-limit-contraction-certificate.json`.
Its transpose support is the union of uncollected vertex-clover supports;
constant-coefficient cancellations cannot delete an affine entry.
All 36 frozen row contractions vanish as formal Green combinations,
and all 60 full rows annihilate the vertex gradient exactly. The entire
assembled tensor, including its zero entries, is compared to the table
after the four Green identities below. This is finite exact arithmetic
for a specified tensor, not a numerical mesh-asymptotic premise.

### 3. Reduce the Green coefficients and the physical forms

The absolutely convergent Fourier definition of G gives Delta_T G=delta_0:
multiply its integrand by lambda and integrate each finite character.
At 000, 100, 110 and 111, respectively, cubic symmetry gives

    6g0-6g1=1,
    6g1-g0-g2-4g11=0,
    6g11-2g1-2g21-2g111=0,
    6g111-3g11-3g211=0.                                (8)

With g11=g0-X and g111=g0-X-Y, these equations express every table
entry using g0,X,Y. The g0 coefficient cancels in every entry. The
result is

    K_(i,T)=A T_(i,A)+B T_(i,B)+C T_(i,C)
                                  +D T_(i,D)+E T_(i,E)+F T_(i,F),
    A=16-120X+12Y,       B=8-60X+6Y=A/2,
    C=8-120X-12Y,        D=-6-48Y,
    E=-9+48X+24Y,        F=3-12X-6Y.                    (9)

All integration identities in L154(5)-(6) apply: their H is the same
kernel, u is the same compact divergence-free displacement, and d the
same lower-prefix weight. They retain both diagonal corrections in the
ordered unequal-index sums. Explicitly,

    T_A=(P_D-B_R)/2,             T_B=B_R,
    T_C=-P_A/2,                 T_D=(P_A-P_D)/2,
    T_E=(P_A-P_D)/2-P_C,
    T_F=(P_D+P_A-P_X)/2+P_C.                            (10)

The B_R coefficient is B-A/2=0, rather than an omitted prefix term.
The four remaining coefficients are (A-D-E+F)/2,
(-C+D+E+F)/2, -F/2 and F-E. Substitution of (9) proves (1).
Comparison with L154(1) proves (2). No value of Lambda_i or B_R is
needed for this exact identity. Differentiation and IBP may first be
performed at a mode cutoff; the absolutely convergent differentiated
heat sums in L173/L153 justify their full-spectrum versions.

### 4. Import complete intervals and recombine with rational endpoints

Use L154's established complete Green intervals with exact endpoints

    X in [793568754697647013092925833111229/4096000000000000000000000000000000,
          6598685808758937548219796508417531/32768000000000000000000000000000000],
    Y in [679506827491627244057509060949181/65536000000000000000000000000000000,
          168531959559512088933042812603947/13107200000000000000000000000000000].

These are the full-cell inclusion, including its origin cell; no
decimal preview or new quadrature is used. Import L133's complete
qualified heat intervals in the matched normalization:

| Probe | P_D | P_A | P_X | P_C |
| --- | --- | --- | --- | --- |
| 3 | (2359.1,2359.2) | (19170.0,19170.1) | (29198.8,29198.9) | (1024.8,1024.9) |
| 6 | (703.6,703.7) | (-4195.9,-4195.8) | (69177.0,69177.1) | (3218.2,3218.3) |

Each decimal endpoint here is an exact terminating rational. Evaluate
each affine coefficient of (1) outward using the exact X,Y intervals.
For coefficient interval [l,h] and heat interval [s,t], enclose their
product by min/max of ls,lt,hs,ht, then sum all four intervals. Treating
the common X,Y independently in different terms enlarges the result
and is valid without an independence assumption.

The exact endpoint totals are saved in the certificate's `enclosures`.
They are contained in (84064.7309,99719.2761) for probe 3 and
(-46942.9681,-38440.9380) for probe 6, in turn strictly inside (3).
The decimal comparisons just displayed are outward weakenings of the
saved rational endpoints. The script compares the rational totals
directly to the required 84000,100000,-47000,-38000 endpoints.
All 275 finite-row/tensor/Green/physical-transform/qualified-interval
checks pass, with zero failures. Reproduction command:

    python3 scripts/combined-ward-response/contract_action_hessian_limit.py

No upstream heat or Green-cell audit is rerun or claimed. Those inputs
are the canonical established results under their existing qualifications.
This signed coefficient cannot be assigned to V_i, the full isolated
cubic response or the full Ward correction.

## Mathlib

Full matching action-Hessian contraction, scalar lattice Green recurrence
and imported heat-enclosure coverage: **not checked**; unknown is not
absence. The finite bilinear polarization, Fraction coefficient
enumeration, Fourier character orthogonality, compact-support IBP and
interval products are standard methods. The unchanged
[assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md)
supplies no matching isolated pinned-forest coefficient theorem to
import instead of this calculation. L153/L154 are a different residual
polynomial: only their exactly matched kernel definitions, Green bounds
and physical identities are reused, and (2) is proved by this separate
complete-row contraction. L133 supplies qualified full-spectrum bounds,
not a new discovery or an independently verified heat calculation.
