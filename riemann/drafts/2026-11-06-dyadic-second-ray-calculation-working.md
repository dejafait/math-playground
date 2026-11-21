# Dyadic second ray — exact coefficient attempt

2026-11-06. RESEARCH/calculation under the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-06-dyadic-cubic-infinite-tail-second-ray.md`.
The exact approved target alone is being tested. L030–L032/C032a actual-Xi
mixed positivity remains open. Prior finite all-ray and generic
log-concavity stops were checked; neither decides this infinite product.

For H(t)=1/F(-t), product self-similarity gives
P(-t)H(t)=H(t/2), hence h_0=1, negative subscripts zero and
(1-2^(-n))h_n=2h_(n-1)-2h_(n-2)+h_(n-3), n>=1.
The covered rectangular identity for partition (r,r), conjugate (2^r),
should identify the desired second-ray determinant with
h_r^2-h_(r-1)h_(r+1). This orientation and fixed-rank passage still
need canonical documentation.

Preliminary exact fractions: h_4=64/7, h_5=1280/217,
h_6=52736/13671. The rank-five difference is
-1409024/2966607<0. This is a preliminary calculation until the
ordinary-coefficient matrix is independently evaluated and the
analytic/identity applicability is written out. No truncation or
numerical asymptotic is needed. A negative exact minor rejects this
family's all-shift ansatz, not RH or other infinite products.

Next within this attempt: write a full rational certificate with both
the original 5-by-5 determinant and the rectangular expression; document
the recurrence, analytic scope and exact result in one canonical lemma.
L841's independent first-ray audit remains pending; only its analytic
product setup is needed here. No new pole mechanism, higher shift or
parameter-family calculation is authorized in this step.

## Completion

The canonical proof is now in
`lemmas/L842-dyadic-cubic-negative-second-ray-minor.md`.
The original ordinary-coefficient 5-by-5 determinant, evaluated by its
complete rational Leibniz sum, agrees exactly with the rectangle route:
-1409024/2966607. All five grouped checks pass in
`scripts/dyadic-cubic/second-ray-exact-certificate.json`.
This informative negative stops the exact model's all-shift ansatz.
No higher-shift, modified-family or Xi calculation was performed.
