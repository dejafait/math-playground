# Lemma 874: exact actual-theta finite-contact flux, with an unpaid sign

## Hypotheses

Use the exact kernel K of L019 and the family of L058,

    F(lambda,z) = integral_0^infinity exp(lambda u^2) K(u) cos(zu) du.

For real lambda, put g_lambda(z)=F(lambda,z)/F(lambda,0). Define the
local logarithmic coefficients by

    log g_lambda(z) = -sum_(k>=1) S_k(lambda) z^(2k)/k,
    H_d(lambda) = (S_(i+j+2)(lambda))_(0<=i,j<=d).

The logarithm is the germ with value zero at z=0. Let d>=0 be finite,
lambda_*>0, and c be a fixed nonzero real vector of length d+1. Assume
H_d(lambda_*) is positive semidefinite and H_d(lambda_*)c=0. No
positivity at another degree or parameter is assumed. All unlabelled
coefficients and expectations below are evaluated at lambda_*.

Set r=max{i:c_i!=0}, N=2r+2, and

    b_n = sum_(i+j=n-2) c_i c_j,             2<=n<=N,
    A = 2N(2N+1)c_r^2 > 0.

Indices i,j in this sum lie between 0 and d. Empty sums are zero.

## Conclusion

The S_k are locally real analytic and obey the exact finite recurrence

    S_k' = -2k(2k+1)S_(k+1)
           +4k sum_(a=1)^k S_a S_(k+1-a).                 (1)

At the stated contact, Phi=c^T H_d' c is

    Phi = -A S_(N+1) + B,                                 (2)
    B = -2 sum_(n=2)^(N-1) n(2n+1)b_n S_(n+1)
        +4 sum_(n=2)^N n b_n
                    sum_(a=2)^(n-1) S_a S_(n+1-a).

Thus the requested sign Phi<=0 is exactly the still-unproved bound

    S_(N+1) >= B/A.                                       (3)

B involves only S_2,...,S_N. If r=d, S_(N+1)=S_(2d+3) is outside
H_d, whose last coefficient is S_(2d+2); its nonzero coefficient in
(2) has not been eliminated by the null equations. If r<d, S_(N+1)
is inside H_d: the extra equations of the larger matrix are retained,
and no assertion of an unpaid *external* coefficient is made in that
case. Formula (2) holds in both cases.

There is also an exact expression using the actual theta probability
density

    dmu_lambda(u) = exp(lambda u^2) K(u) du / F(lambda,0).

For n>=1 define the real polynomial

    T_n(u) = [z^(2n)] cos(zu)/g_lambda(z),
    R_(lambda,c)(u) = -sum_(n=2)^N n b_n T_n(u).

At the contact, with E denoting expectation under mu_(lambda_*),

    E R = 0,       E[u R'(u)] = 0,
    Phi = E[u^2 R(u)]
        = -E[u (log K)'(u) R(u)]/(2lambda_*).             (4)

The polynomial R has degree 2N=4r+4 and leading coefficient
-N c_r^2/(2N)!<0. It takes both signs on (0,infinity), so the displayed
integrand u^2 R cannot be signed pointwise using K>0. The alternative
score pairing in (4) is exact, but the required inequality
E[u(log K)'R]>=0, equivalent to Phi<=0, has not been proved either.

For the scalar specialization d=0,c=1, write m_j=E[u^j]. A contact
means m_4=3m_2^2, and

    Phi = -20S_3 = -(m_6-15m_2^3)/12.                     (5)

The required lower bound is m_6>=15m_2^3. Cauchy--Schwarz supplies
only m_6>=9m_2^3 under that contact equality. This compares an available
bound with the required one; it neither establishes a scalar contact
for actual theta nor gives an actual-family counterexample.

At lambda=0 the S_k agree with L025's reciprocal-zero power sums,
by its normalized local logarithm. No deformed zero sum is used here.
These identities do not prove a contact sign, an invariant cone,
all-degree positivity, or RH.

## Proof

### Local analytic normalization and coefficient evolution

L058 gives joint entirety, F(lambda,0)>0 on the real parameter axis,
and F_lambda=-F_zz. Around any fixed real lambda, choose a small complex
parameter disk and a small z-disk where F(lambda,0) is nonzero and g
is sufficiently close to 1. The logarithm with log g(lambda,0)=0 is
then jointly holomorphic. Evenness and conjugation make its even
coefficients real for real lambda. Coefficient extraction, spatial
derivatives and parameter derivatives commute on smaller disks by
holomorphy and Cauchy's formula. No global logarithm is needed.

Writing ell=log g, evenness gives ell_z(lambda,0)=0. The normalization
at zero must be included when differentiating:

    ell_lambda = -ell_zz-ell_z^2+ell_zz(lambda,0).

Indeed F_zz/F=ell_zz+ell_z^2, and the derivative of log F(lambda,0)
is -F_zz(lambda,0)/F(lambda,0)=-ell_zz(lambda,0). Now

    ell_z  = -2 sum_(k>=1) S_k z^(2k-1),
    ell_zz = -2 sum_(k>=1) (2k-1)S_k z^(2k-2).

Equating the z^(2k) coefficients for k>=1 yields

    -S_k'/k = 2(2k+1)S_(k+1)
              -4 sum_(a=1)^k S_a S_(k+1-a),

which is (1). The final constant term in ell_lambda affects no positive
coefficient but is needed for a correctly normalized identity.

Logarithmic heat transformations are known tools: T. Tao, *Heat flow
and zeroes of polynomials*, 17 October 2017, equation (2) and Exercise 3,
https://terrytao.wordpress.com/2017/10/17/heat-flow-and-zeroes-of-polynomials/.
That source uses the opposite heat direction. The finite extraction
above is reproduced to fix L058's normalization and identify the exact
matrix contraction; it is not claimed as a new heat transformation.
The prior source comparison is the notebook assessment
`drafts/literature/2026-11-06-reciprocal-hankel-heat-contact.md`.

### Null-vector cancellation and the missing coefficient

Since c is held fixed, Phi=sum_(n=2)^N b_n S_n'. For n>=2, the two
end terms of the convolution in (1) are 2S_1 S_n. Their contribution
to Phi is 8S_1 sum_n n b_n S_n. Symmetry of H_d gives

    sum_n n b_n S_n
      = sum_(i,j) (i+j+2)c_i c_j S_(i+j+2)
      = 2 sum_i (i+1)c_i (H_dc)_i
      = 0.                                               (6)

Removing these terms and using b_N=c_r^2 proves (2). The remaining
convolution contains only S_2,...,S_(N-1). The first sum in B reaches
S_N and no further. All coefficients in H_d have index at most 2d+2,
which verifies the full-degree and lower-degree qualifications above.
Dividing by the strictly positive A gives (3).

The calculation uses H_dc=0; positive semidefiniteness locates the
intended boundary problem but has supplied no additional sign in this
argument. In particular, the nonzero top coefficient does not prove
that the actual-theta values are freely variable or that no closure
using more theta information exists.

### Exact theta response, its signs, and the score identity

Write g_lambda(z)^(-1)=sum_(j>=0) a_j z^(2j), a_0=1. Then

    T_n(u) = sum_(j=0)^n a_(n-j)(-1)^j u^(2j)/(2j)!.

These are finite polynomials. All their moments under mu_lambda are
finite by L058's compact domination. Taking expectations coefficient
by coefficient gives

    E T_n = [z^(2n)] g_lambda/g_lambda = 0       (n>=1).

Furthermore

    partial_lambda log g_lambda
      = E[u^2 cos(zu)]/g_lambda(z)-E[u^2].

Its positive coefficients give S_n'=-n E[u^2 T_n]. Therefore
Phi=E[u^2 R] and E R=0. This computation uses normalized moments,
including the derivative of the normalizing mass; no derivative of
the parameter-dependent polynomial R is being suppressed.

Using u partial_u cos(zu)=z partial_z cos(zu), with g fixed while
differentiating u, also gives

    E[u T_n'(u)]
      = [z^(2n)] z g_lambda'(z)/g_lambda(z) = -2S_n.

Consequently E[u R']=2 sum_n n b_n S_n=0 at contact by (6).

Only n=N contributes the leading coefficient of R. N is even, so it
is -N b_N/(2N)!=-N c_r^2/(2N)!. Hence R is strictly negative for
sufficiently large u. The density mu_lambda is strictly positive on
(0,infinity), and E R=0. If R were nonpositive everywhere there,
the negative tail would make its integral strictly negative. Thus R
is positive somewhere as well. Continuity gives intervals of both
signs at positive u; multiplication by u^2 preserves these signs.

For completeness the integration by parts below has no unpaid tail.
From L019, set v=pi n^2 exp(2u) and

    K_n(u)=4v(2v-3)exp(u/2-v),        K=sum_(n>=1) K_n.

Termwise differentiation is locally uniform, and

    K_n'(u) = [60pi^2 n^4 exp(9u/2)
               -30pi n^2 exp(5u/2)
               -16pi^3 n^6 exp(13u/2)] exp(-pi n^2 exp(2u)).

In particular, on u>=0,

    |K'(u)| <= C exp(13u/2-pi exp(2u)),
    C=(60pi^2+30pi+16pi^3)
                         sum_(n>=1) n^6 exp(-pi(n^2-1)) < infinity.

The same bound on finite sums justifies the asserted differentiation;
the summability follows, for example, by comparison with a geometric
series times n^6. Thus polynomial factors and exp(lambda u^2) remain
integrable against both K and |K'|. At infinity uR exp(lambda u^2)K
tends to zero; at zero its factor u makes the boundary term zero.
Integration by parts on [0,T], followed by this domination, yields

    0 = E[R+u R'+2lambda_* u^2 R+u(K'/K)R].

K>0 makes K'/K defined, and its pairing is absolutely integrable
because its product with the density contains K', not an uncontrolled
reciprocal. The first two expectations vanish at contact. Since
lambda_*>0, division gives (4). At lambda=0 this argument instead
gives only E[u(log K)'R]=0 at contact: division by lambda there is
not permitted, and no endpoint estimate has been proved.

The exact score, if needed for an independent theta estimate, is

    u(log K)'(u)
      = u sum_(n>=1) (K_n(u)/K(u))
                    [9/2+6/(2pi n^2 exp(2u)-3)
                         -2pi n^2 exp(2u)].

This follows by differentiating log K_n and then summing K_n'. It
gives a specific actual-theta quantity, not a sign for its pairing
with the sign-changing R. A future inequality must control that
signed pairing, including the finite null premises, independently.

### Low-degree arithmetic and the precise deficit

Expanding g=1-m_2 z^2/2+m_4 z^4/24-m_6 z^6/720+O(z^8) gives

    S_1=m_2/2,
    S_2=(3m_2^2-m_4)/12,
    S_3=(m_6-15m_2m_4+30m_2^3)/240.

For d=0,c=1, H_0=0 gives m_4=3m_2^2. Formula (1) with k=2 gives
S_2'=-20S_3+16S_1S_2=-20S_3, proving (5). Directly the response is

    R(u)=-(u^4-6m_2u^2+3m_2^2)/12.

This yields the same flux, checking the sign and normalization by
the independent moment expansion. Since the density has full positive
support, m_2>0. Cauchy--Schwarz applied to u and u^3 gives
m_4^2<=m_2m_6, hence m_6>=9m_2^3 at this hypothetical contact.
Its constant 9 is smaller than the required 15. Even the strict form
for a nondegenerate density supplies no quantitative improvement to
15. No actual contact or counterexample follows from this comparison.

As a second algebraic check, if d=1, S_2=a>0, S_3=b, S_4=b^2/a and
c=(-b/a,1), substitution into (1) gives

    Phi = -72S_5 + 64b^3/a^2 + 8ab.

It agrees with (2); it is only a conditional full-degree check, not an
assertion that such an actual theta parameter exists. Cases a=0 are
covered by (2), without division by a.

The zero-time identification is exactly L025's unique local logarithm
of Xi(z)/Xi(0), together with F(0,z)=Xi(z) from L058. All quantities
used at nonzero lambda were defined by local coefficients and finite
integrals. No claim about deformed product convergence, contact
existence, first-contact continuation, non-strict tangency, initialization
or control as d tends to infinity is part of this result.

### Bounded exact verification

Run `python3 scripts/heat/reciprocal_hankel_contact_algebra_20261106.py`.
The standard-library rational polynomial calculation independently
differentiates the normalized g coefficients and reconstructs log g
and 1/g. Its 22 exact checks cover (1), the mean, dilation and time
response identities for k=1,...,5, and the two low-degree contact
expansions above. All 22 residuals vanish, with no failures; the full
selected residual records and the 9-versus-15 bound comparison were
inspected in `scripts/heat/reciprocal-hankel-contact-algebra-20261106.json`.
These finite algebra checks support the normalization; they do not
replace the arbitrary-degree analytic proof or verify the theta sign.
No numerical or formal contact is presented as an actual theta contact.

### Independent finite-identity audit, 6 November 2026 (step 11)

The audit passes for the written finite hypotheses. This validates the
existing reduction, not its sign, and imports no additional signed
theorem. The logarithmic heat tool is reproduced for the normalization
already explained above. In particular:

1. L058's compact domination permits all the parameter and spatial
   derivatives used here. Positivity of F(lambda,0) at a real base point
   and continuity give a common complex polydisk on which g is close
   to 1. The normalized holomorphic logarithm exists there; evenness
   and conjugation follow by uniqueness of that germ. Its constant
   term is identically zero. The displayed ell_lambda has constant
   term -ell_zz(lambda,0)+ell_zz(lambda,0)=0, and coefficient
   extraction gives (1), including k=1 where the convolution has only
   one term. For every n used in Phi, n>=2, so its two endpoint terms
   really are distinct and give 8n S_1 S_n.
2. With c held fixed, the finite contraction is precisely
   sum_n b_n S_n'. Swapping i and j in its endpoint contribution gives
   (6), using only rows of H_dc=0. Since c_i=0 for i>r, b_N=c_r^2
   and b_n=0 for n>N. The remaining convolution has indices from 2
   through n-1, while the remaining linear sum reaches S_N. This
   verifies B, A>0 and the direction of (3). If r<d then
   N+1=2r+3<=2d+1; if r=d it equals 2d+3. The larger-matrix null
   hypotheses remain in force; this formula does not declare the
   top coefficient freely variable. PSD is a contact hypothesis,
   not an input to the algebraic cancellation.
3. Each T_n uses only the finite inverse coefficients a_0,...,a_n.
   Its mean and dilation identities can therefore be integrated as
   finite polynomial sums. Equivalently, extracting a coefficient
   under the cosine integral is justified on the same small disk by
   L058. The time-response identity differentiates log g before
   forming R; it never differentiates E R as if R were parameter
   independent. All moments involved are finite. The negative leading
   coefficient of R and the positive density on every open positive
   interval, together with E R=0, prove both asserted signs of R.
4. Direct differentiation verifies every coefficient in K_n' and the
   stated summand score. For u>=0, n^2,n^4<=n^6,
   exp(5u/2),exp(9u/2)<=exp(13u/2), and
   exp(-pi(n^2-1)exp(2u))<=exp(-pi(n^2-1)). These inequalities give
   the displayed summable bound for |K'| and uniform derivative
   convergence on compact intervals. For any polynomial P and fixed
   real lambda, both |P|exp(lambda u^2)K and
   |P|exp(lambda u^2)|K'| are integrable: the negative exp(2u)
   term dominates the quadratic and linear exponents and every
   polynomial. The same estimate makes uR exp(lambda u^2)K tend to
   zero at infinity; at zero R and K are finite and the explicit u
   factor kills the product. Thus every term in the integrated
   derivative is absolutely integrable. Cancellation of K in the
   score pairing is legitimate because K>0. Division requires
   lambda_*>0 as stated; the lambda=0 qualification is retained.
5. The scalar and degree-one substitutions agree with (1)-(2).
   Cauchy--Schwarz gives the available constant 9, not the required
   15. L025's zero-time interpretation uses its normalized germ and
   L058's F(0,z)=Xi(z); no positive-parameter zero product is needed.

The existing standard-library verification program was inspected and
replayed. All 22 exact residuals in the certificate's complete `checks`
array are empty; its full scalar comparison and summary were inspected.
This finite replay supports, and does not replace, the arbitrary-finite
analytic audit above. No mathematical error was found. Contact existence,
the signed estimate, equality/continuation, initialization, degree-uniform
control and the RH endpoint remain unproved. Full Mathlib coverage and
supporting specialized coverage remain unchecked as stated below.

## Mathlib

Full matching coverage is not checked; availability is unknown, not
asserted absent. No formal theorem for the contact sign is imported.
The proof uses local analytic coefficient extraction, finite polynomial
algebra, dominated integration by parts and Cauchy--Schwarz. Supporting
formal coverage of these specific specializations is also unchecked.
Reference: https://leanprover-community.github.io/mathlib4_docs/.
