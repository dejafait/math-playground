# Fixed-shift pole attempt, step668 — preserved working note

Completed: the full proof, exact constants and qualifications are canonical
in `../lemmas/L834-fixed-shift6002-reciprocal-pole-ray.md`. The partial
reasoning below records the checkpoint before that write-up; its pending
checks were completed within the approved attempt. A separate critical
audit remains outstanding. No numerical certificate was needed or created.

Approved scope: the unchanged SPECIALIZE assessment
`literature/2026-11-05-fixed-shift-reciprocal-pole-test.md`, only k=6002.
Main gap: actual-Xi all-degree mixed positivity. Test one eventual positive
ray with unbounded rank; stop on unpaid simplicity, isolation, sign or
relative error. No effective onset, neighboring shift or growing-k claim.

Inputs read: L018/L021/L776 normalization, L832 height/product input,
step667's source assessment and the reciprocal algebra stop. The latter
still blocks signing by duality alone. No cross-notebook input.

Primary Platt–Trudgian v1 Theorem1 and Section2, pp.2–3, were inspected:
the verification counts sign changes and matches the expected total by
Turing's method. Matching disjoint sign-change intervals to the count with
multiplicity forces each to contain one simple zero. No individual decimal
enclosure is required for an existential contour.

Pending canonical write-up: put F(z)=G(-z)/a0 and p_j=4 gamma_j^2.
For the first k+1 positive ordinates, use R=(p_k+p_(k+1))/2. Higher
off-line images have modulus 4((beta-1/2)^2+gamma^2)>4H^2. Subtract
principal parts A_j/(1-z/p_j) of 1/F, A_j=-1/(p_j F'(p_j)). The
crossing signs give sign A_j=(-1)^(j-1). A finite contour constant M
bounds the remaining coefficients by M R^(-n), n>=0.

The proposed leading matrix on h_(r+j-i) factors as U diag(A_l p_l^(-r)) V,
U_(i,l)=p_l^i, V_(l,j)=p_l^(-j). The two Vandermonde signs and the
residue-product sign cancel. The inverse norm is at most a fixed constant
times p_k^r; the shifted remainder norm is at most another fixed constant
times R^(-r). Thus the intended paid ratio is C(p_k/R)^r ->0.

Still to check before treating this as complete: the imported finite-minor
identity with a0^r and both parity factors, all negative indices, the
precise meromorphic-theorem hypotheses, and real determinant transfer.
The complete proof will be canonical in L834 if those checks succeed.
