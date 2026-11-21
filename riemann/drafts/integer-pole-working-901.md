# Fixed integer-pole attempt901 — working checkpoint

The gate-approved target is exactly assessment899's fixed law, with
contact window 0<x<=16. No rates or window will be tuned. Main gap:
L030-L032/C032a actual-Xi positivity; model success would only exclude
integer multiplicity as a sufficient extra scalar barrier premise.

Source imports: Sra arXiv2611.02944v1 Lemma C.17 proof (C.49),
pp38-39 for the finite positive inverse; Kwasnicki arXiv1710.11023v3
Section6.1 p20 for the geometric smoother; Steutel--van Harn V.2.11,
V.2.16 (2.23), III.10.4 for the same-law scalar identity after its
kernel checks. Reuse assessment899 completion900; no new source gap.

Preliminary algebra, not yet a full contact certificate:
f(x)=2exp(-x)-2exp(-3x)cos(x)-4exp(-3x)sin(x), x>0;
p=f*g_1. Its canonical kernel is
H(t)=exp(-t)+2exp(-3t)cos(t)+sum_(n>=1)exp(-2^n t).
On 0<t<=1 the first three displayed trigonometric terms of H and
-H' are positive. For t>=1 use 2sqrt(10)exp(-2t)<1,
since exp(2)>7>2sqrt(10), to dominate the oscillatory derivative;
the same bound dominates the oscillatory term of H. Integral H=13/5.

The finite inverse and g_1 give smoothness, flatness and positivity
after checking convolution regularity; all poles have integer order.
D2 and the full D3 prefix/simple contact are still unproved.
Planned bounded check: evaluate this law by its distinct-pole partial
fractions, first diagnostically, then with complete interval/tail
control if feasible. A sampled sign is never the contact certificate.
The C466d endpoint composition argument was read for its applicability
pattern; its gamma-specific estimates are not imported.

Diagnostic finite-product script contact-diagnostic-901.py (floating,
not proof) suggests the first D3 change between 177/32 and 178/32.
Later floating signs near x=14 are cancellation noise and are unused.
A possible exact endpoint join uses the finite inverse f itself:
D3(f;x)=1000exp(-7x), and
D2(f;x)=20exp(-4x)[exp(-2x)-cos(x)+2sin(x)]. The bracket and
its first derivative vanish at zero; on [0,1/4] its second derivative
is 4exp(-2x)+cos(x)-2sin(x)>=3/2. Thus the strict finite-head
signs are available for the C466d composition argument with q=g_1.
These identities and the composition hypotheses still need final review.

Proposed rigorous compact method: finite product N=128, with rational
partial fractions, compared to the true law by convolving its remaining
positive real exponential tail. Put all derivatives on f convolved
with the first six real exponentials. Its finite partial fractions bound
the global Lipschitz constants; the omitted tail has mean 2^(-128).
This gives uniform errors for derivatives through order5. Outward
integer intervals can then check the compact prefix and contact bracket.

Stop this law if a required premise is rigorously false. An unpaid
endpoint join/enclosure is inconclusive. No actual-Xi transfer,
strict actual forcing, simultaneous-contact barrier or propagation
has been supplied. No complete RH candidate exists.

## Completion901

The complete proof and final constants are canonical in C466e. The
natural-interval evaluator was interrupted after excessive endpoint
refinement, without a completed certificate, and is preserved under
scripts/integer-pole/contact-natural-interval-incomplete-901.py.
The final evaluator uses p8 for derivatives through order eight and
Taylor enclosures of the determinant functions through a third-derivative
remainder. It passed all 189 cells; the complete ledger check also passed.
This supersedes the preliminary p6 plan above. The original fixed law
and window are unchanged. Independent conceptual/arithmetic audit is
pending; the next assessment is a REVIEW_REQUIRED nomination only.
