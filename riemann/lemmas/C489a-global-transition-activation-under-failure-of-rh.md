# Corollary 489a: failure of RH activates the finite-collision reduction

## Hypotheses

Use the actual theta heat family F of L058 and the Xi conventions of
L018. Accept the global de Bruijn–Newman threshold theorem and the
unconditional Polymath upper bound, precisely cited below, together with
L488/L489 and their retained source qualifications. Assume RH is false.
This last premise is conditional and has not been established.

## Conclusion

There is a real parameter lambda_* with

    0<lambda_*<=11/200<1/8

such that all zeros of F(lambda_*,.) are real. For every fixed pair
0<a<lambda_*<b<=1/8 there is a real x_* satisfying

    0<|x_*|<R(a),       R(a)=(1/2)exp(C_*/(4a)),
    F(lambda_*,x_*)=F_z(lambda_*,x_*)=0.

Here C_*>0 is L488's absolute existential constant. The exact multiplicity
of x_* is a finite integer at least two. The chosen x_* may depend on
a,b; no effective numerical cutoff or uniform bound as a decreases to
zero is claimed. All-real slices occur to the right of lambda_*, and
nonreal zeros occur at every real time below lambda_*.

This is a known-theorem application, not a new collision mechanism or a
proof of RH. It supplies no actual off-line zero and excludes no collision.

## Proof

### Precise imported statements

C. M. Newman, *Fourier Transforms with Only Real Zeros*, Proceedings of
the AMS **61** (1976), 245–251, Theorem 3, p.247,
[DOI](https://doi.org/10.1090/S0002-9939-1976-0434982-5), supplies the
finite transition theorem. Use its exact modern primary restatement in
D. H. J. Polymath, *Effective approximation of heat flow evolution of the
Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences **6** (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2),
introduction, paragraph after (4): there is a finite real Lambda such
that all zeros of H_t are real if and only if t>=Lambda. This is a
closed-threshold statement for every real t. Theorem 1.1 of the same
version states unconditionally that Lambda<=0.22=11/50.

These are accepted by precise citation. The original theorem proofs and
Polymath's numerical verifications are not independently audited here.
The modern restatement is used rather than unreliable inequality glyphs
in the extracted Newman scan, whose Gaussian-sign convention differs.
No conditional improvement or infinite RH verification is imported.

### Exact local application

L488 establishes, in precisely these conventions,

    F(lambda,z)=8 H_(4lambda)(2z).

The nonzero factor and the real invertible spatial scaling preserve
reality and multiplicity of all zeros in both directions. Therefore
all zeros of F(lambda,.) are real if and only if 4lambda>=Lambda.
By L058, F(0,z)=Xi(z), and L018 identifies all-real Xi zeros with RH.
Failure of RH thus implies that H_0 has a nonreal zero. The threshold
statement at t=0 forces 0<Lambda. Define lambda_*=Lambda/4; the cited
upper bound gives 0<lambda_*<=11/200<1/8.

Fix arbitrary 0<a<lambda_*<b<=1/8. Put epsilon=b-lambda_*>0.
For every lambda_*<lambda<=lambda_*+epsilon=b, one has
4lambda>Lambda, so every zero is real. This is exactly L489's first
hypothesis, and the whole chosen right interval is contained in [a,b].
For integers j>=1 define

    lambda_j=lambda_*-(lambda_*-a)/(j+1).

These are strictly increasing real numbers in (a,lambda_*), tending
to lambda_*. Since 4lambda_j<Lambda, the threshold equivalence says
that not all zeros of H_(4lambda_j) are real: a nonreal zero exists.
The scaling gives a nonreal zero of F(lambda_j,.) for every j.
This is L489's second hypothesis, with all its incoming times in [a,b].
No simplicity or endpoint-reality assumption was used.

Apply L489 with this same compact positive-time interval. It gives
endpoint reality and a real multiple zero with |x_*|<R(a), of finite
multiplicity at least two. Its strict bound includes the exclusion of
the equality edges via L488's real/simple tail; it is not a strict
inequality passed through a limit. L058 gives F(lambda_*,0)>0, so x_*
is nonzero. Nonzero entirety, finite multiplicity and the strip/cutoff
qualifications are exactly those retained in L489. This proves the
conclusion. The threshold also gives the asserted all-real and nonreal
sides at every real time, without a compact-time restriction. ∎

### Qualifications and verification

Both transition quantifiers are discharged conditionally on failure of
RH and the cited inputs. Verification consists of the explicit time
scaling, the bound 11/200<1/8, the right interval and increasing incoming
sequence above; no numerical experiment is evidence for these steps.
L488's underlying asymptotic and strip proofs, and the imported global
threshold and upper-bound proofs/certificates, remain unaudited. Its
local replay and L489's compactness implication have separate audits;
this application passed its separate critical audit on 2026-10-30,
conditional on those inputs, with no proof correction required.
Finite positive-time collision exclusion, zero-time control and actual-Xi
all-degree positivity remain open. In particular a finite collision
under failure of RH is not a contradiction.

### Separate critical application audit — 2026-10-30

This audit accepts the precise global statements cited above and the
qualified local inputs L018/L058/L488/L489. It checks their application,
not their source proofs or numerical certificates. No stronger
conditional Polymath bound or theorem about the sign of Lambda is used.

The identity F(lambda,z)=8 H_(4lambda)(2z) in L488 comes from the
absolutely convergent defining integrals. Its identity scope includes
every real lambda, even though L488's tail conclusion has a restricted
positive-time range. Thus the time-threshold equivalence transfers for
every real lambda. Spatial scaling is a bijection of C preserving the
real axis in both directions. At every order k the derivative scales
by 8*2^k, a nonzero factor, so multiplicities agree as well.

L018 and F(0,z)=Xi(z) give a nonreal F(0,.) zero under failure of RH.
Equivalently H_0 does not have all its zeros real. The closed
biconditional at source time zero therefore implies 0<Lambda; it does
not merely imply Lambda>=0. Dividing the finite threshold and its
unconditional bound by four gives

    0<lambda_*=Lambda/4<=11/200<25/200=1/8.

In particular lambda_* is in L489's open allowed range, and admissible
pairs 0<a<lambda_*<b<=1/8 exist. The conclusion quantifies over every
such fixed pair, rather than claiming a single effective choice of a.

For any such pair, epsilon=b-lambda_*>0 gives the entire required
right interval (lambda_*,lambda_*+epsilon]=(lambda_*,b] inside [a,b].
At every time in that interval, 4lambda>Lambda and the threshold gives
all-real zeros. Write d=lambda_*-a>0 for the incoming sequence. For
every integer j>=1,

    lambda_j-a=d*j/(j+1)>0,
    lambda_*-lambda_j=d/(j+1)>0,
    lambda_(j+1)-lambda_j=d/((j+1)(j+2))>0.

Also d/(j+1) tends to zero. Thus all sequence terms, not just an
eventual subsequence, lie in (a,lambda_*) and increase to lambda_*.
At each term, 4lambda_j<Lambda. Negating the all-real property supplies
a nonreal zero; it requires neither an additional zero-existence
assumption nor a global enumeration. The spatial substitution transfers
that zero to F(lambda_j,.). These are exactly L489's two hypotheses
on the same compact positive-time interval.

L489 now supplies endpoint reality and a finite-multiplicity real zero
of order at least two with |x_*|<R(a). The strict spatial conclusion
uses L488 at the endpoint: equality would imply simplicity, contradicting
that multiplicity. No strict inequality is passed through a limit.
L058 gives F(lambda_*,0)>0, so x_* cannot be zero and the endpoint
slice is nonzero. There is no extra simplicity, effective-cutoff,
infinite-height verification or uniform a->0 premise. The global
all-real/nonreal sides follow from the same threshold for all real
times; only the compact collision conclusion uses [a,b].

Verdict: the local application passes without a missing hypothesis or
proof correction. This independently validates a known-theorem
specialization; it adds no result beyond the accepted source inputs.
Finite collision exclusion and control as a decreases to zero remain
unproved, as do actual-Xi all-degree signs. The conditional collision
is neither a contradiction nor a rigorous off-line-zero certificate.

## Mathlib

Full matching coverage has not been checked; absence is not asserted.
No declaration is claimed for the global threshold or the numerical
upper bound. The application uses elementary order/sequence facts after
the cited analytic inputs. See the
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
