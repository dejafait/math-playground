# C212a — The complete quadratic gauge-jet term is subcubic

## Hypotheses

Use exactly L212's SU(2) hypotheses: the relative box (-4,4)^4,
admitted even meshes a=8/N, the straight lower-rooted direction-1
forest, the complete L008 displacement, both actual L010 probes
i=3,6 at tau=1/16, and the bare expansion at fixed mesh before
refinement. Coordinates and adjoints are ordinary full variable-link
coordinates. Retain every normal end edge and physical boundary row.
Vertex potentials vanish on all physical boundary vertices. Constants
may depend on the fixed data and probe, but not on sufficiently fine N.

Keep L212's co-closed covariance S, projection P, residual A=PAP,
complete quadratic probe B_i=PB_iP, r=sum_c (z^c)^T A z^c,
t=2SAz and M=2SAS. The three colors of z are independent with
covariance S; S may be singular in the ambient link space. Both
insertion subtractions remain in A. With the actual pinned prefix
Phi and endpoint-sum map q, put

    H=I-D Phi/2, V=q Phi, b=[Hz,Vz]/2.

This b is exactly L212(2), not a new or independently sampled
quadratic field. For X,Y in {H,V}, define
C_XY=XSY^T and K_XY=XMY^T. Keep L184's first-placement convention
Q_(1,i,N), including its coefficient 3 in L184(6).

## Conclusion

The response of the entire quadratic gauge-jet term in L212(4) is

    K^(bb)_(i,N):=Cov_S(<b,B_i b>,r)=Q_(1,i,N)/2,       (1)

and consequently, for both actual probes,

    |K^(bb)_(i,N)|<=C_i N^(5/2),
    a^3 |K^(bb)_(i,N)|<=C_i' N^(-1/2) -> 0.           (2)

In particular set

    U_i(z)=F_(i,4)(z)+dF_(i,3)(z)[b(z)]
                              +2<B_i z,c(z)>,        (3)

where the complete co-closed flow jets and full cubic endpoint field
c are those of L212. Then its original target response satisfies

    K_(i,a)=Cov_S(U_i,r)+O(N^(5/2)).                   (4)

Thus K_(i,a) and Cov_S(U_i,r) have the same a^3-scaled limit if
either exists. This removes only <b,B_i b> at that scale. No bound
or convergence for the remaining joint expression (3) is proved.
In particular the two nested zero-time flow integrals, correlated
prefix corrections and their upper jumps remain. No separate-term
limit, complete compensation, finer asymptotic, finite matching,
interacting reflected estimate <=c_box/2, continuum axioms or
infrared finite positive mass follows. This is a specialization of
existing local Wick and prefix estimates, not progress beyond the
sources checked or an originality claim.

## Proof

### 1. Differentiate the entire quadratic gauge-jet polynomial

L212(12)'s single-polynomial Gaussian identity gives

    K^(bb)_(i,N)=(1/2)E[d<b,B_i b>[t]]
               =E[<B_i b,db[t]>].                    (5)

The second equality uses B_i=B_i^T. The derivative db[t] is L212(7):
both Phi z and z vary, and Phi t retains every pinned endpoint.
With W=P db[t], B_i P=B_i implies

    2 E[<B_i W,b>]=2 K^(bb)_(i,N).                    (6)

The left side is exactly the contribution differentiating the B_i z
leg of J=2<B_i z,b> in direction W, hence L184's first placement.
No differentiation of W is involved. This proves (1); the following
independent covariance-minor calculation checks its normalization.

### 2. Check all four signed minors by a quadratic Gaussian tilt

The SU(2) bracket is minus the cross product. For each fixed output
color c, Isserlis' fourth-moment formula applied to
b_e^c=-(1/2)sum_(d,f) epsilon_(cdf)(Hz^d)_e(Vz^f)_e
has no within-b pairing: it would require d=f. The two crossing
pairings give opposite color signs. Summing all three output colors
therefore gives the exact identity

    E[<b,B_i b>]=(3/2)sum_(e,g) (B_i)_(eg)
        [(C_HH)_(eg)(C_VV)_(eg)
                          -(C_HV)_(eg)(C_VH)_(eg)].   (7)

Indeed sum_(c,d,f) epsilon_(cdf)^2=6; its factor 1/4 is from
the two factors b. Exchanging d,f changes the color sign for
the other crossing. The formula uses the original correlated H,V
within each color; independence is only between different colors.

At this fixed mesh, apply the normalized quadratic tilt exp(lambda r)
on im P. For all sufficiently small real lambda it is integrable,
and its one-color covariance has derivative M=2SAS at lambda=0.
To justify this also in singular ambient coordinates, write
z=S^(1/2)xi on the support of S. There the tilted standard Gaussian
has covariance (I-2lambda S^(1/2)AS^(1/2))^(-1), positive for
|2lambda| ||S^(1/2)AS^(1/2)||<1. Its derivative, after lifting,
is M. The same lambda neighborhood gives polynomial Gaussian
domination, so differentiating (7) is legitimate. The derivative
of its normalized left side is precisely Cov(<b,B_i b>,r),
without an assumption that either mean vanishes.

Hold B_i,H,V and Phi fixed as deterministic maps in this tilt.
Differentiating both covariance factors in each product in (7)
gives

    K^(bb)_(i,N)=(3/2)sum_(e,g)(B_i)_(eg) {
        (K_HH)_(eg)(C_VV)_(eg)
       -(K_HV)_(eg)(C_VH)_(eg)
       -(K_VH)_(eg)(C_HV)_(eg)
       +(K_VV)_(eg)(C_HH)_(eg)}.                     (8)

Compare directly with L184(6): (8) is Q_1/2, not Q_1 and not
the full Q_1+Q_2+Q_3. Both the directional calculation (5) and
the tilted expectation (7) give this same factor. Differentiating
the covariance of the fixed polynomial in (7) retains the effects
of both moving prefixes in (5); it does not freeze a random prefix.

### 3. Reuse the established full-boundary estimate

Equation (8) matches L186(1) with exactly half its coefficient and
the same S,M,A,B_i,H,V. All its hypotheses apply: the forest is
unchanged, B_i is the actual complete quadratic probe, and the
signed M retains both insertion subtractions. L186(2) therefore
gives (2) directly; no new prefix estimate is required.

For clarity, the imported bound uses max_(e,g)|B_(eg)|<=C_i a^6,
||S^(1/2)AS^(1/2)||<=CN,
||HSH^T||_HS<=CN^(7/2) and ||VSV^T||_HS<=CN^4.
Each of the four products in (8) is bounded by
2||S^(1/2)AS^(1/2)|| ||HSH^T||_HS ||VSV^T||_HS
after entrywise Cauchy--Schwarz, as proved in L186(11)--(13).
The total exponent is -6+1+7/2+4=5/2. The differentiated
prefix estimate in that proof includes the upper pinned rank-one
correction; neither an end row nor a constant own-direction mode
has been removed. M is controlled as a signed matrix, not as a
positive covariance. No smooth-input consistency is assigned to
its rough slots. Full external heat sums remain in B_i.

Finally L212(4),(9) give K_(i,a)=Cov_S(U_i+<b,B_i b>,r).
Covariance is linear, so (1)--(2) prove (4). Multiplying its error
by a^3=8^3/N^3 proves the stated equivalence of cubic-scale limits.
The achieved bound is strictly below O(N^3) for this complete term;
it is not a bound on (3) or a use of final-time smoothing at an
internal flow endpoint. L022 and ATTEMPTS/010's failed isolated
curvature transfer are not invoked. The earlier prefix failures
in ATTEMPTS/039--045 remain unchanged.

## Mathlib

Full matching result: **not checked**. Supporting coverage of
Isserlis' formula, normalized quadratic Gaussian tilts and singular
Gaussian linear images: **not checked**; unknown availability is
not absence. The standard named input is Isserlis' fourth-moment
formula, specialized explicitly in (7). The Gaussian tilt identity
is already established in L212, and the needed uniform estimate is
imported from L186, rather than reproved. The unchanged
[coverage assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
approves this complete quartic response test; it imports no theorem
for a limit of the selected bare forest cumulant.
