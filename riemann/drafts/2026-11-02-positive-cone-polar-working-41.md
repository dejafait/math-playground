# Positive-cone real-polar test — step 41

The supplied startup files and unchanged EXPLORE assessment
`drafts/literature/2026-11-02-displaced-positive-cone-distance.md`
cover this single mathematical attempt on the exact rate-1/100 cone
distance. Existing changes and unfinished work are preserved.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
a Laurent polynomial p with frequencies -2n through 2n such that
ell(f)=Re mean(conj(p) f) has ell(1)=1, ell(W_a)>=0 at all
nonanchor L666 nodes, and ||p||_2<=exp(n/100)*n^C with absolute
C/onset uniformly in the displacement vector. Cauchy--Schwarz would
then give the approved cone bound. The b_a=1 application, full-spatial
Jensen/H step, general support, Xi realization and signs remain separate.
Continue on this uniform bound or a quantified obstruction; a finite
optimization is only exploratory. Failure parks only this ansatz.

Inputs inspected: L666's exact rational factorization and hypotheses;
L672's explicit complex coefficients and nonsingularity argument;
L673's exact positive construction and rate qualification; C673a's
recorded contour stop. Their proofs are not re-audited here. The
continued-value functional at u=0 has the pre-existing exponential
cost obstruction in C645p and is not a new mechanism. The scalar/Gram
stops and original unit residues remain intact. No favorable spectrum,
cross-term positivity or mass cap is assumed.

## Work saved before the bounded test

The chosen test concerns the real Hilbert inner product. Its sign is
ell(W_a)>=0, because the affine cone is 1+sum b_a W_a with b_a>=0.
No general projection theorem needs reproof. A numerical dual must
retain every Fourier component of its candidate p, and exact positivity
would require either analytic actions or rigorous error bounds. The
degree-2n cutoff is an ansatz, not a property of the original cone.

The complete products have both interior common poles and exterior
node-dependent poles. Consequently a plain Hardy evaluation or an
exponential replacement is not justified. The next calculation will
first determine whether the finite Laurent polar problem has a
credible sign/norm profile before any claimed uniform construction.

## Completed bounded calculation: EXPLORATION, not a lemma

Use normalized measure and the real inner product Re mean(conj(f)*g).
If a Laurent polynomial p has the stated exact actions, then for every
b_a>=0, ell(1+sum b_a W_a)>=1 and Cauchy--Schwarz gives a lower
norm bound 1/||p||_2. Fourier orthogonality gives the exact continuous
norm squared sum_(|k|<=2n)|p_k|^2. In the computation this last sum is
evaluated in floating arithmetic; no sampled norm of p replaces it.

The qualitative projection input is Moreau (1965), Proposition 4.a and
Corollary 4.b, pp.278--281, as inspected in the unchanged assessment:
[original paper](https://www.numdam.org/article/BSMF_1965__93__273_0.pdf).
Only its underlying real-Hilbert convention and polar orientation are
used. It supplies no quantitative norm or conditioning estimate here.
For exact Fourier columns V_a=Pi_(2n)W_a, an exact conic minimizer
r=1+sum b_a V_a would satisfy Re<r,V_a>>=0 and
b_a Re<r,V_a>=0. Thus Re<r,1>=||r||^2 and, when r!=0,
p=r/||r||^2 would be the desired finite-degree polar. These are
conditional specialized identities, not a claim that the numerical
solver has supplied an exact minimizer or certified any such signs.
The standard Cauchy--Schwarz and finite Fourier orthogonality inputs
do not decide the family-specific norm. No new general cone theorem
or full matching Mathlib theorem is claimed; coverage was not checked.

The script is `scripts/one-sided-hankel/positive-cone-polar-screen.py`.
It retains every rational-product factor, including j=0 and U*u-t_j*x.
It tested q=4,8,16,32 (n=51,99,195,387) for two vectors at each q:
dyadic 2^(-24) approximations to L673's phase-aligned displacements,
and independently chosen multiples of 1/64 in [-1/8,1/8] with the
recorded deterministic seed. The former are admissible dyadic vectors;
L673's exact coefficient signs are NOT asserted for their roundings.
The stored ordinates and evaluated products have floating errors.
All original residues are still one; all optimized b are auxiliary.

### Exact-sample alias bound and its limited scope

The mathematical Fourier extraction uses the standard Laurent form of
Cauchy's coefficient estimate on 4/5<=|u|<=6/5. All common interior
poles have modulus <80/121<4/5; all exterior poles have modulus >5/4.
Also 5/4<=|a|<4/3. With d=5/4 define the rational bound

    B_n(r)=product_(1<=j<n)
       [(d+t_j*r)/(d-t_j*r)]
       *[(U*r+(4/3)*t_j)/(U*r-d*t_j)],   r in {4/5,6/5}.

Every denominator is positive. Triangle inequalities applied separately
to L666's exact product give |W_a(u)|<=B_n(r) on |u|=r; the
j=0 prefactor has modulus at most one. Cauchy's formula bounds
positive coefficients by B_n(6/5)*(5/6)^k, and coefficient -k by
B_n(4/5)*(4/5)^k, for k>=0 in the respective estimates. These
geometric bounds justify the absolutely convergent alias identity for
exact Nth-root samples. For every retained |k|<=2n<N their total
omitted aliases are at most

    A_n,N=B_n(4/5)*(4/5)^(N-2n)/(1-(4/5)^N)
           +B_n(6/5)*(5/6)^(N-2n)/(1-(5/6)^N).

The script uses the first power of two N>=16n+1024. Exact Fraction
calculations give upper bounds 10^(-114), 10^(-230), 10^(-463),
10^(-279) respectively at the four tested n; all beat the chosen
10^(-30) threshold. Full numerators and denominators are in the
per-case `positive-cone-polar-repair-screen-n*-*-alias.txt` files.
These bounds are uniform in allowed e for each tested n, but enclose
ONLY the exact-sample alias error. They do not enclose libm values,
floating products, the FFT, linear algebra or coefficients of p.
No rounding-certified action follows. This standard estimate is
included to specify the computational method, not promoted as a new
mathematical input toward the main gap.

### Strict-action repair and complete finite observations

The unrepaired candidates had negative computed actions in all eight
cases. At n=387 for the phase vector, the most negative was about
-3.07e-10. Those signs were not silently accepted within a tolerance.
The new repair solves, numerically, for v with Re(v_0)=0 and
Re<v,V_a/sigma_a>=1, where sigma_a=||V_a||_2 is computed from all
retained Fourier coefficients. With epsilon at least 1e-8 and large
enough to dominate the computed negative normalized actions, it sets
p_repaired=p+epsilon*v. Complete base and repaired Laurent vectors,
all actions, b, scales, ranks and singular values are retained in
`scripts/one-sided-hankel/positive-cone-polar-repair-screen.json`.
The earlier unrepaired screen is separately preserved. Its failure
records refer to the base candidates; no exact sign certificate exists
for either set of candidates.

The following are floating observations only:

| n | phase repaired norm | independent repaired norm | exact-sample alias upper bound |
|---|---:|---:|---:|
| 51 | 1.479219 | 1.448713 | 10^(-114) |
| 99 | 1.506775 | 1.390246 | 10^(-230) |
| 195 | 1.647110 | 1.328224 | 10^(-463) |
| 387 | 3.100108 | 1.362985 | 10^(-279) |

All repaired computed normalized actions are positive, with minimum
about 9.9397e-9, and Re(p_repaired,0)=1. Every displayed norm is below
exp(n/100) at its finite n. That observation does not control any
absolute-C/onset asymptotic assertion. No solver rank truncation or
iteration cap was reported. However the phase-vector correction at
n=387 has computed norm about 3.0392e6 and normalized action residual
about 1.766e-9 before multiplication by epsilon. Its large cost is a
real issue to bound, not a favorable spectral hypothesis. The full
128-entry repaired normalized action vector and diagnostics at that n
were inspected; the certificate reader was also used for the complete
failure list. None of these floating quantities is rigorous evidence
for a uniform cone margin, a countersequence, or an exact finite sign.

Reproduce the final diagnostic from the notebook directory with

    OPENBLAS_NUM_THREADS=1 python3 scripts/one-sided-hankel/positive-cone-polar-screen.py --q 4 8 16 32 --patterns phase independent --output scripts/one-sided-hankel/positive-cone-polar-repair-screen.json

## Decision and outstanding work

The result is EXPLORATION. The bounded finite test found a numerically
positive strict-action repair but no proof of the required uniform
norm. It neither establishes nor refutes rate 1/100. No lemma, DAG
edge or main-argument change is justified. Prior results L672/L673
and the qualified C673a contour barrier remain unchanged.

One analytic continuation is justified inside the same assessed cone
target: replace the computed strict-action repair by a formula or
proved quantitative interpolation estimate, paying both the base polar
and correction norms. In exact notation a candidate pair must satisfy
Re(p_0)_0=1, Re(v_0)=0, Re<p_0,W_a>>=-epsilon*sigma_a,
Re<v,W_a>>=sigma_a, and
||p_0||+epsilon||v||<=exp(n/100)*n^C, with all inequalities uniform
in n and every displacement. Here sigma_a must be defined and
controlled exactly (for example ||Pi_(2n)W_a||_2 with positivity
proved); its sampled value cannot be assumed. This sufficient
intermediate test still leaves construction of p_0, interpolation
conditioning, exact signs and all uniform bounds unresolved.
Continue only on such estimates or a quantified obstruction to this
repair mechanism. Another finite q/mesh expansion would not discharge
those obligations. The b_a=1 and Jensen/H application, support, Xi
realization and actual mixed signs remain independent gaps.
