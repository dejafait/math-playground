# Retained native cusp label — bounded attempt

Step 204 works only on the pre-existing SPECIALIZE target in
`drafts/literature/2026-10-14-retained-native-cusp-label.md`.
Main gap: original finite B>=A and actual input/action/pilot/essentiality.
Intermediate target: identify L053's Q with L057's c(1) up to sign.
Possible use: one retained-place cusp-marking prerequisite; compatible
splitting and full selected/theta data remain independent.

Inputs are the fixed maps and objects of L053,L056,L057, with L055
and their inherited L051,L045,L048,L054 hypotheses. Preserve unchanged
N, the pointed Tate isomorphism and changed r=q_0, v_3(r)=30.
The ready source review and ATTEMPTS/027,030 were checked. There is no
local duplicate of the marked-map conclusion and no cross-notebook input.

Initial reasoning was saved before the coordinate test. Completed
bounded reasoning follows; no new canonical input is adopted.

Continuation test: a neighboring section and one-step map over unchanged
N, with orientation ambiguity only. An arbitrary unit label fails.
An essential general input outside the assessment requires withholding
the conclusion and a REVIEW_REQUIRED continuation. No theta splitting,
full native type or numerical inequality is inferred.

## Actual-map reduction

Let tau_t denote the standard coordinate Tate uniformization at t,
and s_i L056's canonical sections of D=T_7(r), with s_0 the origin.
The fixed pointed isomorphism gives h_N(P)=tau_r(beta). L056's
algebraic equality gamma alpha=kappa^(-1)a_N h_N thus reduces this
attempt to the following sufficient identities for the ACTUAL maps:

    a_N(tau_r(beta)) = tau_(r^7)(r),
    kappa(s_epsilon,N) = tau_(r^7)(r),  epsilon in {1,-1}.

If both hold, injectivity of kappa gives gamma(Q)=s_epsilon,N.
L057's native one-index deck map lifts its actual component map over k.
L056's rotation lifts the same map with one of the two orientations.
The cited proper-henselian full faithfulness identifies their actual
lifts with rotation or its inverse. Applying them to the origin would
give c(1)=Q or -Q. The displayed identities are unproved sufficient
conditions, not premises. This reduction does not allow an arbitrary
unit relabeling modulo seven or use Phi as an analytic map.

## Subsidiary coordinate checks

These calculations are retained inside the unfinished attempt, not
introduced as downstream lemma inputs. The representative beta belongs
to unchanged N: for sigma in G_N, N-rationality of P, Galois equivariance
and the exact Tate kernel imply sigma(beta)/beta=r^m, m an integer.
Its seventh power is 1 since beta^7=r is fixed. Thus r^(7m)=1;
positive valuation forces m=0. Algebraic beta is fixed by G_N, hence
lies in N. This checks the kernel ambiguity before inferring a fixed
representative from a fixed class.

Use Kedlaya's equations (4)–(5) and rewritten series, pp.2–3, only
at the two retained pairs (u,t)=(beta,r) and (r,r^7). Write
v=v_3,a=v(u),b=v(t) for each of these pairs.

The index-zero terms are u/(1-u)^2 and u^2/(1-u)^3. Their errors
from u and u^2 have valuations at least 2a and 3a. Positive-index
summands have valuations nb+a and 2(nb+a), respectively. Rewrite
negative indices using w=t^n/u, n>=1: their summands are
w/(1-w)^2 and -w/(1-w)^3, of valuation nb-a. The constant series
s_1(t)=sum_(n>=1) n t^n/(1-t^n) has valuation at least b, including
all integer multiples in X,Y. The tails converge because nb-a tends
to infinity. The respective error bounds are min(2a,b-a) and
min(3a,b-a) for these pairs, on the COMPLETE series; no finite
truncation stands in for the infinite remainder.

At (u,t)=(beta,r), (a,b)=(30/7,30), this gives

    v(X(beta,r)-beta)>=60/7, v(Y(beta,r)-beta^2)>=90/7,
    v(X(beta,r))=30/7, v(Y(beta,r))=60/7.

At (u,t)=(r,r^7), (a,b)=(30,210), it gives

    v(X(r,r^7)-r)>=60, v(Y(r,r^7)-r^2)>=90,
    v(X(r,r^7))=30, v(Y(r,r^7))=60.

These are valuations of the named coordinate points. They do not
compute a_N(tau_r(beta)) or kappa(s_1). The expected valuation layer
does not verify either actual-map identity or a component label.

## Unfinished bridge and decision

Narrowly reinspected already-assessed primary inputs for this proof
attempt, without a new discovery search:
[Conrad, July 18, 2006 author version](https://math.stanford.edu/~conrad/papers/kmpaper.pdf),
section 2.5, printed pp.17–18, (2.5.1)–(2.5.3), Example 2.5.1 and
Theorem 2.5.2 with proof; and
[Kedlaya, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
Theorem 1, equations (4)–(5), rewritten series and proof discussion
pp.2–4. Retain the source notes' version and odd-level qualifications.

Conrad's power map is X_i -> X_i^7,Y_i -> Y_i^7 in FORMAL ANNULUS
coordinates. Kedlaya's X(u,t),Y(u,t) are Weierstrass coordinates.
They cannot be identified by notation. Theorem 2.5.2 fixes kappa at
the formal group of the origin and uses contraction in its proof;
the inspected statement does not compute this nonidentity section in
Kedlaya's coordinates. Kedlaya's point theorem does not itself give
the map from Conrad's component-indexed annuli. I did not complete
that same-object comparison. This is not a claim that it is false,
impossible or absent from the literature. Origin normalization may
determine an actual algebraic map without computing its value here.

The shortcut would assert both sufficient identities directly from
point-group powers and origin normalization. That would silently
upgrade Phi and conflate the two coordinate systems. It is not used.
Ambiguous PDF text extraction of adjacent overlaps is not a verified
gluing formula; the requested screenshot yielded no inspectable image.
No conclusion rests on that extraction.

Outcome: EXPLORATION, REPRODUCTION. No native label, counterexample,
new lemma or mathematical input beyond the sources checked results.
The prior ready assessment still authorizes this completed attempt.
A precise essential coordinate bridge is now REVIEW_REQUIRED, rather
than reopening the graph audit or exact-curve globalization stop.
Full matching Mathlib coverage remains not checked. PROOF and DAG
remain unchanged because the assembled argument has not changed.
