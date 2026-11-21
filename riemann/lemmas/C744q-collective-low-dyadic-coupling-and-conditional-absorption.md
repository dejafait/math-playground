# C744q: One neutral profile against a finite dyadic high block

## Hypotheses

Fix ell=log(3)/2, finite M0,M>=1 and the real nonnegative
chi in C_c^infinity(0,ell), positive on a nonempty open interval,
used in C744n. For R>=e^3 set

    y=log R, K_R=floor(log log R/ell), L_R=K_R ell,
    t_j=2^j R, y_j=log(t_j), 0<=j<J,

where J>=1 is any finite integer. Use L744(1)'s smooth complex
cell-train families on this common window. Thus u in F_(K_R,M0)
and w_j in F_(K_R,M) have unit unweighted L2 norm, and their smooth
zero extensions have H2 norms at most M0 and M respectively, with

    ||z||_H2^2=||z||_2^2+||z'||_2^2+||z''||_2^2.

Require, in every cell k and for each sigma in {+1,-1},

    integral_0^ell exp(sigma s/2)u_k(s) ds=0.                 (1)

Use precisely C744p's v_j=exp(it_j x)w_j-h_j, with C744n(1)'s
unchanged complex-linear correction on K_R cells. In particular
b_tau(s)=chi(s)exp(tau s/2), G_(sigma,tau)=integral_0^ell
chi(s)exp((sigma+tau)s/2) ds, and

    d_(j,k,sigma)=exp(it_j k ell)
          integral_0^ell exp(sigma s/2)w_(j,k)(s)exp(it_j s) ds,
    h_j(x)=sum_(k,tau) (G^-1 d_(j,k))_tau b_tau(x-k ell).

G is the fixed invertible matrix of C744n. For arbitrary complex c_j
put g=sum_j c_j v_j and S=sum_j y_j|c_j|^2. Use the original complete
energy E_L(z)=-Re<A_L z,z> and its Hermitian polarization

    mathcal E_L(a,b)=-(<A_L a,b>+<a,A_L b>)/2,                (2)

with first-slot-linear inner product. All functions and finite
combinations are in the actual smooth generator domain as in C744o.
No sign of E_(L_R)(u) or RH is assumed. Empty families assert no
existence. The profiles may vary arbitrarily with R,J and j subject
to these hypotheses.

## Conclusion

There is a finite C=C(M0,M,chi), explicit in (4) below, such that
for every admitted choice at every R>=e^3,

    |mathcal E_(L_R)(u,g)| <= C sqrt(log R) R^-2 sqrt(S).     (3)

In addition let R>=R_*(M,chi), the single onset in C744p(1), and
write e=E_(L_R)(u), eps=C sqrt(log R)/R^2. For every complex a,

    E_(L_R)(a u+g)
       >= (1/8)(sqrt(S)-8eps|a|)^2+(e-8eps^2)|a|^2,
    E_(L_R)(a u+g) >= (e-16eps^2)|a|^2+S/16.

Consequently the independently established original-energy margin

    e >= 32 C^2 log R/R^4

is sufficient for E_(L_R)(a u+g)>=e|a|^2/2+S/16, strictly positive
unless a=0 and c=0. Merely e>8eps^2 also suffices for strict positivity
of every nonzero coefficient pair. These are sufficient conditions,
not necessary conditions or assertions that any such margin holds.

This is a REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-11-11-collective-low-dyadic-coupling-506.md`,
11 November 2026, step508. It is a standard quantitative application,
not a discovery beyond the sources checked. The separate conceptual
audit below (11 November 2026, step510) accepts (1)-(9) and both
conditional absorption bounds without repair. This supplies neither
a low sign nor an RH candidate.

## Proof

### Complete common-window input and explicit constants

Set c_RS=1.03883 and

    A=2+8sqrt(2)/3+log(4pi),
    H=||G^-1|| (||b_+||_H2^2+||b_-||_H2^2)^(1/2)
                                sqrt(33 ell exp(ell)/8) M,
    D=4M0 M(1+A/3)+(A+3)M0 H/3+4c_RS(4M0 M+H),
    C=D sqrt(16/15+16log(2)/675).                           (4)

These constants depend only on M0,M,chi and the fixed ell.
We use C744o(8)-(11), which were proved for every finite K>=2
before its own-window substitution. In particular we do not identify
K_R with K(t_j). Here K_R>=2 and L_R<=log log R for R>=e^3.
For T=t_j>=R, those estimates on the common window give

    |mathcal E_(L_R)(u,v_j)| <= T^-2 {
       4M0 M[A+log(2+T/2)]+(A+3)M0 H
                       +4c_RS sqrt(y)(4M0 M+H)}.            (5)

For clarity, C744o(4) is the complete polarization with both pole
products F_u(i/2)conj(F_v(-i/2)) and F_u(-i/2)conj(F_v(i/2)),
where F_z(xi)=integral z(x)exp(-i xi x)dx. Condition (1) and the
exact correction kill both global moments of u and v_j. Its remaining
form is Q_m(u,v_j)-<B_(L_R)u,v_j>, with
m(xi)=Re psi(1/4+i xi/2)-log pi and
B_L=sum_(2<=n<exp L) Lambda(n)/sqrt(n)(T_(log n)+T_(log n)^*).
Thus (5) retains the whole correction and all prime powers.
The prime mass used here is C744o(11)'s 4c_RS exp(L_R/2), at most
4c_RS sqrt(y). Neither intermediate uncorrected pole terms nor a
prime-only replacement are being dropped.

The underlying analytic imports, already specialized and audited in
C744o, are Vasy, *Math 172: The Fourier Transform — Basic Properties
and the Inversion Formula*, author-hosted notes, pp.1-2 and Lemma 0.4,
p.13 (https://math.stanford.edu/~andras/172-4.pdf); NIST DLMF 5.11.2
and 5.11(ii) (https://dlmf.nist.gov/5.11.E2 and
https://dlmf.nist.gov/5.11#ii); and Rosser--Schoenfeld, Illinois
J. Math.6 (1962),64-94, Theorem12/(3.35), p.71
(https://doi.org/10.1215/ijm/1255631807). Smooth zero extensions,
the same right-half-plane digamma line, and the inclusive prime-power
mass are unchanged. We import those results and C744o's estimates;
no reproof of Fourier identities, scalar asymptotics or the prime
estimate is needed. The new obligation is their common-window finite
weighted application below.

Since T>=e^3>4, log(2+T/2)<=log T=y_j. Also y_j>=y>=3, so
A<=Ay_j/3, 1<=y_j/3, and sqrt(y)<=y<=y_j. Applying these inequalities
term by term in (5), with exactly D in (4), proves

    |mathcal E_(L_R)(u,v_j)| <= D y_j/t_j^2.                 (6)

All bounds are simultaneous in K_R, profiles and j.

### Weighted finite coefficient norm

Import finite complex Cauchy--Schwarz/bilinear duality as in
Montgomery--Vaughan, *Multiplicative Number Theory II: Primes and
Sieves*, author-hosted draft retrieved 11 November 2026,
Theorem G.1 and proof, printed pp.398-399
(https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf).
It applies to arbitrary finite complex coefficient vectors; the weights
y_j are strictly positive. First-slot linearity in (2) gives

    mathcal E(u,g)=sum_j conj(c_j)mathcal E(u,v_j).

Apply the imported inequality to sqrt(y_j)c_j and
mathcal E(u,v_j)/sqrt(y_j). By (6),

    |mathcal E(u,g)| <= sqrt(S)
              (sum_j |mathcal E(u,v_j)|^2/y_j)^(1/2)
       <= D sqrt(S) (sum_j y_j/t_j^4)^(1/2).                (7)

No division by S is made, so c=0 is included. Write b=log2.
Finite positive sums are bounded by the elementary geometric majorant

    sum_(j<J) y_j/t_j^4
       = R^-4 sum_(j<J) (y+jb)16^-j
       <= R^-4 [(16/15)y+(16/225)b]
       <= R^-4 y [16/15+16b/675].                          (8)

Indeed sum_(j>=0)r^j=1/(1-r) and sum_(j>=0)jr^j=r/(1-r)^2
at r=1/16 give the two displayed constants. These are scalar
majorants of finite sums, not a claim about infinite form synthesis.
The last inequality uses y>=3. Substituting (8) in (7) proves (3)
with (4), without J, largest-frequency or support factors.

### Conditional absorption in the original energy

C744p(1) gives E_(L_R)(g)>=S/8 for every R>=R_*(M,chi), uniformly
in every finite family. This already pays its high/high interactions,
whole correction and complete arithmetic operator. Put e=E_(L_R)(u),
a real number whose sign is unspecified. Hermitian polarization gives

    E_(L_R)(a u+g)=e|a|^2+2Re(a mathcal E_(L_R)(u,g))+E_(L_R)(g)
       >=e|a|^2-2eps|a|sqrt(S)+S/8.                         (9)

Completing the scalar square in (9) yields the first claimed bound.
Alternatively 0<=(4eps|a|-sqrt(S)/4)^2 gives
2eps|a|sqrt(S)<=16eps^2|a|^2+S/16, proving the second.
If the independently paid e satisfies e>=32eps^2, then
e-16eps^2>=e/2, giving the stated quantitative lower bound.
All constants in (4) are positive, so this condition has e>0.
If e>8eps^2, the completed square gives strict positivity when a!=0;
when a=0 and c!=0, S>0 supplies strict positivity directly.
No orthogonality of u and the carriers, bounded operator on their
infinite span, or positivity of a shifted norm was assumed. This is
the elementary scalar specialization of positive-block absorption;
the e margin is a hypothesis, never inferred from factorization.

The rate required by the approved test is attained. The independent
low-energy margin, non-neutral directions and a general all-window
assembly remain unresolved. One direction is not the entire low
subspace. L742's summability, L745's general-sign scope and L750's
specified corrected-IMS stops remain intact; they are contrasts, not
premises. No complete RH argument, counterexample or novelty claim
follows from this local specialization.

### Separate conceptual audit (11 November 2026, step510)

**Verdict and imports.** The claims pass at their full stated scope.
This is a REPRODUCTION under the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-11-collective-low-dyadic-audit-508.md`.
The cited Fourier, digamma, prime-power and finite complex duality
results above are reused as imports. C744o's passing arbitrary-window
estimates and C744p's passing high-block floor are used within their
hypotheses; their proofs are not being audited again. No new source
theorem, numerical evidence or independent low sign is asserted.

**Common domain, window and exact moments.** Since log log R>=log3=2ell,
K_R>=2, and flooring gives L_R<=log log R. For each finite K_R and J,
all the cell trains, their modulations, corrections and finite complex
combinations are smooth and compactly supported in (0,L_R). L744's
smooth-domain argument therefore applies without a uniform bound on
the generator-domain norm. The unit norm and H2 bounds on u and w_j
are exactly those required by C744o with M1=M. Crucially, its proof
of (8)-(11) holds at arbitrary finite K before K(t) is selected.
Use K=K_R and T=t_j there; no equality K_R=K(t_j) is needed.

For each cell k, the local moment vector of f_j=exp(it_j x)w_j
is d_(j,k). The local moment vector of h_j is G(G^-1 d_(j,k)),
with no conjugation. Thus both local moments of v_j vanish exactly.
Together with (1), finite cell summation gives F_u(+-i/2)=0 and
F_(v_j)(+-i/2)=0, including the weights exp(+-k ell/2).
The two pole products in C744o(4) consequently vanish for the actual
corrected pair. Their disappearance is exact, not an estimate of the
large weights or a deletion of intermediate uncorrected pole terms.

**All four costs and the constant D.** With H in (4), the four
remaining contributions are bounded by

    |Q_m(u,f_j)| <= 4M0 M[A+log(2+T/2)]/T^2,
    |Q_m(u,h_j)| <= (A+3)M0 H/T^2,
    |<B_(L_R)u,f_j>| <= C_prime(L_R)4M0 M/T^2,
    |<B_(L_R)u,h_j>| <= C_prime(L_R)H/T^2.

The last line uses ||u||_2=1, not an unproved small norm of B_(L_R).
C744n's correction bound is independent of K_R because it sums
squared cell H2 norms. C744o(11) bounds the entire nonnegative
prime-power mass, including both delay directions, by

    C_prime(L_R) <= 4c_RS exp(L_R/2) <= 4c_RS sqrt(y).

The strict cutoff n<exp(L_R) is covered by its inclusive upper bound;
a delay at L_R is zero. Adding the four estimates gives precisely (5).
This checks the whole correction in the arithmetic as well as the
Fourier term and introduces no profile, window or family-size factor.

All constants used for the next comparison are nonnegative, A>0,
and T>=R>=e^3>4. Hence log(2+T/2)<=log T=y_j, y_j>=y>=3,
A<=Ay_j/3, and sqrt(y)<=y<=y_j. The three terms of (5)'s numerator
are respectively at most

    4M0 M(1+A/3)y_j,
    (A+3)M0 H y_j/3,
    4c_RS(4M0 M+H)y_j.

Their sum is exactly D y_j with D as displayed, proving (6) with
one constant for every admitted varying family.

**Complex coefficients and finite summation.** The form (2) is
Hermitian and first-slot-linear, so its second slot is conjugate-linear:
mathcal E(u,g)=sum_j overline(c_j)mathcal E(u,v_j). Finite complex
Cauchy--Schwarz with weights y_j>0 gives (7). No real-coefficient
restriction, division by S, or orthogonality of profiles is used.
Since t_j^4=16^j R^4 and y_j=y+j log2, the two positive scalar
geometric sums have exact values

    sum_(j>=0)16^-j=16/15,
    sum_(j>=0)j16^-j=16/225.

They majorize each finite sum in (8). Dividing its second constant
by y>=3 gives 16log2/675, so its square root is exactly the factor
in C. The infinite sums here are scalar numerical majorants only;
no infinite vector, energy limit or interchange with the form occurs.
Consequently (3) is uniform in R,J and every allowed profile choice,
including c=0. J is a positive finite integer; an empty admitted
profile class makes the universal assertion vacuous, not an existence
claim. There is no largest-frequency cost.

**Original-energy absorption and the separate onset.** The hypotheses
R>=e^3 remain in force; absorption additionally requires R>=R_*(M,chi)
from C744p, rather than extending its floor to all R>=e^3. Hermitian
first-slot linearity gives the mixed term 2Re(a mathcal E(u,g)),
so (3) and E(g)>=S/8 give exactly (9), with the original real e=E(u).
Writing x=|a| and z=sqrt(S), its lower quadratic obeys the identities
and inequalities

    e x^2-2eps x z+z^2/8
      = (z-8eps x)^2/8+(e-8eps^2)x^2,
    0 <= (4eps x-z/4)^2
      =16eps^2 x^2-2eps x z+z^2/16.

These verify both claimed lower bounds with constants 8 and 16.
The sufficient margin e>=32eps^2 makes e-16eps^2>=e/2. Since C>0
and finite R gives eps>0, that margin also gives e>0; together with
y_j>0 it proves strict positivity for every nonzero coefficient pair.
Alternatively e>8eps^2 makes the exact square expression positive
when a!=0, while a=0 and c!=0 is paid by S/8. The zero coefficient
pair has zero energy. No strict positivity is asserted at equality
e=8eps^2; the first bound still implies nonnegative energy there.
Potential dependence of u on the v_j is not an extra premise: under
either sufficient margin, positivity itself excludes a nonzero
coefficient pair synthesizing the zero function. No L2 orthogonality
or converse block-positivity theorem was used.

**Scope and dependency check.** The conclusion is a validated
conditional interface, not proof that its independent margin holds.
One low direction is not a low subspace, and finite synthesis gives
no density, non-neutral coverage or all-window sign. The recorded
L742/L745/L750 and generic-joint-energy stops remain intact. The
common-window application uses the same imported estimates and
high-block floor as the original proof; the DAG therefore needs no
new edge. Full matching Mathlib coverage remains unchecked. This
audit validates a previously
unaudited local input without claiming progress beyond the imported
standard tools or a complete RH argument.

## Mathlib

Full matching coverage of this complete energy, correction, common
window and conditional estimate has not been checked. Finite complex
Cauchy--Schwarz and geometric sums are supporting standard results;
the cited Fourier/arithmetic inputs are imported as specified above.
No absence claim or formal verification is made.
