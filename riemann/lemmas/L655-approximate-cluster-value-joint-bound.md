# Lemma 655: approximate values control a dense narrow pole cloud

## Hypotheses

Let n>=5, x=-d=-5/4, R=11/8, U=R^2, eta=1/100 and t_j=j/n
for 0<=j<n. The finite set Z consists of distinct points a with
Re(a)=x and |a|<=R-eta, and contains x. The original simple-pole
residues r_a are positive integers, M=sum_a r_a<=n/3 and N=|Z|.
The family is independent of |u|=1. No separation, symmetry or
coefficient-integrality assumption is made. Put

    B_u(z)=product_(j<n) R(z-t_j*u)/(U-t_j*z/u),
    b_u(zeta)=B_u(R*zeta),  W_a(u)=B_u(x)/B_u(a),
    L(z)=sum_a r_a/(z-a),  q_u(zeta)=sum_a r_a W_a(u)/(R*zeta-a).

Keep the conjugated denominator angle and every grid factor. F_u is
the complete analytic component specified by

    b_u q_u=B_u(x)L(R*zeta)-F_u.

Use normalized spatial and angular circle means and
<f,g>=mean f conjugate(g), linear in the first entry. Define

    D_u=sum_a r_a^2 |W_a(u)|^2/(U-|a|^2),
    D_single,n=mean_u D_u,
    D_(u,M)={P_+(b_u J s): deg s<M},
    J s=zeta^(-1)conjugate(s),
    J_n=mean_u ||Proj_(D_(u,M)) F_u||_2^2,
    sigma=sqrt(137/5000),
    delta=log(26/19)-(log 2)/3,  tau_n=(M/sigma)exp(-delta*n),
    f_u(z)=conjugate(B_u(x))/B_(conjugate(u))(2x-z).

For the approximate construction choose an integer 1<=m<=M and a
real h>=0 such that |a-x|<=h for all a and h<r=m/(8n). Let
H_(u,m) be the Taylor polynomial of f_u about x through degree m-1,
and s_(u,m)(zeta)=H_(u,m)(R*zeta). Set

    K_(n,m)=exp(m)*(21n/m)^m,
    E_(n,m,h)=exp(m+8nh)*(h/r)^m/(1-h/r),
    A_u=R^(-1)sum_a r_a |W_a(u)|^2.

All logarithms are natural; at h=0 the displayed E equals zero.
The choice of m imposes no derivative conditions at the actual poles.

## Conclusion

The complete norm and relative value errors satisfy, uniformly in u,

    ||s_(u,m)||_2 <= K_(n,m),
    |H_(u,m)(a)-conjugate(W_a(u))|
                      <= E_(n,m,h)*|W_a(u)|  for every a.       (1)

If E=E_(n,m,h)<=1, this yields the full joint lower certificate

    ||Proj_D F_u||_2
        >=max(0,(1-E)*A_u/K_(n,m)-tau_n).                      (2)

In particular, for every original admissible family satisfying

    n>=8192,             |a-x|<=1/16384 for every a,           (3)

there is no extra restriction on N or M, and

    ||Proj_D F_u||_2^2 >= (1/4)exp(-n/16)D_u,
    J_n >= (1/4)exp(-n/16)D_single,n.                         (4)

Thus arbitrarily many distinct poles, up to the original mass ceiling,
are covered in this fixed narrow interval. This includes shrinking
1/n clouds once they lie in (3), with no lower separation. The degree
used when M>=ceil(n/512) is ceil(n/512)-1, regardless of N. For
smaller M, L654 supplies (4).

This is a geometric partial result for the approved joint target.
Families spread outside (3), including multiple separated dense
clouds, remain unresolved. No replacement of cross-cluster terms by
their diagonal is proved. Xi realization, matching detector upper
bounds, all-degree signs and inherited audits remain independent.
This result is separately unaudited, not certified originality or an
RH candidate.

## Proof

### 1. Source scope and complete response

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-joint-full-grid-polynomial-dual.md`.
It covers the finite polynomial/Fourier/residue test of this same
joint space. The scoped comparison checked C645y's complete component,
L649--L654's relevant definitions and proofs, the local cluster/Taylor
passages and the recorded angular screen failure. L652's repeated-jet
cost and L654's distinct-count cost do not supply (1): here the degree
is chosen to allow an error in values. L647's constant grouping stop
is a contrast, not a premise. No novelty is inferred from this search.

Import the Hardy projection convention from L. Baratchart, S. Chevillard
and T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47, preprint v2,
24 March 2015, [Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Fourier orthogonality and Parseval are A. Levitt, *Analyse de Fourier
et applications*, version retrieved 2 November 2026,
[Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12,
printed pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
The residue theorem and simple-pole rule underlying L650's response
are R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition,
front matter updated 22 August 2025,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
These primary inputs were inspected in the reused assessment chain;
there is no new source retrieval or independent source audit here.
No general approximation theorem is assumed or reproved. The
grid-specific Taylor error and full-circle norm need the calculation
below; the cited facts alone do not evaluate their rate.

All B_u(a) are nonzero: |a|>=d>t_j and U>t_j|a|. Also f_u(x)=1,
and 2x-a=conjugate(a) gives f_u(a)=conjugate(W_a(u)). Its possible
finite poles are 2x-t_j*conjugate(u), whose distances from x exceed
1/4. Thus its Taylor series at x converges absolutely and uniformly
on every closed disk of radius less than 1/4. This also follows by
expanding each of its finitely many rational factors geometrically.

For any polynomial s of degree <M put e=P_-(b_u J s) and
v=P_+(b_u J s). L650's complete polynomial response and L651's
Gram/correction estimate give

    <F_u,v>=B_u(x)<L(R*zeta),e>
                  -R^(-1)sum_a r_a W_a(u)s(a/R),
    ||v||<=||s||,
    |B_u(x)<L(R*zeta),e>|<=tau_n||s||.                         (5)

L651 also gives delta>1/16, D_u>=64/21, and a positive lower Gram
bound for every nonzero such s. These facts retain the entire
negative-part correction, not just the residue pairing. No grid
prefix or independently normalized pole column is used.

### 2. Relative Taylor error and whole-circle norm

Write w=z-x. The exact rational product is

    f_u(x+w)=product_(j<n)
      [1+t_j*u*w/(U-t_j*u*x)]/[1-w/(x-t_j*conjugate(u))].      (6)

Here |t_j/(U-t_j*u*x)|<2 and |1/(x-t_j*conjugate(u))|<4,
since U-d=41/64>1/2 and d-t_j>1/4. For 0<=v<=1/16, (6) gives

    |f_u(x+w)|<=[(1+2v)/(1-4v)]^n<=exp(8nv)  (|w|<=v),
    |f_u(x+w)|>=[(1-2v)/(1+4v)]^n>=exp(-8nv) (|w|<=v).     (7)

For the first exponential comparison,
log(1+2v)<=2v and -log(1-4v)<=4v/(1-4v)<=16v/3.
For the second,
log(1-2v)>=-2v/(1-2v)>=-16v/7 and log(1+4v)<=4v.
The resulting coefficients are 22/3<8 and 44/7<8.
These scalar inequalities follow by integrating 1/(1+t) or
1/(1-t); no logarithm branch of f_u is needed.

Because m<=n/3, r=m/(8n)<=1/24<1/16. Write
f_u(x+w)=sum_(k>=0) a_k(u)w^k. Fourier orthogonality on |w|=r,
applied to its uniformly convergent series, yields

    a_k r^k=mean_theta f_u(x+r exp(i theta)) exp(-ik theta),
    |a_k|<=exp(m)r^(-k).                                    (8)

Summing the complete geometric tail for |a-x|<=h<r gives

    |f_u(a)-H_(u,m)(a)|<=exp(m)(h/r)^m/(1-h/r).

By (7), |f_u(a)|>=exp(-8nh), proving the relative error in (1).
The tail includes every omitted coefficient; it is not a finite
numerical preview.

For |zeta|=1, |R*zeta-x|<=R+d=21/8. Put Q=(R+d)/r=21n/m>=63.
Using (8) on every retained coefficient gives

    |H_(u,m)(R*zeta)|<=exp(m)sum_(k<m)Q^k
                         <=exp(m)Q^m=K_(n,m).                (9)

The normalized L2 norm is at most this supremum. This bounds the
polynomial on the whole spatial circle, far beyond the small Taylor
disk; no convergence of the infinite Taylor series there is used.
Only its finite polynomial is evaluated on that circle.

Let P_u=R^(-1)sum_a r_a W_a(u)H_(u,m)(a). The relative errors give

    |P_u-A_u|<=R^(-1)sum_a r_a |W_a|
                    |H_(u,m)(a)-conjugate(W_a)|<=E*A_u.      (10)

The original positive residues justify this weighted sum. Thus
|P_u|>=(1-E)A_u when E<=1. Since H_(u,m)(x)=1, s_(u,m) and its
joint image are nonzero. Apply (5), Cauchy--Schwarz against the
projection, and (9) to obtain (2). All phases are retained until
the proved error estimate (10); no positivity of individual complex
cross terms has been assumed.

### 3. Degree choice for a dense narrow cloud

Assume (3) and first M>=m=ceil(n/512). Use h=1/16384. Then

    16<=m,  n/512<=m<=17n/8192,
    h/r=n/(2048m)<=1/4,  8nh<=m/4.                          (11)

Consequently

    E<= (4/3)exp(-(log 4-5/4)m)<=(4/3)exp(-m/8)<1/4.         (12)

For exact constants, integrate
2/(1-t^2)>2(1+t^2) from 0 to 1/3 to get
log 2>56/81>11/16, hence log 4>11/8. Also
exp(2)>1+2+2+8/6=19/3>16/3. Together with m>=16 these prove (12).

Since 21n/m<=10752 and log 10752<10,

    log K=m[1+log(21n/m)]<11m
                    <=187n/8192<3n/128.                    (13)

One exact witness for the logarithm bound is exp(1)>8/3 and
2^21=2097152>21*3^10=1240029. Thus
exp(10)>(8/3)^10>21*512=10752. No fitted exponent is being used.

The original squared-residue diagonal obeys

    D_u<=sigma^(-2)sum_a r_a^2 |W_a|^2
        <=(MR/sigma^2)A_u,
    D_u>=64/21.                                            (14)

Here U-|a|^2>=sigma^2 and r_a<=M; no unit-residue substitution is
made. From (12)--(14) and M<=n/3,

    (1-E)A_u/K >= [6sigma^2/(MR sqrt(21)K)]sqrt(D_u)
                 >= [1/(16n)]exp(-3n/128)sqrt(D_u).          (15)

Indeed 18sigma^2/(R sqrt(21))>18sigma^2/(15/2)
=1233/18750>1/16, using R<3/2 and sqrt(21)<5.

For n>=8192, exp(n/128)>=(n/128)^4/24>=16n, since the last
comparison reduces to n^3>=384*128^4 and its ratio at n=8192
is 16/3. Therefore (15) is at least exp(-n/32)sqrt(D_u).
The complete correction is small enough at the same onset:

    tau_n/[exp(-n/32)sqrt(D_u)]
      <=sqrt(21)/(24sigma)*n*exp(-(delta-1/32)n)
      <2n exp(-n/32)<=393216/n^2<=3/512<1/2.                 (16)

Here delta>1/16, sqrt(21)/(24sigma)<2 follows from
21<2304sigma^2, and exp(v)>=v^3/6 gives the penultimate bound.
Thus (2) proves the pointwise assertion (4) for M>=ceil(n/512).

If M<ceil(n/512), its integrality gives
N<=M<=ceil(n/512)-1<n/512<n/384. L654 (5), with its full
correction and original diagonal, proves exactly (4) in this case.
This use of L654 is why its hypotheses and unaudited status remain
part of the present result; the Taylor construction is not claimed
to have degree <M when M is smaller than the chosen m.

For each fixed finite family, all weights and Taylor coefficients
depend continuously on u. L651's Gram bound makes the joint
projection continuous as well. The pointwise bound (4) can therefore
be integrated in normalized angular measure, giving the stated J_n
bound. There is no limiting pole coalescence or interchange of an
infinite tail with an angular mean in this step.

### 4. What the test settles

Unlike exact interpolation at N nodes, (8)--(12) spend a chosen degree
and tolerate relative value error. This removes any further N ceiling
on the narrow-cloud family (3), including N=M=floor(n/3) distinct
unit-residue poles. It neither replaces those poles by a repeated
anchor nor prescribes the unused higher Taylor jets.

The geometric restriction is essential to this estimate. With the
same degree, h>=r makes its geometric remainder bound unavailable;
even h approaching r produces an excessive error in (1). This is
a limit of the certificate, not an admissible obstruction to the
joint projection. Applying separate polynomials to separated clouds
would require controlling their cross-cloud values and full combined
norm; adding their individual lower bounds is not justified.

Exact scalar checks for (7), (11)--(16) are reproduced by
`python3 scripts/one-sided-hankel/approximate-cluster-constants.py`,
with the full certificate at
`scripts/one-sided-hankel/approximate-cluster-constants.json`.
They check arithmetic witnesses, not analytic hypotheses or the
open spread-family comparison. The argument above supplies the
uniformity; neither this proof nor its inherited inputs has received
a separate critical audit in this turn.

## Mathlib

Full matching coverage for this grid-specific approximate value
certificate and dense narrow-cloud joint bound has not been checked.
Supporting residue, Fourier/Parseval and projection facts are the
precise named imports above. Unknown coverage is not evidence of
absence. No formal theorem asserting the unrestricted joint bound
or actual-Xi positivity is assumed.
