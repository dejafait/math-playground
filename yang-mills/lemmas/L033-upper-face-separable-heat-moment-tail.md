# L033 — Separable weights and an explicit upper-face spectral tail

## Hypotheses

Keep L008's box, relative normalized one-form modes, exact cutoff rho,
two potentials and tau=1/16. Keep L030's formal Q_i(t), N_2, and L032's
pure-sector decomposition. For alpha=A,B let Q_i^alpha be the degree-zero
probe operator and N^alpha the degree-one residual operator. Write

\[
 I_{i,M}=8\sum_{\alpha=A,B}\sum_{\substack{k\in Z,\ell\text{ relative}\\
                         k_j,\ell_j\le M\ (j=1,2,3,4)}}
 \frac{e^{-\tau(\lambda_k+\lambda_\ell)}}{\lambda_k^2\lambda_\ell}
 (Q_i^\alpha)_{k\ell}(N^\alpha)_{k\ell}.
\]

The second index includes every one-form component and every admissible
frequency, including its allowed zero frequency. N is symmetric by its
defining composition, as justified in L031. No signs of matrix entries
or sums are assumed. Let c=9/1024, and define nonnegative heat moments

\[
 S_p=\sum_{n=0}^\infty n^p e^{-cn^2},\qquad
 T_p(M)=\sum_{n=M+1}^\infty n^p e^{-cn^2},\quad p=0,10,
\]

with 0^0=1 in S_0.

## Conclusion

Both infinite pure-sector sums satisfy the explicit bound

\[
 |I_i-I_{i,M}|\le C_i\,7^4
 \{7T_{10}(M)S_0^6+42S_{10}T_0(M)S_0^5\},             \tag{1}
\]

where C_3=11,584,512 and C_6=46,338,048. All omitted modes are covered;
no transition coefficients, second-index components or inverse weights
are dropped from I_i or I_{i,M}. Only their absolute tail estimate uses
a lower spectral-gap bound and ignores parity restrictions.

Exact rational evaluation of the estimates below gives, at M=112,

\[
 |I_3-I_{3,112}|\le 1.37381915696\,10^{-11},\qquad
 |I_6-I_{6,112}|\le 5.49527662781\,10^{-11}.             \tag{2}
\]

The inverse weights also have the exact separated representation

\[
 F_i(\alpha,\alpha)=8\int_\tau^\infty (s-\tau)\,ds
 \int_\tau^\infty dr\sum_{k\in Z,\ell}
 (Q_i^\alpha)_{k\ell}(N^\alpha)_{k\ell}
 e^{-s\lambda_k-r\lambda_\ell}.                        \tag{3}
\]

Its inner sum factors term by term into four one-dimensional sums
after the finite weak differential expansion described below. This
identity does not specify or certify a numerical integration rule.

Neither I_{i,112} nor its coefficient integrals have been evaluated
with an enclosure here. Thus (2) gives no sign of I_i. The cutoff-12
values in the preceding working record cannot be substituted for
I_{i,112}. No bound for other action classes, compensation, the complete
Ward coefficient, its logarithm, the reflected error <= c_box/2 or a
Yang–Mills mass gap follows.

## Proof

### 1. Weak monomials and bounds independent of bump derivatives

Each potential is a tensor product Psi=prod_j h_j(x_j), with h_j=x_j rho
in its two named directions and h_j=rho in the other directions. Its
L^1 norm is at most 9^2 6^2=2916, since 0<=rho<=1 and its support is
[-3,3]. Expand L030(5)–(8) only to the indicated formal degrees.
Each weak matrix entry is a finite sum of monomials

\[
 v\int_D (\partial^d\Psi)
                 (\partial^a f_{k,\beta})(\partial^b f_{\ell,\gamma})\,dx.       \tag{4}
\]

Here a,b,d are derivative multiindices, and beta,gamma are component
labels. No component summation is implicit in a single monomial.
Q has total derivative
degree |d|+|a|+|b|=4, and N has degree 6. These degrees count derivatives
on the coefficient as well as on the arguments. In the action term
use <L f,K h>; move the outer E_nu correction from K to L f by
integration by parts. Symmetrizing this weak form exchanges its two
arguments and halves their coefficients. This preserves the degree
and does not increase the absolute coefficient sum used next.

Define the weighted absolute coefficient sum of a weak expansion by
Omega=sum |v| 2^{|d|}, across all argument components. It suffices to
use the following conservative bounds, separately for either potential:

\[
 \Omega(Q_3)\le192,\quad\Omega(Q_6)\le768,
 \quad\Omega(N)\le6704/3.                              \tag{5}
\]

Here is an explicit count verifying them without relying on a numerical
expansion. For a fixed component u has at most one term, with coefficient
magnitude 1 and coefficient derivative degree 1; u^(2) has magnitude
1/6 and degree 3. Thus their weighted sums are at most 2 and 4/3.
The weighted sums of w, s, w^(2), s^(2) in one component or pair are
at most 4, 8, 16/3, 32/3 respectively. A curl has absolute coefficient
sum 2. Its degree-one incidence correction has sum 1/12; including
both clover averages increases this to 7/12. For a fixed output
component L=d* d has coefficient sum at most 8, and its degree-one
correction has sum at most 2/3. These bounds include terms which cancel
or vanish, so equality is not required.

For Q_3 there are six planes, two possible diagonal weights, and two
curl factors, giving 6*8*4=192. For Q_6 there are six pairs and four
curvature indices, with weighted shear sum 8 and curl product sum 4;
the two polarizations with factor 1/2 give 6*4*8*4=768.

In the degree-one action weak form <L f,K h>, there are at most
four output components times two nonzero velocity components.
The four corrections have weighted sums at most

\[
 (4/3)\,8\,2=64/3,\quad
 2\,(8/8)\,2=4,\quad
 2\,8\,(7/12)=28/3,\quad
 2\,(2/3)\,2=8/3.
\]

They correspond to u^(2), E^(2), C^(2)d+d^(2), and L^(2).
Their sum times eight is 896/3. Symmetrizing does not increase it.
For the degree-one triplet, its corrected weight has weighted sum at
most 2*(16/3)+2*(8/2)=56/3: the second term retains both coefficient
plane averages. Thus its full corrected sum is at most
6*((56/3)*4+2*8*(1/12)*2)=464.
For the degree-one shear the corresponding bound is
6*4*((32/3)*4+2*8*(7/12)*2)=1472.
Subtracting both corrected probes from the action therefore gives
896/3+464+1472=6704/3. This verifies (5).

For a mode pair set R^2=sum_j(k_j^2+ell_j^2); k_1=0 leaves seven free
indices. A positive-frequency one-dimensional normalized sine or
cosine has two complex exponential coefficients of magnitude 1/4,
whose absolute sum is 1/2. A zero-frequency normalized cosine has
magnitude 1/sqrt(8)<=1/2. Move partial^d in (4) off Psi. Compact support
eliminates all boundary terms. The product-rule/exponential expansion
bounds its derivative multiplier in direction j by
(omega(k_j+ell_j))^{d_j}, where omega=pi/8<1/2. The argument derivative
multipliers are (omega k_j)^{a_j} and (omega ell_j)^{b_j}. Using
k_j,ell_j<=R and k_j+ell_j<=2R therefore gives, for total degree h,

\[
 |(\text{operator})_{k\ell}|
 \le (2916/256)\,2^{-h}R^h\Omega(\text{operator}).       \tag{6}
\]

This estimate involves only Psi's L^1 bound, rather than derivatives of
rho. It includes constant factors and zero argument derivatives with
the usual convention 0^0=1; a positive derivative of a constant vanishes.

### 2. Include the entire omitted spectrum

Every relative one-form mode has three positive sine indices. Thus
lambda_k,lambda_ell>=3 pi^2/64>27/64 and
tau(lambda_k+lambda_ell)>cR^2. Apply (6) to Q and N, use the lower gap
only for the denominator, and sum their component-specific coefficient
bounds. The inequality sum_gamma Omega(Q_gamma)Omega(N_gamma)
<=Omega(Q)Omega(N) permits extending all component domains to the same
nonnegative seven-index set without multiplying by an extra component
count. The two potentials together give

\[
 |\text{summand contributions at a seven-index vector}|
 \le 16(2916/256)^2 2^{-10}(64/27)^3
             \Omega(Q_i)\Omega(N) R^{10}e^{-cR^2}
 =27\Omega(Q_i)\Omega(N) R^{10}e^{-cR^2}.
\]

Inserting (5) yields precisely C_3 and C_6. Enlarging the allowed
frequency sets and disregarding parity only adds nonnegative majorants.
Write the seven indices as n_1,...,n_7. Convexity of x^5 gives
(sum_j n_j^2)^5<=7^4 sum_j n_j^{10}. For the omitted cube use
1_{max n_j>M}<=sum_j 1_{n_j>M}. Summing the products of the seven
one-dimensional heat factors gives seven equal-index terms
T_10(M) S_0^6 and forty-two unequal-index terms S_10 T_0(M) S_0^5.
This proves (1). In particular the bound tends to zero and covers the
full omitted signed sum, rather than a sampled set of modes.

### 3. Exact rational evaluation of the heat moments

For rational x>=0 and integer J>=0 define
H_J(x)=(sum_{j=0}^J x^j/j!)^{-1}. The exponential power series with
nonnegative terms proves e^{-x}<=H_J(x). For m=M+1 set

\[
 r_p=((m+1)/m)^p H_J(c(2m+1)).
\]

If r_p<1, the ratio of successive n^p e^{-cn^2} terms for n>=m is
at most r_p: both (1+1/n)^p and e^{-c(2n+1)} decrease with n.
Consequently

\[
 T_p(M)\le m^p H_J(cm^2)/(1-r_p).                       \tag{7}
\]

For a chosen B with a valid ratio, also
S_p<=sum_{n=0}^B n^p H_J(cn^2)+T_p(B). Every operation in these bounds
is rational. Replacing each intermediate value by a larger terminating
decimal preserves the inequality; these outward replacements avoid
excessive rational denominator growth.

The reproduction command is

```sh
python3 scripts/combined-ward-response/check_continuum_heat_tail.py
```

The complete certificate is
`scripts/combined-ward-response/continuum-heat-tail-certificate.json`.
With B=J=160 the certified moment upper bounds are
S_0<=9.95308720484 and S_10<=5.32283164890*10^12.
At M=112 they are T_0<=2.10711391688*10^-49 and
T_10<=7.25796325172*10^-29. The outward ratio bounds are respectively
0.135997716001 and 0.148523677252, both below one. Substituting these
rational decimals in (1) and rounding outward gives (2).

The independent finite symbolic expansion in the existing continuum
program has weighted sums 64,192,2072/3 and the expected degrees 4,4,6
for both potentials. The certificate checks these against (5). This is
a consistency check; the conservative mathematical counts above prove
the constants independently of that program. At cutoff 12 the direct
p=10 geometric ratio is not below one, so this particular evaluation
of (7) fails there and is recorded in the certificate. At M=64 the
two tail bounds exceed 10^19; the useful small bounds require much
larger cutoffs. No failed threshold is concealed as a sign certificate.

### 4. Exact separation of the inverse weights

Elementary integration gives integral_tau^infinity (s-tau)e^{-s lambda}
ds=e^{-tau lambda}/lambda^2 and integral_tau^infinity e^{-r lambda}dr
=e^{-tau lambda}/lambda for lambda>0. Absolute convergence from L032
justifies exchanging these integrals with the complete signed sum,
since integrating the absolute majorant recovers its convergent
weighted series. This proves (3).

In a weak monomial, the coefficient, mode factors and integration box
are products over the four coordinates. Thus its matrix element has
the form v prod_j A_j(k_j,ell_j). A pair of monomials from Q and N
has product vw prod_j A_j(k_j,ell_j)B_j(k_j,ell_j). The exponential
weight also factors over the coordinates, and the admissible mode
domains for a fixed component are product sets, with k_1 fixed at zero.
Each inner sum is therefore a product of four one-dimensional sums.
Finite monomial expansions and Gaussian majorants justify these
factorizations. They retain the unrestricted second-index component
sum. Numerical use still requires certified coefficient integrals,
one-dimensional spectral truncation and the two integration tails.

The general flow and matching sources in the saved SPECIALIZE review
remain cited within their prior scopes. None supplies the present
stencil-specific tail bound or evaluates its signed functional. This
is a local bound, not certified originality beyond the checked sources.

## Mathlib

Coverage of the full bound and residual specialization: not checked.
Supporting exponential integrals, convexity, finite products and
absolutely convergent sum/integral exchanges: not checked. The exact
rational script is not a Mathlib formalization and certifies no sign
or interacting estimate.
