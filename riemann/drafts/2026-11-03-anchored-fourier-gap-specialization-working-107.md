# Anchored Fourier-gap specialization — step 107

The invocation-start SPECIALIZE assessment approves precisely the anchored
infinite half-lattice test. Reused its primary comparison and source proof
reading; no additional literature search or finite-transfer claim is needed.
The local duplicate/failure checks used L665's hypotheses/conclusion, L666's
exact family and the signed-canonical attempt's recorded infinite/finite gap.
All pre-existing edits and unfinished work were preserved.

The main unresolved claim is actual-Xi all-degree mixed positivity. The
intermediate target is existence of the specified infinite Fourier gap with
the fixed atom, unit masses and shifts bounded by 1/8. Its possible use is to
test collective cancellation versus anchor protection, with no implication
yet for L666's finite complete logarithmic loss. Continue the application only
if its phase, coefficient norm and displacement cap work exactly; otherwise
reject it. No minimum gap width is required.

Checkpoint of the applicability calculation: fix a=1/8, b=3/8, c=1/4 and
epsilon=1/8 before taking Lev's delta>0. For an even smooth cutoff eta with
0<=eta<=1, eta=1 on [-1/2,1/2] and support in [-1,1], set

    h=min(1/32,delta/8),
    chi(t)=eta((t-c)/h)+eta((t+c)/h),
    S(t)=-exp(pi*i*t)*chi(t).

The bands are disjoint and strictly inside Lev's prescribed open bands.
S is Hermitian and sup_k |S-hat(k)|<=||S||_1<=4h<=delta/2.
For nu=sum_m delta_(m+e_m), Lev gives nu-hat=delta_0+S on (-b,b).
After translation by 1/2 and addition of the fixed atom,

    mu-hat=1+delta_0+exp(-pi*i*t)*S=1+delta_0-chi

on that interval. It vanishes on J=(c-h/2,c+h/2). The requested
angular-frequency interval is I=2*pi*J. Unit weights and shifts are unchanged.

The completed proof, source statement, distributional qualifications and
limitations are canonical in `lemmas/L693-anchored-half-lattice-fourier-gap.md`.
This is REPRODUCTION / source specialization, not an originality claim or
an RH candidate. No mathematical script or numerical certificate is needed.
The construction is existential and supplies no effective lower bound on h,
no unsmoothed finite-tail estimate and no rational-W/all-moment/logarithmic
transfer. A separate audit is the next proposed target, requiring separate
approval of its newly recorded assessment scope.
