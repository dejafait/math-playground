# Combined origin audit working record1624

18 November 2026. One RESEARCH / proof_audit / conceptual_audit under
the unchanged SPECIALIZE assessment1623 supplied at invocation.

Target is exactly its combined E_o/S allowance on r>=e^12,
sigma>=-r/(4 log r). Main RH positivity and Mellin-to-sign bridge
remain independent gaps. Continue only with a complete uniform proof
or a specific checkable defect; failure of a sufficient envelope is
not failure of the actual allowance.

Read C048a in full, the fixed-ray and complete-kernel portions of L804,
audit538, history1622 and source notes1623. C048a is the mathematical
input. L804 is a method comparison, not an imported numerical bound.
Existing notebook work is preserved. Initial scoped git status was
unexpectedly large and truncated; no inference from omitted changes
is used and no existing lemma is being overwritten.

Unfinished plan: derive explicit Lambert clearance from w exp(w)=2p/pi;
bound the complete theta sum on the short strip and a Cauchy disc;
estimate the primitive, retained vertical segment and low horizontal
piece relative to the exact S. Treat tau>=r/2, sigma<0 and small tau,
then reflection and zero height. All numerical bounds remain unproved
at this checkpoint. No source estimate is assumed true.

## Developed attempt (still requiring complete write-up)

At fixed y, combine the two paths and deform to the straight ray
ending at 1+iy. Write q=sqrt(1+y^2), beta=atan y, a0=1/4.
The continued ray is sum c_n(a0 exp(i beta))^(2p+2n)/(p+n)
plus twice the ray integral from a0 to q. Equality first holds for
sigma>0, then meromorphically at fixed y. This retains rather than
discards the original finite vertical segment.

Candidate uniform controls: U>3L/4>=9, |w|<U+2<L+2,
cos V>1/(4L). The latter relaxed clearance suffices for a full-strip
bound M_L<10^7 L^(5/2); a radius-1/2 disc gives |c_n|<10^8 4^n.
Only that coefficient bound is needed, not source's second bound.

With b=|w|/2 and alpha=arg w, the exact phase denominator is
H=2sigma log b-2tau alpha-2 Re(p/w). Its remaining amplitude has
inverse <=sqrt r because sqrt(|1+w|) exp(-9U/4)/(8pi^(5/2))<1.
Let A=1/2-2/U-2/U^2>41/162. Since beta>=y/2,
beta-alpha-V/|w|^2 >= y A. For sigma>=0, use q^(2sigma);
loss >=2sigma(log(b/q)-1/U)+2tau y A. Here b/q>3,
and for tau>=r/2, y>9/40, giving loss>41r/720>r/32.
For sigma<0 use a0^(2sigma), tau>99r/100, y>27/40;
loss >=2tau y A-r log(2(L+2))/(2L)>r(1353/4000-1/6)>r/32.
The last log term is <r/6 for L>=12 by monotonicity and log28<4.
For tau<r/2, sigma>4r/5 and direct ray integration gives loss>64r/45.

The two continued-ray terms have prefactor <10^9 L^(5/2);
small tau's direct prefactor is <10^7 L^(5/2). Thus a candidate
stronger result is 10^9 L^(5/2) sqrt(r) exp(-r/32).
All equalities, inequalities, closed cases and the final threshold
will be checked in the canonical proof; this scratch record is not
verification or a completed theorem.

## Completion

The complete argument and all constants are now written canonically in
C048b. It proves the stronger 10^9 envelope and the nominated 10^19
envelope's final allocation. No source defect was needed or claimed;
the straight-ray estimate is a disclosed alternative proof of the
combined allowance. Independent critical review remains the nominated
continuation. This working record is preserved, not promoted as proof.
